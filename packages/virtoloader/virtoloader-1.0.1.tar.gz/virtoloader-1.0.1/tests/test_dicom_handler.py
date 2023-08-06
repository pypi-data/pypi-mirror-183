""" Tests the DICOM handlers module."""

from dataclasses import asdict
import pytest
import pydicom

from src.virtoloader import dicom_handler
from src.virtoloader import data_objs

# pylint: disable=fixme
class TestDICOMHandler:
    """Tests the DICOMHandler class."""

    @pytest.fixture
    def handler(self):
        """DICOMHandler instance."""
        return dicom_handler.DICOMHandler()

    @pytest.fixture
    def checker(self):
        """DICOMChecker instance."""
        return data_objs.ToValidateDICOM()

    @pytest.fixture
    def patients(self):
        """Test patients info."""
        patients = {
            "ecmo": {
                "test_dicom": "tests/test_data/IM01553",
                "PatientID": "ECMO02",
            },
            "hannover": {
                "test_dicom": "tests/test_data/IM00166",
                "PatientID": "19",
            },
            "medira-err": {
                "test_dicom": "tests/test_data/-CC--078.dcm",
                "PatientID": "yXSaoXA",
            },
        }
        return patients

    def test_read_dicom(self, handler, patients):
        """Tests the read_as_dicom method."""

        dicom = handler.read_dicom(patients["ecmo"]["test_dicom"])
        assert isinstance(dicom, pydicom.dataset.FileDataset)
        assert dicom.get("PatientID") == patients["ecmo"]["PatientID"]

        with pytest.raises(FileNotFoundError):
            handler.read_dicom("tests/test_data/IM01553.dcm")

        # TODO
        # with pytest.raises(pydicom.errors.InvalidDicomError):

    def test_read_as_dicom(self, handler, patients):
        """Tests the read_as_dicom method."""

        dicom = handler.read_as_dicom(patients["hannover"]["test_dicom"])
        assert isinstance(dicom, pydicom.dataset.FileDataset)
        assert dicom.get("PatientID") == patients["hannover"]["PatientID"]

        with pytest.raises(FileNotFoundError):
            handler.read_as_dicom("tests/test_data/IM01553.dcm")

    def test_get_attribute(self, handler, patients):
        """Tests the get_attribute method."""

        dicom = handler.read_dicom(patients["ecmo"]["test_dicom"])
        assert (
            handler.get_attribute(dicom, "PatientID") == patients["ecmo"]["PatientID"]
        )
        dicom = handler.read_as_dicom(patients["hannover"]["test_dicom"])
        assert (
            handler.get_attribute(dicom, "PatientID")
            == patients["hannover"]["PatientID"]
        )
        assert handler.get_attribute(dicom, "PatientAddress") is None

    def test_get_attribue_elsena(self, handler, patients):
        """Tests the get_attribute_elsena method."""

        dicom = handler.read_as_dicom(patients["hannover"]["test_dicom"])
        assert (
            handler.get_attribute_elsena(dicom, "PatientID")
            == patients["hannover"]["PatientID"]
        )
        assert handler.get_attribute_elsena(dicom, "PatientAddress") == "NA"

    def test_get_attribue_elsezero(self, handler, patients):
        """Tests the get_attribute_elsezero method."""

        dicom = handler.read_dicom(patients["ecmo"]["test_dicom"])
        assert (
            handler.get_attribute_elsezero(dicom, "PatientID")
            == patients["ecmo"]["PatientID"]
        )
        assert handler.get_attribute_elsezero(dicom, "PatientAddress") == "0"

    def test_is_valid_dicom(self, handler, checker, patients):
        """Tests the is_valid_dicom method of the DICOMHandler class."""

        dicom = handler.read_dicom(patients["ecmo"]["test_dicom"])
        assert handler.is_valid_dicom(dicom, list(asdict(checker).values())) is True
        dicom = handler.read_dicom(patients["medira-err"]["test_dicom"])
        assert handler.is_valid_dicom(dicom, list(asdict(checker).values())) is False

    def test_inplace_decompression(self, handler, patients):
        """Tests the inplace_decompression method of the DICOMHandler class."""

        dicom = handler.read_dicom(patients["medira-err"]["test_dicom"])
        assert handler.inplace_decompression(dicom) is None
        dicom = handler.read_dicom(patients["ecmo"]["test_dicom"])
        assert handler.inplace_decompression(dicom) == "Success"
