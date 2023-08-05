# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_msgspec_json']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<4.0', 'djangorestframework>=3.14.0,<4.0.0']

setup_kwargs = {
    'name': 'drf-msgspec-json-renderer',
    'version': '0.1.3',
    'description': '',
    'long_description': "Django Rest Framework msgspec Renderer\n==================\n\n\nDjango Rest Framework renderer using [msgspec](https://github.com/jcrist/msgspec)\n\n## Installation\n\n`pip install drf-msgspec-json-renderer`\n\nYou can then set the `MsgspecJSONRenderer` class as your default renderer in your `settings.py`\n\n```python\nREST_FRAMEWORK = {\n    'DEFAULT_RENDERER_CLASSES': (\n        'drf_msgspec_json.renderers.MsgspecJSONRenderer',\n    ),\n    ...\n}\n```\n\nAlso you can set the `MsgspecJSONParser` class as your default parser in your `settings.py`\n\n```python\nREST_FRAMEWORK = {\n    'DEFAULT_PARSER_CLASSES': (\n        'drf_msgspec_json.parsers.MsgspecJSONParser',\n    ),\n    ...\n}\n```\n",
    'author': 'Novitskii Aleksei',
    'author_email': 'mr.alexeynov95@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
