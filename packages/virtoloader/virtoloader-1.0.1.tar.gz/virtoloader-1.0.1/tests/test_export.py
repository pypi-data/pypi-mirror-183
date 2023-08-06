"""Tests the export module."""

import os
import tempfile
import pytest

from src.virtoloader import export


@pytest.fixture(name="source_dir")
def fxt_source_dir():
    """Raw data test directory."""
    return "tests/test_data"


def test_main(source_dir):
    """Tests the main function."""

    with tempfile.TemporaryDirectory() as tmp_dir:
        export.main(source_dir, tmp_dir)
        assert len(os.listdir(tmp_dir)) == 5
        assert "ecmo02-anonymus^kiba-ecmo" in os.listdir(tmp_dir)
