"""Test for anomaly_data_viz config."""


import os

from dotenv import load_dotenv

from src.anomaly_data_viz.config import AppConfig


def test_config_typing():
    """Test config typing."""
    load_dotenv()
    app_config = AppConfig(
        name=os.environ.get("APP_NAME"),
        title=os.environ.get("APP_TITLE"),
        debug=os.environ.get("DEBUG"),
        host=os.environ.get("APP_HOST"),
        port=os.environ.get("APP_PORT"),
        repository=os.environ.get("APP_REPOSITORY"),
        assets_folder=os.environ.get("APP_ASSETS_FOLDER"),
    )
    assert isinstance(app_config.name, str)
    assert isinstance(app_config.title, str)
    assert isinstance(bool(app_config.debug), bool)
    assert isinstance(app_config.host, str)
    assert isinstance(int(app_config.port), int)
    assert isinstance(app_config.repository, str)
    assert isinstance(app_config.assets_folder, str)


def test_config_set_debug_mode():
    """Test config set debug mode."""
    load_dotenv()
    app_config = AppConfig(
        name=os.environ.get("APP_NAME"),
        title=os.environ.get("APP_TITLE"),
        debug=os.environ.get("DEBUG"),
        host=os.environ.get("APP_HOST"),
        port=os.environ.get("APP_PORT"),
        repository=os.environ.get("APP_REPOSITORY"),
        assets_folder=os.environ.get("APP_ASSETS_FOLDER"),
    )
    current_mode = bool(app_config.debug)
    app_config.set_debug_mode(~current_mode)
    assert app_config.debug == ~current_mode


def test_config_repr():
    """Test config repr method."""
    load_dotenv()
    app_config = AppConfig(
        name=os.environ.get("APP_NAME"),
        title=os.environ.get("APP_TITLE"),
        debug=os.environ.get("DEBUG"),
        host=os.environ.get("APP_HOST"),
        port=os.environ.get("APP_PORT"),
        repository=os.environ.get("APP_REPOSITORY"),
        assets_folder=os.environ.get("APP_ASSETS_FOLDER"),
    )
    app_config_repr = repr(app_config)
    assert isinstance(app_config_repr, str)
    assert len(app_config_repr) > 0
