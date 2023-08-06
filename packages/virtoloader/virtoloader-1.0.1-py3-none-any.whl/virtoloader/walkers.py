"""Contains filesystem walkers, i.e. directories iterators."""

import os
from typing import List

from virtoloader.dicom_handler import DICOMStandardHandler

# pylint: disable=too-few-public-methods
class RawScanner:
    """Scans a raw data directory for DICOM files."""

    def __init__(
        self, src_dir: str, reader: DICOMStandardHandler, attributes: List[str]
    ) -> None:
        """Initializes the RawScanner class.

        Args:
            src_dir (str): The directory to scan.
            reader (DICOMStandardHandler): A DICOM reader/handler.
            attributes (List[str]): A list of DICOM attributes to be used for validation."""

        self.src_dir = src_dir
        self.reader = reader
        self.attributes = attributes
        self.valid_dicoms: list = []
        self.non_dicoms: list = []

    def get_all_dicoms(self, src_dir) -> tuple[list, list]:
        """Gets all DICOM, and non-DICOM files, from a directory.

        Args:
            src_dir (str): The directory to scan.

        Returns:
            tuple[list,list]: A tuple containing two lists, one with the paths of all valid DICOM
            files, and the other with the paths of all non-DICOM files."""
        for entry in os.scandir(src_dir):
            if entry.is_file():
                dcm_path = entry.path
                dicom = self.reader.read_as_dicom(dcm_path)
                if self.reader.is_valid_dicom(dicom, self.attributes):
                    self.valid_dicoms.append(dcm_path)
                else:
                    self.non_dicoms.append(dcm_path)
            elif entry.is_dir():
                self.get_all_dicoms(entry.path)

        return (self.valid_dicoms, self.non_dicoms)
