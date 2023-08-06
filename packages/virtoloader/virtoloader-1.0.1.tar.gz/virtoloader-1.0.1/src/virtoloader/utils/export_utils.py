"""Contains utility functions for the main processes."""

import os
import shutil
import tarfile
import zipfile
import re
from pathlib import Path
from typing import List


def extract_file(file_path: str, output_dir: str) -> None:
    """Extracts files from a compressed directory.

    Supported types: zip, tar, tar.gz

    Args:
        file_path: Path of the source file
        outputdir: Path of the destination directory

    Raises:
        ValueError if type not supported.
    """
    if file_path.endswith(".tar.gz") or file_path.endswith(".tar"):
        with tarfile.open(file_path) as tar:
            tar.extractall(os.path.join(output_dir, file_path.split(".")[0]))
    elif file_path.endswith(".zip"):
        with zipfile.ZipFile(file_path) as zipp:
            zipp.extractall(os.path.join(output_dir, file_path.split(".")[0]))
    else:
        raise ValueError("File type not supported.")


def clean_text(string: str) -> str:
    """Replaces special characters in a string with an underscore.

    Args:
        string: String to clean

    Returns:
        str: Cleaned string in lower case.
    """
    to_remove = ["*", ".", ",", '"', "\\", "/", "|", "[", "]", ":", ";", " "]
    for symbol in to_remove:
        string = string.replace(symbol, "_")
    return string.lower()


def delete_series_folders(parent_dir: str, lenght: int = 30) -> List[str]:
    """Deletes series folders that have less than <lenght> dicom files.

    Args:
        parent_dir: Path to the parent directory (e.g: to STD00001 in this case)
        lenght: Number of dicom files threshold

    Returns:
        The paths' list of the deleted series folders.
    """
    deleted = []
    for root, _, files in os.walk(parent_dir):
        if (
            len(files) < lenght
            and bool(re.match(r"SER\d{5}", os.path.basename(root)))
        ):
            deleted.append(root)
            shutil.rmtree(root)
        if len(files) < lenght and os.path.basename(root) in ["None", "NA"]:
            deleted.append(root)
            shutil.rmtree(root)
    return deleted


def create_filesystem(
    root_dir: str, parent_folder: str, series_number: str, std: str = "STD00001"
) -> str:
    """Creates the directory tree down to the series folder.

    Args:
        root_dir: Path of the destination directory
        parent_folder: Name of the patient folder where the series will be stored
        std: Name of the study folder

    Returns:
        Path to the series folder.
    """

    Path(os.path.join(root_dir, parent_folder, std, series_number)).mkdir(
        parents=True, exist_ok=True
    )
    return os.path.join(root_dir, parent_folder, std, series_number)


def exported_filename(*args) -> str:
    """Creates a filename composed from *args and dcm extension.

    Returns:
        A filename
    """
    return ".".join((args + ("dcm",)))
