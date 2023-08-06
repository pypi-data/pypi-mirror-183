from importlib import resources
import warnings


def get_flatland():
    """
    Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to example text file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """

    warnings.warn(
        "This function is deprecated and will be removed in a future version.",
        DeprecationWarning,
    )

    with resources.path("pycounts_k108.data", "flatland.txt") as f:
        data_file_path = f
    return data_file_path
