# -*- coding: UTF-8 -*-

from datetime import date
import os
import logging

# Loggers
# ==============================================================================

LOGS_DIR_NAME = 'logs'
LOGS_FILE_EXT = '.log'

def get_logger(appname, enum_each_exec=False):
    """
    Obtains a logger
    Args:
        appname: the name of the app to be logged
    """
    this_file_path = os.path.dirname(os.path.realpath(__file__))

    logs_dir = os.path.join(this_file_path, LOGS_DIR_NAME)
    if (not os.path.isdir(logs_dir)):
        os.mkdir(logs_dir)

    app_logs_dir = os.path.join(logs_dir, appname)
    if (not os.path.isdir(app_logs_dir)):
        os.mkdir(app_logs_dir)

    base_log_filename = date.today().strftime(f"{appname}_%Y-%m-%d")

    log_full_filename = os.path.join(app_logs_dir, f"{base_log_filename}{LOGS_FILE_EXT}")

    logger = logging.getLogger(appname)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_full_filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s'))
    logger.addHandler(file_handler)
    return logger
