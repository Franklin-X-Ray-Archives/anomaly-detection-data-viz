from app import *
from config import *



def main():
    app.run_server(debug=True, host=AppConfig.host , port=AppConfig.port )


if __name__ == "__main__":
    main()
