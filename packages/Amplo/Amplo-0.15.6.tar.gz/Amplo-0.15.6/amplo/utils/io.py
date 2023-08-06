#  Copyright (c) 2022 by Amplo.

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from time import time
from typing import TYPE_CHECKING, Iterable
from warnings import warn

import numpy as np
import pandas as pd
from requests import HTTPError

from amplo.api.storage import AzureBlobDataAPI
from amplo.utils.logging import get_root_logger

if TYPE_CHECKING:
    from logging import Logger

    from amplo.api.platform import AmploPlatformAPI

__all__ = [
    "boolean_input",
    "parse_json",
    "NpEncoder",
    "read_pandas",
    "get_file_metadata",
    "merge_logs",
]


FILE_READERS = {
    ".csv": pd.read_csv,
    ".json": pd.read_json,
    ".xml": pd.read_xml,
    ".feather": pd.read_feather,
    ".parquet": pd.read_parquet,
    ".stata": pd.read_stata,
    ".pickle": pd.read_pickle,
}


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.Series):
            return obj.to_list()
        if isinstance(obj, pd.DataFrame):
            obj.to_json()
        return super(NpEncoder, self).default(obj)


def boolean_input(question: str) -> bool:
    x = input(question + " [y / n]")
    if x.lower() == "n" or x.lower() == "no":
        return False
    elif x.lower() == "y" or x.lower() == "yes":
        return True
    else:
        warn('Sorry, I did not understand. Please answer with "n" or "y"')
        return boolean_input(question)


def parse_json(json_string: str | dict) -> str | dict:
    if isinstance(json_string, dict):
        return json_string
    else:
        try:
            return json.loads(
                json_string.replace("'", '"')
                .replace("True", "true")
                .replace("False", "false")
                .replace("nan", "NaN")
                .replace("None", "null")
            )
        except json.decoder.JSONDecodeError:
            warn(f"Cannot validate, impassable JSON: {json_string}")
            return json_string


def read_pandas(path: str | Path) -> pd.DataFrame:
    """
    Wrapper for various read functions

    Returns
    -------
    pd.DataFrame
    """
    file_extension = Path(path).suffix
    if file_extension not in FILE_READERS:
        raise NotImplementedError(f"File format {file_extension} not supported.")
    else:
        reader = FILE_READERS[file_extension]
        return reader(path, low_memory=False)


def get_file_metadata(file_path: str | Path) -> dict[str, str | float]:
    """
    Get file metadata from given path.

    Parameters
    ----------
    file_path : str or Path
        File path.

    Returns
    -------
    dict of {str: str or float}
        File metadata.

    Raises
    ------
    FileNotFoundError
        When the path does not exist.
    IsADirectoryError
        When the path resolves a directory, not a file.
    """

    from amplo.utils import check_dtypes

    check_dtypes("file_path", file_path, (str, Path))

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist: '{file_path}'")
    if not file_path.is_file():
        raise IsADirectoryError(f"Path is not a file: '{file_path}'")

    return {
        "file_name": str(file_path.name),
        "full_path": str(file_path.resolve()),
        # "creation_time": os.path.getctime(str(file_path)),
        "last_modified": os.path.getmtime(str(file_path)),
    }


def _get_api_clients(
    azure: tuple[str, str] | bool = False,
    platform: tuple[str, str] | bool | None = None,
):
    """
    Gathers the api clients for merge_logs
    """
    from amplo.api.platform import AmploPlatformAPI

    if not azure:
        blob_api = None
    else:
        azure = azure if not isinstance(azure, bool) else tuple()
        blob_api = AzureBlobDataAPI.from_os_env(*azure)

    # Mirror azure parameter when platform is not set
    if platform is None:
        platform = bool(azure)
    # Get amplo platform client
    if not platform:
        platform_api = None
    else:
        platform = platform if not isinstance(platform, bool) else tuple()
        platform_api = AmploPlatformAPI.from_os_env(*platform)
    return blob_api, platform_api


def _get_folders(
    parent_folder: str | Path,
    blob_api: AzureBlobDataAPI | None = None,
    more_folders: list[str | Path] | None = None,
) -> list[Path]:
    """
    Lists folders for merge_logs
    """
    if not blob_api:
        if not Path(parent_folder).exists():
            raise ValueError(f"{parent_folder} directory does not exist.")
        folders = [
            folder for folder in Path(parent_folder).iterdir() if folder.is_dir()
        ]
    else:
        folders = blob_api.ls_folders(parent_folder)

    # Add more_folders
    if more_folders:
        folders += more_folders

    # return [Path(f) for f in folders]
    return [Path(f) for f in folders]


def _read_files_in_folders(
    folders: Iterable[str | Path],
    target: str,
    blob_api: AzureBlobDataAPI | None = None,
    logger: Logger | None = None,
) -> tuple[list[str], pd.DataFrame, dict[str, dict]]:
    """
    Use pandas to read all non-hidden and non-empty files into a DataFrame.

    Parameters
    ----------
    folders : iterable of (str or Path)
        Directory names.
    target : str
        Target column & directory name
    blob_api : AzureBlobDataAPI or None, optional, default: None
        If None, tries to read data from local folder, else from Azure
    logger : Logger or None, optional, default: None
        When provided, will log progress every 90 seconds.

    Returns
    -------
    filenames : list of str
    data : pd.DataFrame
        All files of the folders merged into one multi-indexed DataFrame.
    metadata : list of dict of {str : str or float}

    Warnings
    --------
    UserWarning
        When any directory is empty, or has no supported file type.
    """

    # Map folders to pathlib.Path object
    folders = [Path(f) for f in folders]

    # Initialize
    file_names, data, metadata = [], [], {}
    last_time_logged = time()
    for folder_count, folder in enumerate(sorted(folders)):

        # List all files
        if blob_api:
            files = list(map(Path, blob_api.ls_files(folder)))
        else:
            files = [f for f in folder.iterdir() if f.is_file()]

        # Remove hidden files
        hidden_files = [f for f in files if re.match(r"^\..*", f.name)]
        files = list(set(files) - set(hidden_files))

        # Remove unsupported file types
        unsupported_files = [f for f in files if f.suffix not in FILE_READERS]
        files = list(set(files) - set(unsupported_files))

        # Remove empty files
        if blob_api:
            empty_files = [f for f in files if blob_api.get_size(f) == 0]
        else:
            empty_files = [f for f in files if f.stat().st_size == 0]
        files = list(set(files) - set(empty_files))

        # Sanity check
        if not files:
            warn(f"Directory is empty and thus skipped: '{folder}'")
            continue

        # Read files
        for file_ in sorted(files):
            if logger:
                logger.debug(file_)

            # read_pandas() may raise an EmptyDataError when the file has no content.
            # The try...except catches such errors and warns the user instead.
            try:
                if blob_api:
                    datum = blob_api.read_pandas(file_, low_memory=False)
                    metadatum = blob_api.get_metadata(file_)
                else:
                    datum = read_pandas(file_)
                    metadatum = get_file_metadata(file_)
            except pd.errors.EmptyDataError:
                warn(f"Empty file detected and thus skipped: '{file_}'")
                continue

            # Convert to dataframe
            if isinstance(datum, pd.Series):
                datum = datum.to_frame()

            # Set multi-index
            datum = datum.set_index(
                pd.MultiIndex.from_product(
                    [[str(file_)], datum.index.values], names=["log", "index"]
                )
            )

            # Add target
            datum[target] = (folder.name == target) * 1

            # Append
            file_names.append(str(file_))
            data.append(datum)
            metadata[str(file_)] = metadatum

        if logger and time() - last_time_logged > 90:
            last_time_logged = time()
            logger.info(f".. progress: {folder_count / len(folders) * 100:.1f} %")

    # Concatenate data
    data = pd.concat(data, axis=0)

    # Validate data
    if target not in data:
        raise ValueError("Target not in data.")
    if data[target].nunique() != 2:
        raise ValueError(f"Number of unique labels is {data[target].nunique()} != 2.")

    return file_names, data, metadata


def _map_datalogs_to_file_names(
    file_names: list[str],
    platform_api: AmploPlatformAPI | None = None,
    logger: Logger | None = None,
) -> dict:
    """
    Get datalogs for every filename.

    Parameters
    ----------
    file_names : list of str
        Files names to get datalogs from - if available.
    platform_api : AmploPlatformAPI or None, optional, default: None
        API to get datlogs from.
    logger : Logger or None, optional, default: None
        When provided, will log progress every 90 seconds.

    Returns
    -------
    list of dict
        Datalogs for every filename.
    """

    if not platform_api:
        return {}

    # It is assumed that the 6th and 5th path position of the (first) filename contains
    # the team and machine name, respectively, if you count from right to left.
    # E.g., "Team/Machine/data/Category/Issue/log_file.csv"

    # Remove path prefixes, otherwise datalogs will not be found
    file_names = ["/".join(str(fname).split("/")[-6:]) for fname in file_names]
    # Extract team and machine
    try:
        team, machine = file_names[0].split("/")[-6:-4]
    except IndexError:
        warn(f"Got an empty list of file names")
        return {}

    # Get datalog for each filename
    datalogs = {}
    last_time_logged = time()
    for file_count, fname in enumerate(file_names):
        try:
            datalog = platform_api.get_datalog(team, machine, fname)
        except HTTPError:
            # No matching datalog found. Do still append it to preserve the order.
            datalog = {}

        datalogs[fname] = datalog

        if logger and time() - last_time_logged > 90:
            last_time_logged = time()
            logger.info(f".. progress: {file_count / len(file_names) * 100:.1f} %")

    return datalogs


def _mask_intervals(datalogs: dict, data: pd.DataFrame) -> pd.DataFrame:
    """
    Masks the data with the intervals given by the datalogs.

    Parameters
    ----------
    datalogs : list of dict
        Datalogs dictionary that should contain the keys 'selected' and 'datetime_col'.
    data : pd.DataFrame
        Data for splitting.

    Returns
    -------
    data_out : pd.DataFrame
        Selected data.

    Warnings
    --------
    UserWarning
        When no valid match for the start or stop time of the data interval was found,
        i.e. when the time difference is more than 1 second.
    """
    for filename in data.index.get_level_values("log").unique():
        # Get intervals and timestamp column from datalog
        datalog = datalogs.get(filename, {})
        intervals = datalog.get("selected", [])
        ts_col = datalog.get("datetime_col", "")

        # Validate
        if not intervals or not ts_col:
            continue
        elif ts_col not in data:
            warn(f"Cannot select intervals as the column '{ts_col}' is not present.")
            continue

        # Convert ts_col
        if not pd.api.types.is_numeric_dtype(data[ts_col]):
            data[ts_col] = (
                pd.to_datetime(data[ts_col], errors="coerce").view(int) / 10**9
            )

        # Extract intervals
        drop_mask = True
        for interval in intervals:
            ts_first, ts_last = interval
            drop_mask = (
                (data[ts_col] < ts_first) | (data[ts_col] > ts_last)
            ) & drop_mask
        if isinstance(drop_mask, pd.Series) and not drop_mask.loc[filename].any():
            continue
        data = data.drop(data.loc[(filename, drop_mask), :].index)

    return data


def merge_logs(
    parent: str | Path,
    target: str,
    more_folders: list[str | Path] | None = None,
    azure: tuple[str, str] | bool = False,
    platform: tuple[str, str] | bool | None = None,
) -> tuple[pd.DataFrame, dict[str, dict]]:
    """
    Combine log files of all subdirectories into a multi-indexed DataFrame.

    The function can handle logs from a local directory as well as data coming from an
    Azure blob storage. For the latter case it is furthermore capable to select
    intervals using Amplo's datalogs.

    Notes
    -----
    Make sure that each protocol is located in a subdirectory whose name represents the
    respective label.

    An exemplary directory structure of ``parent_folder``:
        ``
        parent_folder
        ├─ Label_1
        │   ├─ Log_1.*
        │   └─ Log_2.*
        ├─ Label_2
        │   └─ Log_3.*
        └─ ...
        ``

    Parameters
    ----------
    parent_folder : str or Path
        Directory that contains subdirectories with tabular data files.
    target : str
        The target folder.
    more_folders : list of str or Path, optional
        Additional folder names with tabular data files to append.
    azure : (str, str) or bool, default: False
        Use this parameter to indicate that data is in Azure blob storage.
        If False, it is assumed that data origins from local directory.
        If True, the AzureBlobDataAPI is initialized with default OS env variables.
        Otherwise, it will use the tuple to initialize the api.
    platform : (str, str) or bool or None, default: None
        Use this parameter for selecting data according to Amplo's datalogs.
        If None, its value is set to bool(azure).
        If False, no datalogs information will be used.
        If True, the AmploPlatformAPI is initialized with default OS env variables.
        Otherwise, it will use the tuple to initialize the api.
    verbose : int, default = 1


    Returns
    -------
    data : pd.DataFrame
        All files of the folders merged into one multi-indexed DataFrame.
        Multi-index names are 'log' and 'index'.
    metadata : dict of {int : dict of {str : str or float}}
        Metadata of merged data.
    """
    from amplo.utils import check_dtypes

    logger = get_root_logger()
    check_dtypes(
        ("parent_folder", parent, (str, Path)),
        ("target_col", target, str),
        ("more_folders", more_folders, (type(None), list)),
    )

    # Get azure blob client
    blob_api, platform_api = _get_api_clients(azure, platform)

    # Get child folders
    folders = _get_folders(parent, blob_api)
    if target not in [f.name for f in folders]:
        raise ValueError(f"Target {target} not present in folders.")
    logger.info(f"Found {len(folders)} folders.")

    # Pandas read files
    fnames, data, metadata = _read_files_in_folders(folders, target, blob_api, logger)
    logger.info(f"Found {len(fnames)} files.")

    # Masking data
    if platform_api:
        logger.info("Reading datalogs from platform")
        datalogs = _map_datalogs_to_file_names(fnames, platform_api, logger)
        if datalogs:
            logger.info("Masking intervals from datalogs")
            data = _mask_intervals(datalogs, data)

    return data, metadata
