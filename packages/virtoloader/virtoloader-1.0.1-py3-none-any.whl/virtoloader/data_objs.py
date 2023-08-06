"""Data objects for VirtoLoader."""

import dataclasses


@dataclasses.dataclass(frozen=True)
class ToValidateDICOM:
    """DICOM attributes to use for validation."""

    instance_uid: str = "SOPInstanceUID"
    pixel_data: str = "PixelData"


# pylint: disable=too-many-instance-attributes
@dataclasses.dataclass(slots=True)
class DICOMAttributes:
    """Attributes to be read from DICOM files."""

    patient_id: str = "PatientID"
    patient_name: str = "PatientName"
    series_number: str = "SeriesNumber"
    instance_number: str = "InstanceNumber"
    acquisition_number: str = "AcquisitionNumber"
    acquisition_date: str = "AcquisitionDate"
    instance_creation_date: str = "InstanceCreationDate"
    series_instance_uid: str = "SeriesInstanceUID"
    modality: str = "Modality"


@dataclasses.dataclass(slots=True)
class Patient:
    """Attributes to define a patient."""

    patient_id: str
    patient_name: str
    folder_name: str = dataclasses.field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.folder_name = f"{self.patient_id}-{self.patient_name}"


@dataclasses.dataclass(slots=True)
class Acquisition:
    """Attributes to define an acquisition."""

    series_number: str
    instance_number: str
    acquisition_number: str
    acquisition_date: str
    instance_creation_date: str
    series_instance_uid: str
    modality: str

    def __post_init__(self) -> None:
        if self.series_number not in ["NA", "None"]:
            self.series_number = f"SER{int(self.series_number):05}"
        if self.instance_number not in ["NA", "None"]:
            self.instance_number = f"{int(self.instance_number):05}"
