import requests
from .conf import configuration
from .consts import TELEGRAM_METHOD


def send_message(message: str):
    data = {
        "text": message,
        "chat_id": ""
    }
    chats = configuration.TELEGRAM_BOT.get('CHATS', set())
    for chat_id in chats:
        data['chat_id'] = chat_id
        requests.post(TELEGRAM_METHOD, json=data)
