"""Test for anomaly_data_viz utils."""

import base64
import csv
from io import StringIO

import pandas as pd

from anomaly_data_viz import __version__
from src.anomaly_data_viz.utils import upload_file


def test_version():
    """Test app version."""
    assert __version__ == "0.1.0"


def test_load_empty_file():
    """Test load empty string file."""
    dataset = upload_file("", "")
    assert dataset.shape == (0, 0)


def test_load_non_empty_file():
    """Test load non_empty string file."""
    data = [["complex", "3i"], ["real", 15], ["rational", 2.5], ["integer", 2]]
    file_input = StringIO()
    csv.writer(file_input).writerows(data)
    encoded_input = base64.b64encode(file_input.getvalue().encode()).decode()
    payload = "text/csv;base64," + encoded_input
    dataset = upload_file(payload, "numbers.csv")
    assert isinstance(dataset, pd.core.frame.DataFrame)
    assert dataset.shape[0] > 0
