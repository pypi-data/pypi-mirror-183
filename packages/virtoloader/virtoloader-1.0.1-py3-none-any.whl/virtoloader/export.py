"""Export DICOM data to filesystem."""

import logging
import warnings
import argparse
from dataclasses import asdict
from typing import Optional

from virtoloader import walkers
from virtoloader import dicom_handler
from virtoloader import data_objs
from virtoloader.utils import export_utils

warnings.filterwarnings("ignore")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
csl = logging.StreamHandler()
csl.setLevel(logging.INFO)
file_formatter = logging.Formatter("%(asctime)s : %(filename)-3s : %(message)s")
file_handler = logging.FileHandler("export.log")
csl_formatter = logging.Formatter("%(asctime)s : %(levelname)-3s : %(message)s")
file_handler.setFormatter(file_formatter)
csl.setFormatter(csl_formatter)
logger.addHandler(file_handler)
logger.addHandler(csl)


def exp_parser() -> argparse.ArgumentParser:
    """Parser for the export module."""

    parser = argparse.ArgumentParser(
        prog="export to filesystem", usage="%(prog)s [options]"
    )
    parser.add_argument(
        "src_dir",
        metavar="source raw data directory.",
        help="absolute path to the raw data directory.",
    )
    parser.add_argument(
        "dst_dir",
        metavar="data destination directory.",
        help="absolute path to the destination directory to export DICOM files to.",
    )

    return parser


def main(src_dir: str, dst_dir: str, deletion: Optional[bool] = False) -> None:
    """Main function of the export module.

    Acts as a backbone caller. Contains the sequence logic
    and object instances of the several elements of the export module.

    Args:
        src_dir (str): The source directory to scan for DICOM files.
        dst_dir (str): The destination directory to export DICOM files to.

    """
    logger.info("Process initiated.")
    logger.info("Source directory: %s", src_dir)
    logger.info("Destination directory: %s", dst_dir)
    handler = dicom_handler.DICOMHandler()
    attrs = data_objs.DICOMAttributes()
    checker = data_objs.ToValidateDICOM()
    scanner = walkers.RawScanner(src_dir, handler, list(asdict(checker).values()))
    dcms, nondcms = scanner.get_all_dicoms(src_dir)
    logger.info("%s valid dicom files found.", len(dcms))
    logger.info("%s non-dicom files found.", len(nondcms))
    logger.debug("Non-dicom files: %s", nondcms)
    for dcm in dcms:
        dicom = handler.read_as_dicom(dcm)
        patient = data_objs.Patient(
            export_utils.clean_text(
                handler.get_attribute_elsena(dicom, attrs.patient_id)
            ),
            export_utils.clean_text(
                handler.get_attribute_elsena(dicom, attrs.patient_name)
            ),
        )
        acquisition = data_objs.Acquisition(
            handler.get_attribute_elsena(dicom, attrs.series_number),
            handler.get_attribute_elsena(dicom, attrs.instance_number),
            handler.get_attribute_elsena(dicom, attrs.acquisition_number),
            handler.get_attribute_elsena(dicom, attrs.acquisition_date),
            handler.get_attribute_elsena(dicom, attrs.instance_creation_date),
            handler.get_attribute_elsena(dicom, attrs.series_instance_uid),
            handler.get_attribute_elsena(dicom, attrs.modality),
        )
        if not handler.inplace_decompression(dicom):
            logger.warning("Decompressing error in %s", dcm)
        series_path = export_utils.create_filesystem(
            dst_dir, patient.folder_name, acquisition.series_number
        )
        handler.save(
            dicom,
            series_path,
            export_utils.exported_filename(
                acquisition.modality,
                acquisition.series_instance_uid,
                acquisition.instance_number,
            ),
        )
    if deletion:
        deleted_folders = export_utils.delete_series_folders(dst_dir)
        logger.info("%s series folders were deleted.", len(deleted_folders))
        logger.debug("The following series folders were deleted: %s", deleted_folders)
    logger.info("Process completed.")


if __name__ == "__main__":
    args = exp_parser().parse_args()
    main(args.src_dir, args.dst_dir)
