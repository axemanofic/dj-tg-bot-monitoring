import traceback

from .utils import send_message


def report_bug(name_task="Task name"):
    def wrapper(func):
        def main(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                send_message(
                    f"Task: *{name_task}*"
                    f"\n\n"
                    f"{str(traceback.format_exc())}",
                    parse_mode="MARKDOWN")
        return main
    return wrapper
