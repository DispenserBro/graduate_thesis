import os
import logging
from datetime import datetime

from bot.utils.files import LOGS_DIR


if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

if os.path.exists(LOGS_DIR / "latest.log"):
    os.remove(LOGS_DIR / "latest.log")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    filename=LOGS_DIR / 'latest.log'
)
file_handler.setLevel(logging.INFO)

date_file_handler = logging.FileHandler(
    filename=LOGS_DIR / f'{datetime.today().date().strftime("%d-%m-%Y")}.log'
)
date_file_handler.setLevel(logging.INFO)

debug_file_handler = logging.FileHandler(
    filename=LOGS_DIR / f'{datetime.today().date().strftime("%d-%m-%Y")}_debug.log'
)
debug_file_handler.setLevel(logging.DEBUG)

default_fmt = "[%(levelname)+8s:%(name)-18s] - %(asctime)s : %(funcName)s @ %(lineno)04d: %(message)s"

time_formatter = logging.Formatter(
    fmt=default_fmt,
    datefmt="%H:%M:%S"
    )

date_time_formatter = logging.Formatter(
    fmt=default_fmt,
    datefmt="%d/%m/%Y - %H:%M:%S"
    )

console_handler.setFormatter(date_time_formatter)
file_handler.setFormatter(date_time_formatter)
date_file_handler.setFormatter(time_formatter)
debug_file_handler.setFormatter(date_time_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(date_file_handler)
logger.addHandler(debug_file_handler)