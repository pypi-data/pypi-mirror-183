# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['exenenv']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'exenenv',
    'version': '1.2',
    'description': 'Environment variables verifier and type converter.',
    'long_description': '# ExenENV\nEnvironment variables verifier and type converter.\n\n## Installation\nLibrary is available for installation from PyPI\n```shell\n$ pip install exenenv\n```\n\n## Basic Usage\n```python\nimport os\nfrom exenenv import EnvironmentProfile\n\nos.environ["REQUIRED_VARIABLE"] = "20"  # assume it\'s set to this\n\n\nclass Environment(EnvironmentProfile):\n    REQUIRED_VARIABLE: int\n    DEFAULT_VALUE_VARIABLE: float = 30.0\n\n\nenv = Environment()\nenv.load()\n\nprint(f"{env.REQUIRED_VARIABLE=}\\n{env.DEFAULT_VALUE_VARIABLE=}")\n```\n```\nenv.REQUIRED_VARIABLE=20\nenv.DEFAULT_VALUE_VARIABLE=30.0\n```\n\n## Using EnvVars\n\n```python\nimport os\nfrom exenenv import EnvironmentProfile, EnvVar\n\nos.environ.update({\n    "REQUIRED_VAR": "10",\n    "ALT_NAME_VAR": "40",\n    "CONVERTER_VAR": "gamer,coder,python"\n})  # assume our environment is this\n\n\nclass Environment(EnvironmentProfile):\n    REQUIRED_VAR: int\n    DEFAULT_VALUE_VAR: str = EnvVar(default=20)\n    OTHER_VAR: int = EnvVar(env_name="ALT_NAME_VAR")\n    CONVERTER_VAR: list[str] = EnvVar(converter=lambda x: x.split(","))\n\n\nenv = Environment()\nenv.load()\n\nprint(f"""\\\n{env.REQUIRED_VAR=}\n{env.DEFAULT_VALUE_VAR=}\n{env.OTHER_VAR=}\n{env.CONVERTER_VAR=}\n""")\n```\n```\nenv.REQUIRED_VAR=10\nenv.DEFAULT_VALUE_VAR=20\nenv.OTHER_VAR=40\nenv.CONVERTER_VAR=[\'gamer\', \'coder\', \'python\']\n```\n\n## Union Typehints\nSince `v1.2`, library supports converting to **one of provided types**.\n```python\nimport os\nfrom exenenv import EnvironmentProfile\n\nos.environ.update({\n    "UNION_VAR": "union"\n})\n\n\nclass Environment(EnvironmentProfile):\n    UNION_VAR: int | str\n    OPTIONAL_VAR: float | None = None\n\n\nenv = Environment()\nenv.load()\n\nprint(f"{env.UNION_VAR=}\\n{env.OPTIONAL_VAR=}")\n```\n```\nenv.UNION_VAR=\'union\'\nenv.OPTIONAL_VAR=None\n```\nIn this case, converting to `UNION_VAR` to `int`, so library used next provided type. Default value for `OPTIONAL_VAR` still has to be declared explicitly.\n',
    'author': 'Exenifix',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Exenifix/ExenENV',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
