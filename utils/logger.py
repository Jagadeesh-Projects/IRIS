import logging
import os

from config.settings import settings


os.makedirs(settings.LOG_DIRECTORY, exist_ok=True)


logging.basicConfig(
    filename=f"{settings.LOG_DIRECTORY}/iris.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger("IRIS")