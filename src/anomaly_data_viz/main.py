"""Configure and run app server."""
from app import app
from config import AppConfig


def main() -> int:
    """Main function, entrypoint for running app server."""
    app.run_server(debug=True, host=AppConfig.host, port=AppConfig.port)
    return 0


if __name__ == "__main__":
    main()
