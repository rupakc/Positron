import datetime
import logging
import daiquiri
from constants import commonconstants


def get_logger(name):
    daiquiri.setup(
        level=logging.DEBUG,
        outputs=(
            daiquiri.output.File(commonconstants.LOG_FILE_PATH, level=logging.ERROR),
            daiquiri.output.TimedRotatingFile(
                commonconstants.LOG_FILE_PATH,
                level=logging.DEBUG,
                interval=datetime.timedelta(hours=1))
        )
    )
    logger = daiquiri.getLogger(name)
    return logger
