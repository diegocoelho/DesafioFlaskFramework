import logging
import logging.handlers
from flask import has_request_context, request


class LogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = '%(levelname)-5s %(asctime)s %(name)-8s  %(message)s'
        fmt_date = '%d/%m/%Y %T'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)