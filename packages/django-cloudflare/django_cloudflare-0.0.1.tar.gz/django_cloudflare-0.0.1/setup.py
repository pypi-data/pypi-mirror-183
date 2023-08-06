# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_cloudflare']

package_data = \
{'': ['*']}

install_requires = \
['django>=4.1.5,<5.0.0']

setup_kwargs = {
    'name': 'django-cloudflare',
    'version': '0.0.1',
    'description': 'A middleware for Django applications using Cloudflare as a proxy. Allows you to extract and access CF headers.',
    'long_description': '.. image:: https://github.com/tomwojcik/django-cloudflare/workflows/Tests/badge.svg\n    :target: https://github.com/tomwojcik/django-cloudflare/actions?query=branch%3Amain+workflow%Tests++\n    :alt: Build Status\n\n.. image:: https://img.shields.io/pypi/pyversions/django-cloudflare.svg\n    :target: https://pypi.org/project/django-cloudflare/\n    :alt: Python Versions\n\n.. image:: https://img.shields.io/pypi/v/django-cloudflare.svg\n    :target: https://pypi.org/project/django-cloudflare/\n    :alt: Latest Version\n\n.. image:: https://readthedocs.org/projects/django-cloudflare/badge/?version=latest\n    :target: https://readthedocs.org/projects/django-cloudflare/\n    :alt: Docs\n\n.. image:: https://codecov.io/gh/tomwojcik/django-cloudflare/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/tomwojcik/django-cloudflare\n    :alt: codecov\n\n\n=================\ndjango-cloudflare\n=================\n\nA reusable Django middleware that allows you to easily extract Cloudflare headers.\n\nResources:\n\n* **Source**: https://github.com/tomwojcik/django-cloudflare\n* **Documentation**: https://django-cloudflare.readthedocs.io/\n* **Changelog**: https://django-cloudflare.readthedocs.io/en/latest/changelog.html\n\n------------\nInstallation\n------------\n\n``$ pip install -U django-cloudflare``\n\n\n------------\nRequirements\n------------\n\nPython 3.7+\n\n------------\nDependencies\n------------\n\ndjango>=3.2\n',
    'author': 'Tom Wojcik',
    'author_email': 'django-cloudflare-pkg@tomwojcik.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tomwojcik/django-cloudflare',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
