"""Configure and run app server."""
import os

from dotenv import load_dotenv
from pydantic import ValidationError

from anomaly_data_viz.app import App
from anomaly_data_viz.config import AppConfig


def main() -> int:
    """Main function, entrypoint for running app server."""
    load_dotenv()
    try:
        app_config = AppConfig(
            name=str(os.environ.get("APP_NAME")),
            title=str(os.environ.get("APP_TITLE")),
            debug=bool(os.environ.get("DEBUG")),
            host=str(os.environ.get("APP_HOST")),
            port=5000,
            repository=str(os.environ.get("APP_REPOSITORY")),
            assets_folder=str(os.environ.get("APP_ASSETS_FOLDER")),
        )

        App.app.run(debug=app_config.debug, host=app_config.host, port=app_config.port)
        # App.app.run( *app_config.__dict__ )
        return 0
    except ValidationError as e:
        print(e.json())
        return -1


if __name__ == "__main__":
    main()
