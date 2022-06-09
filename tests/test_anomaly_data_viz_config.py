"""Test for anomaly_data_viz config."""


from src.anomaly_data_viz.config import AppConfig


def test_config_repr():
    """Test config repr method."""
    app_config = AppConfig()
    app_config_repr = repr(app_config)
    assert isinstance(app_config_repr, str)
    assert len(app_config_repr) > 0
