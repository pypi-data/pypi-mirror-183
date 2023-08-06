# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minuteinbox']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'minuteinbox',
    'version': '0.3.0',
    'description': 'Unofficial python wrapper for minuteinbox.com',
    'long_description': ' # minuteinbox\n\n[![Version](https://img.shields.io/pypi/v/minuteinbox?logo=pypi)](https://pypi.org/project/minuteinbox)\n[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_minuteinbox?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_minuteinbox)\n[![CodeCoverage](https://img.shields.io/sonar/coverage/fedecalendino_minuteinbox?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_minuteinbox)\n\nUnofficial python wrapper for minuteinbox.com\n\n\n### usage\n\n```python\nfrom minuteinbox import Inbox\n\n# use without parameters to create a new inbox\n# inbox = Inbox()\n\n# use with address and token to reuse an existing inbox\ninbox = Inbox(\n    address="maximo.kayo@moontrack.net",\n    token="86d6b9308a1a482ba348533a457146c4",\n)\n\naddress = inbox.address\ntoken = inbox.token\n\nprint(address, "(", token, ")")\nprint()\n\n# extend the expiration of the inbox by 10 minutes\ninbox.extend_10m()\n\nprint("Expires in:", inbox.expires_in, "seconds")\nprint()\n\n# fetch all emails in the inbox\nfor mail in inbox.mails:\n    print("FROM:", mail.sender.name, mail.sender.address)\n    print("SUBJECT:", mail.subject)\n    print("SENT AT:", mail.sent_at)\n    print("IS NEW:", mail.is_new)\n\n    print("CONTENT")\n    print(mail.content)\n```',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedecalendino/minuteinbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
