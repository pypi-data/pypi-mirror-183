# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xbool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xbool',
    'version': '1.0.0',
    'description': 'General purpose bool/boolean utilities, extracting bools from strings.',
    'long_description': '![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8|%203.9|%203.10|%203.11&color=blue?style=flat-square&logo=python)\n![PyPI version](https://badge.fury.io/py/xbool.svg?)\n\n- [Introduction](#introduction)\n- [Documentation](#documentation)\n- [Install](#install)\n- [Quick Start](#quick-start)\n    * [bool_value](#bool_value)\n    * [bool_env](#bool_env)\n- [Licensing](#licensing)\n\n# Introduction\n\nGeneral purpose bool/boolean utilities, extracting bools from strings.\n\nOnly two so far:\n\n- `bool_value`, see **[bool_value docs](https://xyngular.github.io/py-xbool/latest/)**.\n- `bool_env`, see **[bool_env docs](https://xyngular.github.io/py-xbool/latest/)**.\n\n# Documentation\n\n**[📄 Detailed Documentation](https://xyngular.github.io/py-xbool/latest/)** | **[🐍 PyPi](https://pypi.org/project/xbool/)**\n\n# Install\n\n```bash\n# via pip\npip install xbool\n\n# via poetry\npoetry add xbool\n```\n\n# Quick Start\n\n## bool_value\n\nGenerally converts objects to bool-values, special-casing strings\nto use the built-in `distutils.util.strtobool` function to convert the string value\nto a bool.\n\n```python\nfrom xbool import bool_value\n\n# Convert string to bool\nassert bool_value(\'true\') is True\nassert bool_value(\'false\') is False\n\nassert bool_value(\'y\') is True\nassert bool_value(\'n\') is False\n\nassert bool_value(\'on\') is True\nassert bool_value(\'off\') is False\n\nassert bool_value(\'t\') is True\nassert bool_value(\'f\') is False\n\nassert bool_value(\'yes\') is True\nassert bool_value(\'no\') is False\n\nassert bool_value(\'1\') is True\nassert bool_value(\'0\') is False\n\n# Any other string is generally considered False:\nassert bool_value("some-other-string") is False\n\n# Convert bools to bools:\nassert bool_value(True) is True\nassert bool_value(False) is False\n\n# Generally, for non-strings, True-like objects return True:\nsome_object = object()\nassert bool_value(some_object) is True\n\n# And False-like objects return False:\nassert bool_value(None) is False\n```\n\n## bool_env\n\nLooks up environmental variable with passed in name.\n\nRuns the env-var value though `bool_value` for you and returns the result.\n\nUseful to easily get a bool-value from an environmental variable.\n\n```python\nfrom xbool import bool_env\nimport os\n\nos.environ[\'SOME_ENV_VAR\'] = "False"\nassert bool_env(\'SOME_ENV_VAR\') is False\n\n\nos.environ[\'SOME_OTHER_ENV_VAR\'] = "True"\nassert bool_env(\'SOME_OTHER_ENV_VAR\') is True\n```\n\n\n# Licensing\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.\n',
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-xbool',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
