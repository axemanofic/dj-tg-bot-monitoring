import requests
from .conf import configuration
from .consts import TELEGRAM_METHOD


def send_message(message: str, parse_mode="HTML"):
    data = {
        "text": message,
        "chat_id": "",
        "parse_mode": parse_mode
    }
    chats = configuration.TELEGRAM_BOT.get('CHATS', set())
    for chat_id in chats:
        data['chat_id'] = chat_id
        requests.post(TELEGRAM_METHOD, json=data)
