"""Configure and run app server."""
import os

from app import App
from config import AppConfig
from dotenv import load_dotenv
from pydantic import ValidationError


def main() -> int:
    """Main function, entrypoint for running app server."""
    load_dotenv()
    try:
        app_config = AppConfig(
            name=os.environ.get("APP_NAME"),
            title=os.environ.get("APP_TITLE"),
            debug=os.environ.get("DEBUG"),
            host=os.environ.get("APP_HOST"),
            port=os.environ.get("APP_PORT"),
            repository=os.environ.get("APP_REPOSITORY"),
            assets_folder=os.environ.get("APP_ASSETS_FOLDER"),
        )

        App.app.run(debug=app_config.debug, host=app_config.host, port=app_config.port)
        # App.app.run( *app_config.__dict__ )
        return 0
    except ValidationError as e:
        print(e.json())
        return -1


if __name__ == "__main__":
    main()
