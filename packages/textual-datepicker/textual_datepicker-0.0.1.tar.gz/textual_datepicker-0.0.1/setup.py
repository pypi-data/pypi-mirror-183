# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textual_datepicker']

package_data = \
{'': ['*']}

install_requires = \
['pendulum', 'textual>=0.6.0']

setup_kwargs = {
    'name': 'textual-datepicker',
    'version': '0.0.1',
    'description': 'A datepicker widget for Textual.',
    'long_description': '# Textual: DatePicker\n\nA DatePicker widget for [textual](https://github.com/Textualize/textual). It can be used standalone or with a DateSelect opening the dialog.\n\n**NOTE:** This package is in a concept phase. A working version (>= 0.1.0) will\nbe release in January 2023. I\'m currently preparing it for publishing on PyPI and\nhappy to receive feedback.\n\n## Usage\n\n```python\nfrom textual_datepicker import DateSelect\n\nDateSelect(\n  placeholder="please select",\n  format="YYYY-MM-DD",\n  picker_mount="#main_container"\n)\n```\n\n## Installation\n\n```bash\npip install textual-datepicker\n```\n\nRequires textual 0.6.0 or later.\n\n## Limitations\n\nThis textual widget is in early stage and has some limitations:\n\n* The default given date will probably not working at this time. Planned for 0.1.0.\n* It can only open below, not above: Make sure to reserve space below for the dialog.\n* It needs a specific mount point (`picker_mount`) where the dialog\n  shall appear. This is needed because the container widget with the select\n  itself could be too small. Maybe in future versions this will no longer\n  needed.\n',
    'author': 'Mischa Schindowski',
    'author_email': 'mschindowski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mitosch/textual-datepicker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
