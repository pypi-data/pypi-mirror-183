"""DICOM handler module."""

import os
from pathlib import Path
from typing import Protocol, List, Iterator, Any
import pydicom


class DICOMStandardHandler(Protocol):
    """Protocol for a DICOM standard handler."""

    def read_dicom(self, dicom_file_path: str) -> object:
        """Reads a DICOM file."""

    def read_as_dicom(self, dicom_file_path: str) -> object:
        """Reads a file as a DICOM file."""

    def get_attribute(self, dicom_obj: object, attribute: str) -> str | None:
        """Gets the value of a DICOM attribute."""

    def is_valid_dicom(self, dicom_obj: object, attributes: Any) -> bool:
        """Checks if a DICOM object is valid."""

    def save(self, dicom_obj: object, dst_dir: str, filename: str) -> None:
        """Saves a DICOM object to a file."""


class DICOMHandler(DICOMStandardHandler):
    """Provides operations on DICOM files.

    This class contains a variety of methods to work with DICOMs.
    """

    def read_dicom(
        self, dicom_file_path: str, no_pixel_data: bool = False
    ) -> pydicom.dataset.FileDataset:
        """Reads a DICOM file.

        Reads the content of a DICOM file and retrieves it as an object.

        Args:
            dicom_file_path (str): Path to the DICOM file.
            no_pixel_data (bool): If True, the pixel data will not be read.

        Returns:
            pydicom.dataset.Dataset: A pydicom dataset object.

         Raises:
            FileNotFoundError: If the DICOM file does not exist.
            pydicom.errors.InvalidDicomError: If the DICOM file is invalid.
        """
        if not Path(dicom_file_path).is_file():
            raise FileNotFoundError(f"DICOM file not found: {dicom_file_path}")
        try:
            dicom_dataset = pydicom.dcmread(
                str(dicom_file_path), stop_before_pixels=no_pixel_data
            )
        except Exception as exc:
            raise pydicom.errors.InvalidDicomError(
                f"Invalid DICOM file: {dicom_file_path}"
            ) from exc
        return dicom_dataset

    def read_as_dicom(
        self, dicom_file_path: str, no_pixel_data: bool = False
    ) -> pydicom.dataset.FileDataset:
        """Reads a file as a DICOM file.

        Reads the content of file as if it was a DICOM file,
        and retrieves it as an object.

        Args:
            dicom_file_path (str): Path to the file.
            no_pixel_data (bool): If True, the pixel data will not be read.

        Returns:
            pydicom.dataset.Dataset: A pydicom dataset object.
        """
        if not Path(dicom_file_path).is_file():
            raise FileNotFoundError(f"DICOM file not found: {dicom_file_path}")
        return pydicom.dcmread(
            str(dicom_file_path), stop_before_pixels=no_pixel_data, force=True
        )

    def get_attribute(  # type: ignore[override]
        self, dicom_obj: pydicom.dataset.FileDataset, attribute: str
    ) -> str | None:
        """Fetch an attribute from a DICOM file.

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.
            attribute (str): Attribute to be fetched.

        Returns:
            Attribute stored as it is in the DICOM object.
        """
        return dicom_obj.get(attribute)

    def get_attribute_elsena(
        self, dicom_obj: pydicom.dataset.FileDataset, attribute: str
    ) -> str:
        """Fetch an attribute from a DICOM file, if doesn't exist returns "NA".

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.
            attribute (str): Attribute to be fetched.

        Returns:
            Attribute as a string from the DICOM object, or "NA".
        """
        return str(dicom_obj.get(attribute, "NA"))

    def get_attribute_elsezero(
        self, dicom_obj: pydicom.dataset.FileDataset, attribute: str
    ) -> str:
        """Fetch an attribute from a DICOM file, if doesn't exist returns "0".

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.
            attribute (str): Attribute to be fetched.

        Returns:
            Attribute as a string from the DICOM object, or "0".
        """
        return str(dicom_obj.get(attribute, "0"))

    def _check_attributes(
        self, dicom_obj: pydicom.dataset.FileDataset, attributes: List[str]
    ) -> Iterator[bool]:
        """Checks if DICOM attribute exists.

        Generator to check if the specified DICOM object has the required
        attributes defined to be considered valid. It yields the result of each attribute check.

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.
            attributes (List[str]): List of attributes to be checked.

        Yields:
            bool: True if the attribute is present, False otherwise.
        """
        for attr in attributes:
            yield self.get_attribute(dicom_obj, attr) is not None

    def is_valid_dicom(# type: ignore[override]
        self,
        dicom_obj: pydicom.dataset.FileDataset,  
        attributes: List[str],
    ) -> bool:

        """Checks if a DICOM object is valid.

        This function checks if the specified DICOM object has the required attributes defined to be
        considered valid.

        Args:
            dicom_obj (pydicom.dataset.FileDataset): The DICOM object to be validated.
            attributes (List[str]): A list of attributes to be checked.

        Returns:
            bool: True if the DICOM object is valid, False otherwise.
        """
        attribute_checks = self._check_attributes(dicom_obj, attributes)

        return all(attribute_checks)

    def inplace_decompression(
        self, dicom_obj: pydicom.dataset.FileDataset
    ) -> str | None:
        """
        Decompresses a DICOM file in-place.

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.

        Returns:
            A string if successful, otherwise None.
        """
        try:
            dicom_obj.decompress()
            return "Success"
        except (NotImplementedError, AttributeError):
            return None

    def save(  # type: ignore[override]
        self, dicom_obj: pydicom.dataset.FileDataset, dst_dir: str, filename: str
    ) -> None:
        """
        Saves a DICOM file in a given path.

        Args:
            dicom_obj (pydicom.dataset.Dataset): A pydicom dataset object.
            dst_dir (str): Path to the destination directory.
            filename (str): Name of the file to be saved.
        """
        dicom_obj.save_as(os.path.join(dst_dir, filename))
