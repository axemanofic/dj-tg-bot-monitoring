import traceback

from .utils import send_message


def report_bug(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except Exception as e:
            send_message(str(traceback.format_exc()))
    return wrapper
