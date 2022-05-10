# dj-tg-bot-monitoring

Exception monitoring in django using telegram bot

## Features

* Middleware to send your exclusions to telegram
* Decorator to send exceptions to telegram

## Contents
* [How install?](#how-install) 
* [How to work with it?](#how-to-work-with-it) 
* [Set up a django app](#set-up-a-django-app) 
* [How to use @report_bug?](#how-to-use-report_bug)
  * [A Simple Example](#a-simple-example)
* [Have questions?](#have-questions)


## How install?

[Poetry](https://python-poetry.org/)

```sh
poetry add git+https://github.com/axemanofic/dj-tg-bot-monitoring.git
```

or [PIP](https://pip.pypa.io/)

```sh
pip install git+https://github.com/axemanofic/dj-tg-bot-monitoring.git
```

## How to work with it?

1. Create telegram bot via [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. [Set up a django app](#set-up-a-django-app)

## Set up a django app

In ``settings.py`` add the following:

```python
MIDDLEWARE = [
    ...
    'dj_tg_bot_monitoring.middlewares.TelegramExceptionsMiddleware',
    ...
]

INSTALLED_APPS = [
    ...
    'dj_tg_bot_monitoring',
]
```

Now add the following settings:

```python
TELEGRAM_BOT = {
    # Your bot token
    "TOKEN": os.getenv('TG_TOKEN'), # Or 'TG_TOKEN'
    # List of user IDs to whom the error notification will be sent 
    # (Attention!!! The bot will send a message only if you started a dialogue with it)
    "CHATS": {
        '123456', # this is your telegram ID
    }
}
```

That's it, now if an error occurs in your application, the Telegram Bot will notify you about it

## How to use ``@report_bug``?

This decorator was created so that you can handle specific functions not related to HTTP requests.

### A Simple Example

```python
from dj_tg_bot_monitoring.decorators import report_bug 

@report_bug(name_task="MyTaskName")
def test_func(some_params):
    1 / 0
```

## Have questions?

If you have questions then "welcome" to my [telegram](https://t.me/axemanofic) 