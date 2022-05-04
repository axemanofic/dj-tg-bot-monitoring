from typing import List, Any, AnyStr
from django.apps import AppConfig
from django.core.checks import Error

from .conf import configuration


def check_settings(app_configs: List[AppConfig], **kwargs: Any) -> List[Error]:
    errors = []
    if configuration.TELEGRAM_BOT:
        if not isinstance(configuration.TELEGRAM_BOT, dict):
            errors.append(
                Error(
                    "TELEGRAM_BOT should be a dict.",
                    id="django_telegram_exceptions.E001"
                )
            )
        if not isinstance(configuration.TELEGRAM_BOT.get('TOKEN', 'no_token'), str):
            errors.append(
                Error(
                    "Key TOKEN should be a str.",
                    id="django_telegram_exceptions.E003"
                )
            )
        if not isinstance(configuration.TELEGRAM_BOT.get('CHATS', set()), set):
            errors.append(
                Error(
                    "Key CHATS should be a set.",
                    id="django_telegram_exceptions.E004"
                )
            )
    else:
        if not isinstance(configuration.TELEGRAM_BOT, bool):
            errors.append(
                Error(
                    "TELEGRAM_BOT should be a bool.",
                    id="django_telegram_exceptions.E002"
                )
            )
    return errors
