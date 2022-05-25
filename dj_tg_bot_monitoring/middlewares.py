import traceback
from django.http import HttpRequest

from .utils import send_message


class TelegramExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        return self.get_response(request)

    async def process_exception(self, request: HttpRequest, exception: Exception):
        """Logging Exceptions"""
        send_message(str(traceback.format_exc()))
