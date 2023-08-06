# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlite_users', 'starlite_users.adapter.sqlalchemy']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=38.0.4,<39.0.0',
 'passlib',
 'python-jose>=3.3.0,<4.0.0',
 'sqlalchemy>=1.4.44,<2.0.0',
 'starlite>=1.43.1,<2.0.0']

setup_kwargs = {
    'name': 'starlite-users',
    'version': '0.1.0',
    'description': 'Authentication and user management for Starlite',
    'long_description': '# starlite-users\nAuthentication, authorization and user management for the Starlite framework\n\n_This package is not yet production ready._\n---\n## Features\n* Supports Starlite Session, JWT and JWTCookie auth backends\n* SQLAlchemy ORM models (Piccolo and Tortoise on roadmap)\n* Pre-configured route handlers for:\n  * Authentication\n  * Registration\n  * Verification\n  * Password reset\n  * Administrative user management\n  * Administrative role management\n  * Assign/revoke roles to/from users\n* Authorization via role based guards\n* Define your own administrative roles for user management\n\n## Getting started\nThe package is not yet availabe on PyPi. Right now you can:\n1. Clone this repository\n2. `cd starlite-users && poetry install`\n3. `poetry run PYTHONPATH=. python examples/main.py`\n\nThis will start a `uvicorn` server running on `127.0.0.1:8000`\nVisit `127.0.0.1:8000/schema/swagger` for interactive docs\n',
    'author': 'Michael Bosch',
    'author_email': 'michael@lonelyviking.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
