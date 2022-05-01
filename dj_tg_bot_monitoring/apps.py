from django.apps import AppConfig
from django.core.checks import Tags, register

from .checks import check_settings


class DjangoBotExceptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_bot_exceptions'

    def ready(self) -> None:
        register(Tags.security)(check_settings)
