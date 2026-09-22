import os
from dotenv import load_dotenv


load_dotenv()


class Settings:

    APP_NAME = "IRIS"

    VERSION = "0.1.0"

    DEBUG = (
        os.getenv("DEBUG", "True").lower() == "true"
    )

    # Root directory of the IRIS project
    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    # Data directory
    DATA_DIRECTORY = os.path.join(
        BASE_DIR,
        "data"
    )

    # SQLite database
    DATABASE_PATH = os.path.join(
        DATA_DIRECTORY,
        "iris.db"
    )

    # Log directory
    LOG_DIRECTORY = os.path.join(
        DATA_DIRECTORY,
        "logs"
    )

    MAX_MEMORY_RESULTS = 5


settings = Settings()