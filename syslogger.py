from datetime import datetime
import logging
import sys

import dirs


def _create_syslogger():
    logger = logging.getLogger(dirs.APP_NAME)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d [%(filename)s:%(funcName)s:%(lineno)d] - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler = logging.FileHandler(dirs.SYSLOG_DIR / datetime.now().strftime('syslog_%Y-%m-%d_%H%M%S.txt'))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Application started")
    return logger
syslogger = _create_syslogger()

