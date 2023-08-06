# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['from_root']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'from-root',
    'version': '1.3.0',
    'description': 'Forget about working directory errors',
    'long_description': '# Usage guide\n\nAre you fed up with that **annoying FileNotFoundError** when your working directory turns out to be something different\nfrom what you expected? Or, maybe, you are looking for an easy and robust way of declaring paths to configs and any data\nfiles in your project? Yeah, that drives us all crazy.\n\nThe package is really tiny, there are two function:\n\n* `from_root` helps with declaring absolute paths relative to your project root\n* `from_here` comes in handy when you want to declare a path relative to the current file\n\nThey are dead simple to use.\n\nLet\'s assume we have a project with the next structure:\n\n```\n├── .git  # OPTIONAL. See explanation below\n├── .project-root  # OPTIONAL. See explanation below\n├── config.json  \n├── assets  \n│ ├── animation.gif  \n│ └── logo.png  \n└── package  \n    ├── __init__.py\n    ├── data.csv    \n    ├── script.py\n    ├── FROM_HERE_DEMO.py\n    └── inner_package  \n      ├── FROM_ROOT_DEMO.py  \n      ├── __init__.py\n      └── insanely\n          └── deep\n              └── dir\n                  └── file.txt\n```\n\n#### `from_root` examples:\n\n```python\n# <PROJECT_ROOT>/package/inner_package/FROM_ROOT_DEMO.py\nfrom from_root import from_root\n\nCONFIG_PATH = from_root(\'config.json\')\n\nPACKAGE_DATA_PATH = from_root(\'package\', \'data.csv\')\n\n# `from_root` returns pathlib.Path object\n# so we can take advantage of its fantastic "/" syntax\nASSETS_DIR = from_root(\'assets\')\nANIMATION_PATH = ASSETS_DIR / \'animation.gif\'\nLOGO_PATH = ASSETS_DIR / \'logo.png\'\n\n# no matter how deep it\'s located\nFILE_TXT_PATH = from_root(\'package\', \'inner_package\', \'insanely\', \'deep\', \'dir\', \'file.txt\')\n\n# If `mkdirs` is set to True (False by default), all *args will be treated as dir names \n# and created for you. \n# If a directory already exists, nothing happens.\n\nimport pickle\n\nRESULTS_DIR = from_root(\'package\', \'deep\', \'results\', \'dir\', mkdirs=True)\nresults = {\n    \'ones\': [1, 1, 1],\n    \'zeros\': [2, 2, 2]\n}\nfor name, data in results.items():\n    path = RESULTS_DIR / f\'{name}.pkl\'\n    # `FileNotFoundError` is not raised because `from_root` has created all non-existing directories\n    with path.open(\'wb\') as file:\n        pickle.dump(data, file)\n\n# WARNING: don\'t do this, you\'ll end up with data.json directory:\nwith from_root(\'results\', \'data.json\', mkdirs=True).open(\'w\') as file:\n    ...\n\n# Do this instead:\nwith (from_root(\'results\', mkdirs=True) / \'data.json\').open(\'w\') as file:\n    ...\n```\n\n#### `from_here` examples:\n\n```python\n# <PROJECT_ROOT>/package/FROM_HERE_DEMO.py\nfrom from_root import from_here\n\n# The only difference from `from_root` is that `from_here` allows you to declare relative paths\n# I think the examples speak for themselves quite good. \n# Take a look at tree above and compare with `from_root` examples\n\nCONFIG_PATH = from_here(\'data.csv\')\nFILE_TXT_PATH = from_here(\'inner_package\', \'insanely\', \'deep\', \'dir\', \'file.txt\')\n```\n\n# How does it work?\n\nWhen `from_root` is called, folders in the current traceback are looked through one by one in order to find `.git`\ndirectory or `.project-root` file (might be empty; you have to create it on your own). The first one that contains at\nleast one of them are considered as a root directory.\n',
    'author': 'Eduard Kononov',
    'author_email': 'aduard.kononov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
