"""Test for anomaly_data_viz app"""

from anomaly_data_viz import __version__
from src.anomaly_data_viz.utils import upload_file


def test_version():
    """Test app version"""
    assert __version__ == "0.1.0"


def test_load_empty_file():
    """Test load empty string file"""
    dataset = upload_file("", "")
    assert dataset.shape == (0, 0)
