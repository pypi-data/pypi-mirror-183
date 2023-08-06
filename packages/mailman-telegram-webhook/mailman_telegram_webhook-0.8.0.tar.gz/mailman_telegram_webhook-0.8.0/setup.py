# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mailman_telegram_webhook']

package_data = \
{'': ['*']}

install_requires = \
['python-telegram-bot>=13.15,<14.0']

setup_kwargs = {
    'name': 'mailman-telegram-webhook',
    'version': '0.8.0',
    'description': 'A small archiver sending message to telegram chats.',
    'long_description': '# Mailman Telegram Webhook\n\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![Code style black](https://img.shields.io/badge/code%20style-black-000000.svg)]("https://github.com/psf/black)\n[![GitHub release](https://img.shields.io/github/release/nanoy42/dinomail.svg)](https://github.com/nanoy42/dinomail/releases/)\n[![PyPI version fury.io](https://badge.fury.io/py/mailman-telegram-webhook.svg)](https://pypi.org/project/mailman-telegram-webhook/)\n\nWant to send message to telegram chats when receiving an email on a mailing list ? This script do it for you.\n\n## Installation\n\n### Installation procedure\n\nIt is possible to install the package via pip :\n\n```\npip install mailman-telegram-webhook\n```\n\nbut make sure to install it at good location. The config file is also downloaded with the python file.\n\nCreate the folder `/usr/lib/python3/dist-packages/mailman_telegram_webhook` and copy the `__init__.py` file inside.\n\nYou will need the python-telegram-bot package (as specified in the dependencies files).\n\nThen copy the `mailam-telegram-webhook.cfg` file to `/ect/mailman3` and edit it :\n\n * You need to set the token to a valid telegram bot token\n * If you want, you can specify a global chat id. Messages will be sent to this chat when the archiver is enabled for a mailing-list but no specific chat id is defined. If you leave this chat id empty, nothing happens when the archiver is enabled for a list without specific chat id.\n * You can specify specific chat id in `[list.list_name]` sections\n\nThen copy the following code to mailman configuration (`/etc/mailman3/mailman.cfg`) :\n```\n[archiver.telegram_webhook]\nclass: mailman_telegram_webhook.Archiver\nenable: yes\nconfiguration: /etc/mailman3/mailman-telegram-webhook.cfg\n```\n\nNote : By default, the archiver will be enable on every list and if a global chat id is defined, messages will be sent from every list to this chat.\n\n### Configuration examples\n\n```\n[global]\ntoken = 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11\nchat_id = 103\n\n[list.contact]\nchat_id = 104\n```\n\nWe suppose that contact@my.domain and webmaster@my.domain have the archiver enabled and the token `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` (which is an example token) is associated to myBot.\n\n * A mail sent to contact@my.domain will make myBot send a message to the chat with id 104.\n * A mail sent to webmaster@my.domain will make myBot send a message to the the chat with id 103.\n\n```\n[global]\ntoken = 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11\n\n[list.contact]\nchat_id = 104\n```\n\nWe suppose that contact@my.domain and webmaster@my.domain have the archiver enabled and the token `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` (which is an example token) is associated to myBot.\n\n * A mail sent to contact@my.domain will make myBot send a message to the chat with id 104.\n * A mail sent to webmaster@my.domain will make do nothing.\n\n## Under the hood\n\nThis little script acts as an archiver (like Hyperkitty). When a message is received by mailman, if the archiver is configured and enabled on the mailing list, the message is passed to the archiver. The `archive_function` function just sends a message to telegram, according to the configuration.\n\nThe code is widely adapted from https://github.com/ondrejkolin/mailman_to_rocketchat and from Hyperkitty.\n\n## FAQ\n\n### How do I obtain a telegram bot token ?\n\nYou need to create a bot by speaking with @BotFather (see here for more information : https://core.telegram.org/bots)\n\n### How do I find chat ids ?\n\nYou can chat with some specific bots to find the chat id or you can use the bot you created. Invite him on the group or chat with him and take a look to `https://api.telegram.org/bot<token>/getUpdates`\n\n### What looks like the message on telegram ?\n\nThe message looks like `New message from {from} to {to} : {subject}`.\n\nExample :\n\n`New message from Yoann Pietri <me@nanoy.fr> to webmaster@my.domain : [Webmaster] Unable to access website`.\n\n### Can I change the message on telegram ?\n\nNo. You cannot change it in the configuration but you can edit the message in the `__init__.py` file, in the `archive_message` function. \n',
    'author': 'Yoann Piétri',
    'author_email': 'me@nanoy.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nanoy42/mailman-telegram-webhook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
