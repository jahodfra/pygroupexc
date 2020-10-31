import logging
import sys

import pygroupexc


class ExceptionAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg, kwargs = super().process(msg, kwargs)
        exc_info = kwargs.get('exc_info')
        if exc_info:
            exc_info = sys.exc_info()
            msg += f'\nException id: {pygroupexc.exception_id(exc_info=exc_info)}'
        return msg, kwargs


logger = ExceptionAdapter(logging.getLogger(), {})

try:
    raise ValueError()
except ValueError:
    logger.exception('Test')
