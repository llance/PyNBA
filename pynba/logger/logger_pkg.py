import time
import logging
import logging.handlers
import sys
from configurationfile import logging_config


def setup_custom_logger(name):
    # logger settings

    log_file = logging_config['LOGGING_DIRECTORY'] + '/' + logging_config['LOGGING_FILENAME']
    log_file_max_size = 1024 * 1024 * 20 # megabytes
    log_num_backups = 3
    log_format = "%(asctime)s [%(levelname)s]: %(filename)s(%(funcName)s:%(lineno)s) >> %(message)s"
    log_date_format = "%m/%d/%Y %I:%M:%S %p"
    log_filemode = "w" # w: overwrite; a: append

    # setup logger
    # datefmt=log_date_format
    logging.basicConfig(
                        filename=log_file + time.strftime("%Y%m%d%H%M%S") + '.log', 
                        level=logging.DEBUG,
                        filemode=log_filemode,
                        format="%(asctime)s [%(levelname)s]: %(filename)s(%(funcName)s:%(lineno)s) >> %(message)s"
                        )

    rotate_file = logging.handlers.RotatingFileHandler(
                                                        log_file + time.strftime("%Y%m%d%H%M%S") + '.log', 
                                                        maxBytes=log_file_max_size, 
                                                        backupCount=log_num_backups
                                                        )
    
    logger = logging.getLogger(name)
    logger.addHandler(rotate_file)

    # print log messages to console
    consoleHandler = logging.StreamHandler()
    logFormatter = logging.Formatter(log_format)
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    return logger


    