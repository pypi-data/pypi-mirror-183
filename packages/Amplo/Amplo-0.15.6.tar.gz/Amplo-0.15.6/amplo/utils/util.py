#  Copyright (c) 2022 by Amplo.

from __future__ import annotations

import functools
import inspect
import logging
import re
import warnings
from collections.abc import Generator

import pandas as pd

__all__ = [
    "get_model",
    "hist_search",
    "clean_feature_name",
    "clean_column_names",
    "deprecated",
    "check_dtypes",
]


def get_model(model_str: str):
    from sklearn import ensemble, linear_model, svm

    from amplo import classification, regression
    from amplo.base import BasePredictor

    model: BasePredictor

    if "RandomForest" in model_str or "Bagging" in model_str:
        model = getattr(ensemble, model_str)()
    elif model_str == "SVC":
        model = svm.SVC(probability=True)  # type: ignore
    elif model_str == "SVR":
        model = svm.SVR()  # type: ignore
    elif "Logistic" in model_str or "Linear" in model_str or "Ridge" in model_str:
        model = getattr(linear_model, model_str)()
    elif "Classifier" in model_str:
        model = getattr(classification, model_str)()
    elif "Regressor" in model_str:
        model = getattr(regression, model_str)()
    else:
        raise ValueError("Model not recognized.")
    return model


def hist_search(array, value):
    """
    Binary search that finds the index in order to fulfill
    ``array[index] <= value < array[index + 1]``

    Parameters
    ----------
    array : array of float
    value : float

    Returns
    -------
    int
        Bin index of the value
    """

    # Return -1 when no bin exists
    if value < array[0] or value >= array[-1]:
        logging.debug(
            f"No bin (index) found for value {value}. "
            f"Array(Min: {array[0]}, "
            "Max: {array[-1]})"
        )
        return -1

    # Initialize min and max bin index
    low = 0
    high = len(array) - 1

    # Bin search
    countdown = 30
    while countdown > 0:
        # Count down
        countdown -= 1

        # Set middle bin index
        middle = low + (high - low) // 2

        if low == middle == high - 1:  # stop criterion
            return middle

        if value < array[middle]:  # array[low] <= value < array[middle]
            high = middle
        elif value >= array[middle]:  # array[middle] <= value < array[high]
            low = middle

    warnings.warn("Operation took too long. Returning -1 (no match).", RuntimeWarning)
    return -1


def clean_feature_name(feature_name: str | int) -> str:
    """
    Clean feature names and append "feature_" when it's a digit.

    Parameters
    ----------
    feature_name : str or int
        Feature name to be cleaned.

    Returns
    -------
    cleaned_feature_name : str
    """
    # Handle digits
    if isinstance(feature_name, int) or str(feature_name).isdigit():
        feature_name = f"feature_{feature_name}"

    # Remove non-numeric and non-alphabetic characters.
    # Assert single underscores and remove underscores in prefix and suffix.
    return re.sub("[^a-z0-9]+", "_", feature_name.lower()).strip("_")


def clean_column_names(data: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, str]]:
    """
    Cleans column names.

    NOTE:
        This used to take care of duplicate columns after cleaning the feature names.
        This is no longer the case, and the data processor should take care of duplicate
        columns.

    Parameters
    ----------
    data : pd.DataFrame
        Data to be cleaned.

    Returns
    -------
    pd.DataFrame
        Same data but with cleaned column names.
    dict of {str : str}
        Dictionary which indicates the renaming.
    """
    # Make first renaming attempt. May create duplicated names.
    renaming = pd.Series({old: clean_feature_name(old) for old in data.columns})
    return data.rename(columns=renaming), renaming.to_dict()  # type: ignore


def deprecated(reason):
    # This decorator is a copy-pase from:
    # https://stackoverflow.com/questions/2536307/decorators-in-the-python-standard-lib-deprecated-specifically
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """
    string_types = (type(b""), type(""))

    if isinstance(reason, string_types):

        # The @deprecated is used with a 'reason'.
        #
        # .. code-block:: python
        #
        #    @deprecated("please, use another function")
        #    def old_function(x, y):
        #      pass

        def decorator(func1):

            if inspect.isclass(func1):
                fmt1 = "Call to deprecated class {name} ({reason})."
            else:
                fmt1 = "Call to deprecated function {name} ({reason})."

            @functools.wraps(func1)
            def new_func1(*args, **kwargs):
                warnings.simplefilter("always", DeprecationWarning)
                warnings.warn(
                    fmt1.format(name=func1.__name__, reason=reason),
                    category=DeprecationWarning,
                    stacklevel=2,
                )
                warnings.simplefilter("default", DeprecationWarning)
                return func1(*args, **kwargs)

            return new_func1

        return decorator

    elif inspect.isclass(reason) or inspect.isfunction(reason):

        # The @deprecated is used without any 'reason'.
        #
        # .. code-block:: python
        #
        #    @deprecated
        #    def old_function(x, y):
        #      pass

        func2 = reason

        if inspect.isclass(func2):
            fmt2 = "Call to deprecated class {name}."
        else:
            fmt2 = "Call to deprecated function {name}."

        @functools.wraps(func2)
        def new_func2(*args, **kwargs):
            warnings.simplefilter("always", DeprecationWarning)
            warnings.warn(
                fmt2.format(name=func2.__name__),
                category=DeprecationWarning,
                stacklevel=2,
            )
            warnings.simplefilter("default", DeprecationWarning)
            return func2(*args, **kwargs)

        return new_func2

    else:
        raise TypeError(repr(type(reason)))


def check_dtypes(*dtype_tuples):
    """
    Checks all dtypes of given list.

    Parameters
    ----------
    *dtype_tuples : Any
        Tuples of (name, parameter, allowed types) to be checked.
        When checking only one parameter, the wrapping in a tuple can be omitted.

    Returns
    -------
    None

    Examples
    --------
    Check a single parameter:
    >>> check_dtypes(("var1", 123, int))  # tuple
    >>> check_dtypes("var1", 123, int)  # without tuple

    Check multiple:
    >>> check_dtypes(("var1", 123, int), ("var2", 1.0, (int, float)))  # tuples
    >>> check_dtypes(("var", var, str) for var in ["a", "b"])  # list or generator

    Raises
    ------
    ValueError
        If any given constraint is not fulfilled.
    """
    # Allow single dtype check without wrapping in a tuple
    if isinstance(dtype_tuples[0], str):
        if len(dtype_tuples) != 3:
            raise TypeError("Invalid arguments for `check_dtypes` function.")
        dtype_tuples = (dtype_tuples,)

    # Allow single list or generator object
    if isinstance(dtype_tuples[0], (list, Generator)):
        if len(dtype_tuples) != 1:
            raise TypeError("Invalid arguments for `check_dtypes` function.")
        dtype_tuples = dtype_tuples[0]

    # Check dtypes
    for name, value, typ in dtype_tuples:
        if not isinstance(value, typ):
            msg = f"Invalid dtype for argument `{name}`: {type(value).__name__}"
            raise TypeError(msg)
