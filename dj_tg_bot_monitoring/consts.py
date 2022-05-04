from .conf import configuration

TELEGRAM_METHOD = f"https://api.telegram.org/bot{configuration.TELEGRAM_BOT.get('TOKEN')}/sendMessage"
