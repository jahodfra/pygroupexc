"""
Small library for providing unique identifier to similar exceptions

1) we check just filename and function name
2) we don't check line numbers because they often change e.g. by unrelated changes
3) we check exception type but not message as the message can often differ for similar problems

the code is public-domain
written by Frantisek Jahoda
"""

import sys
import hashlib


def format_exception(exc_info=None):
    if not exc_info:
        exc_info = sys.exc_info()
    exc_class, _, traceback = exc_info
    rows = []
    while traceback:
        code = traceback.tb_frame.f_code
        rows.append((code.co_filename, code.co_name))
        traceback = traceback.tb_next
    rows.append(exc_class.__name__)
    return rows


def exception_id(exc_info=None):
    return hashlib.md5(str(format_exception(exc_info)).encode()).hexdigest()

