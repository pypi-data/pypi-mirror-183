""" Tests the walkers module."""

from src.virtoloader import walkers
from src.virtoloader import dicom_handler

# pylint: disable=too-few-public-methods
class TestRawScanner:
    """Tests the RawScanner class."""

    def test_get_all_dicoms(self):
        """Tests the get_all_dicoms method of the RawScanner class."""

        handler = dicom_handler.DICOMHandler()

        scanner = walkers.RawScanner(
            "tests/test_data", handler, ["SOPInstanceUID", "PixelData"]
        )
        valid_dcms, nondcms = scanner.get_all_dicoms("tests/test_data")
        assert len(valid_dcms) == 11
        assert len(nondcms) == 2

        # with invalid attributes
        scanner = walkers.RawScanner(
            "tests/test_data", handler, ["RandomField", "PixelData"]
        )
        valid_dcms, nondcms = scanner.get_all_dicoms("tests/test_data")
        assert len(valid_dcms) != 11
        assert len(nondcms) != 2
