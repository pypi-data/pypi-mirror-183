# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mailhog']

package_data = \
{'': ['*']}

install_requires = \
['dataclass-wizard>=0.22.2,<0.23.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'mailhog',
    'version': '0.1.0',
    'description': 'A python client for the Mailhog API',
    'long_description': "# mailhog-python\n\nA python client for the [Mailhog](https://github.com/mailhog/MailHog) API\n\n\n## Installation\n\nInstall from PyPI \n\n```\npip install mailhog\n```\n\n## Get Started\n\n```python\nfrom mailhog import Mailhog\n\nmailhog = Mailhog() # Defaults to http://localhost:8025\n\n# Get all messages\nmailhog.messages()\n\n# Get all messages with start and limit parameters\nmailhog.messages(start=0, limit=10)\n\n# Search for messages\nmailhog.search('Text contained in the message')\n\n# Search for messages by recipient\nmailhog.search('test@test.com', 'To')\n\n# Search for messages by sender\nmailhog.search('test@test.com', 'From')\n\n# Delete all messages\nmailhog.delete_all()\n```\n\n# API\n##  mailhog.Mailhog\n> Mailhog API client\n#### Parameters\n\n* `host` - The host of the Mailhog API, defaults to `localhost`\n* `port` - The port of the Mailhog API, defaults to `8025`\n\n### Methods\n### `messages(start=0, limit=10)`\n> Get all messages\n\n#### Parameters\n* `start` - The start index of the messages to return, defaults to `0`\n* `limit` - The number of messages to return, defaults to `10`\n\n#### Returns\n* `list` - A list of `mailhog.Message` objects\n\n#### Example\n```python\nfrom mailhog import Mailhog\n\nmailhog = Mailhog()\n\nmessages = mailhog.messages()\n```\n\n### `search(query, kind='containing', start=0, limit=10)`\n> Search for messages\n\n#### Parameters\n* `query` - The query to search for\n* `kind` - The kind of search to perform, defaults to `containing`\n* `start` - The start index of the messages to return, defaults to `0`\n* `limit` - The number of messages to return, defaults to `10`\n\n#### Returns\n* `list` - A list of `mailhog.Message` objects\n\n#### Example\n```python\nfrom mailhog import Mailhog\n\nmailhog = Mailhog()\n\nmessages = mailhog.search('Some Text')\n```\n\n### `delete_all()`\n> Delete all messages\n\n#### Example\n```python\nfrom mailhog import Mailhog\n\nmailhog = Mailhog()\n\nmailhog.delete_all()\n```\n\n# Datatypes\n##  mailhog.Messages\n> A list of `mailhog.Message` objects\n#### Attributes\n* `total` - The total number of messages\n* `start` - The start index of the messages\n* `count` - The total number of received messages\n* `items` - A list of `mailhog.Message` objects\n\n##  mailhog.Message\n> A message from Mailhog\n#### Attributes\n* `id` - The ID of the message\n* `from_` - A mailhog.Path object containing the sender\n* `to` - A List of mailhog.Path objects containing the recipients\n* `created` - The date the message was created\n* `content` - A mailhog.Content object containing the content of the message\n* `raw`: - The raw message\n* `mime` - A mailhog.MIME object containing the MIME data of the message\n\n#### Methods\n### `get_sender()`\n> Get the sender of the message\n\n#### Returns\n* `str` - The sender of the message\n\n### `get_recipients()`\n> Get the recipients of the message\n\n#### Returns\n* `list` - A list of recipients\n\n### `get_subject()`\n> Get the subject of the message\n\n#### Returns\n* `str` - The subject of the message\n\n##  mailhog.Path\n> A path object\n#### Attributes\n* `relays` - A list of relays\n* `mailbox` - The mailbox\n* `domain` - The domain\n* `params` - The parameters\n\n##  mailhog.Content\n> The content of a message\n#### Attributes\n* `headers` - A Dict of headers of the message\n* `body` - The body of the message\n* `size` - The size of the message\n* `mime` - The MIME type of the message\n\n\n##  mailhog.MIMEBody\n> The body of a MIME message\n#### Attributes\n* `parts` - A list of mailhog.MIMEContent objects\n\n\n##  mailhog.MIMEContent\n> The content of a MIME message\n#### Attributes\n* `headers` - A Dict of headers of the message\n* `body` - The body of the message\n* `size` - The size of the message\n* `mime` - The MIME type of the message\n\n___\n\n## About the Package\n\n### WIP\n\nThis package is still a work in progress. If you find any bugs or have any suggestions, please open an issue on the [GitHub repository](https://github.com/nklsw/mailhog-python)\n\n### Roadmap\n\n- [x] Mailhog API v2 Messages Endpoint\n- [x] Mailhog API v2 Search Endpoint\n- [ ] Mailhog API v2 Jim Endpoint\n- [x] Mailhog API v1 Delete Messages Endpoint\n- [ ] Mailhog API v1 Delete Message Endpoint\n\n\n### Local Development\n\nTo install the package locally, run the following commands:\n\n```\ngit clone\ncd mailhog-python\n\npoetry install\n```\n\nTo run a mailhog instance locally, run the following command:\n\n```\ndocker-compose up -d\n```\n\n\n\nTo run the tests, run the following command:\n\n```\npoetry run pytest\n```\n",
    'author': 'nklsw',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nklsw/mailhog-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
