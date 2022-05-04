import traceback
import requests
from django.http import HttpRequest

from .conf import configuration

TELEGRAM_METHOD = f"https://api.telegram.org/bot{configuration.TELEGRAM_BOT.get('TOKEN')}/sendMessage"


class TelegramExceptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        return self.get_response(request)

    async def process_exception(self, request: HttpRequest, exception: Exception):
        """ Логирование Exception """
        data = {
            "text": str(traceback.format_exc()),
            "chat_id": ""
        }
        chats = configuration.TELEGRAM_BOT.get('CHATS', set())
        for chat_id in chats:
            data['chat_id'] = chat_id
            requests.post(TELEGRAM_METHOD, json=data)
