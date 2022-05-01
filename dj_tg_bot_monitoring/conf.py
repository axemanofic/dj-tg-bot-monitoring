from django.conf import settings
from typing import Union


class Settings:
    @property
    def TELEGRAM_BOT(self) -> Union[dict, bool]:
        return getattr(settings, "TELEGRAM_BOT", False)


configuration = Settings()
