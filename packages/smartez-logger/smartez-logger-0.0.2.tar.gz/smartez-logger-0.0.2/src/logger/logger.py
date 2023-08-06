import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def log_to_console(level, prog_info, message):
    # ERROR = 1, INFO = 2, DEBUG = 3
    if int(os.getenv('LOG_LVL')) > 0 and level == 'ERROR':
        print(level, prog_info, message)
    if int(os.getenv('LOG_LVL')) > 1 and level == 'INFO':
        print(level, prog_info, message)
    if int(os.getenv('LOG_LVL')) > 2 and level == 'DEBUG':
        print(level, prog_info, message)
