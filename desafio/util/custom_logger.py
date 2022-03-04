import logging
import logging.handlers
from logging import getLogger
from functools import wraps


class LogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = '%(levelname)-5s %(asctime)s %(message)s'
        fmt_date = '%d/%m/%Y %T'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)
        self.setLevel(logging.DEBUG)


def log(func):
    @wraps(func)
    def generate_log(*args, **kwargs):
        logger = getLogger(__name__)
        output = func(*args, **kwargs)
        logger.info('{}\t{}\t{}'.format(func.__name__, output[1], output[0].get_json()))
        return output
    return generate_log
