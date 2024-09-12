# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bootstrap4', 'bootstrap4.templatetags']

package_data = \
{'': ['*'],
 'bootstrap4': ['templates/bootstrap4/*', 'templates/bootstrap4/widgets/*']}

install_requires = \
['beautifulsoup4>=4.10.0,<5.0.0', 'django>=4.2,<5.0']

setup_kwargs = {
    'name': 'django-bootstrap4',
    'version': '24.3',
    'description': 'Bootstrap 4 for Django',
    'long_description': '# django-bootstrap 4\n\n[![CI](https://github.com/zostera/django-bootstrap4/workflows/CI/badge.svg?branch=main)](https://github.com/zostera/django-bootstrap4/actions?workflow=CI)\n[![Coverage Status](https://coveralls.io/repos/github/zostera/django-bootstrap4/badge.svg?branch=main)](https://coveralls.io/github/zostera/django-bootstrap4?branch=main)\n[![Latest PyPI version](https://img.shields.io/pypi/v/django-bootstrap4.svg)](https://pypi.python.org/pypi/django-bootstrap4)\n\nBootstrap 4 for Django.\n\n## Goal\n\nThe goal of this project is to seamlessly blend Django and Bootstrap 4.\n\n## Requirements\n\nThis package requires a combination of Python and Django that is currently supported.\n\nSee "Supported Versions" on https://www.djangoproject.com/download/.\n\n## Documentation\n\nThe full documentation is at https://django-bootstrap4.readthedocs.io/\n\n## Installation\n\n1. Install using pip:\n\n```bash\npip install django-bootstrap4\n```\n\n   Alternatively, you can install download or clone this repo and call ``pip install -e .``.\n\n2. Add to `INSTALLED_APPS` in your `settings.py`:\n\n```python\nINSTALLED_APPS = (\n  # ...\n  "bootstrap4",\n  # ...\n)\n```\n\n3. In your templates, load the `bootstrap4` library and use the `bootstrap_*` tags. See example below.\n\n## Example template\n\n```jinja\n{% load bootstrap4 %}\n\n{# Display a form #}\n\n<form action="/url/to/submit/" method="post" class="form">\n    {% csrf_token %}\n    {% bootstrap_form form %}\n    {% buttons %}\n        <button type="submit" class="btn btn-primary">Submit</button>\n    {% endbuttons %}\n</form>\n```\n\n## Example\n\nAn example application app is provided in `example`. You can run it with `make example`.\n\n## Bugs and suggestions\n\nIf you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.\n\nhttps://github.com/zostera/django-bootstrap4/issues\n\n## License\n\nYou can use this under BSD-3-Clause. See [LICENSE](LICENSE) file for details.\n\n## Author\n\nDeveloped and maintained by [Zostera](https://zostera.nl).\n\nOriginal author: [Dylan Verheul](https://github.com/dyve).\n\nThanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.\n\nPlease see [AUTHORS](AUTHORS) for a list of contributors.\n',
    'author': 'Dylan Verheul',
    'author_email': 'dylan@dyve.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
