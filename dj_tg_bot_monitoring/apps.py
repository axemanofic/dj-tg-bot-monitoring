from django.apps import AppConfig
from django.core.checks import Tags, register

from .checks import check_settings


class DjangoTelegramBotMonitoringConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj_tg_bot_monitoring'

    def ready(self) -> None:
        register(Tags.security)(check_settings)
