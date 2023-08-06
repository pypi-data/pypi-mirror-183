# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dino_seedwork_be',
 'dino_seedwork_be.adapters',
 'dino_seedwork_be.adapters.messaging',
 'dino_seedwork_be.adapters.messaging.firebase',
 'dino_seedwork_be.adapters.messaging.rabbitmq',
 'dino_seedwork_be.adapters.pubsub',
 'dino_seedwork_be.adapters.rest',
 'dino_seedwork_be.adapters.rest.fastapi',
 'dino_seedwork_be.application',
 'dino_seedwork_be.domain',
 'dino_seedwork_be.event',
 'dino_seedwork_be.event.persistance',
 'dino_seedwork_be.fp',
 'dino_seedwork_be.logic',
 'dino_seedwork_be.media',
 'dino_seedwork_be.process',
 'dino_seedwork_be.pubsub',
 'dino_seedwork_be.serializer',
 'dino_seedwork_be.storage',
 'dino_seedwork_be.storage.alchemysql',
 'dino_seedwork_be.types',
 'dino_seedwork_be.utils',
 'dino_seedwork_be.utils.persistance',
 'dino_seedwork_be.utils.process']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=14.1.0,<15.0.0',
 'Pillow>=9.2.0,<10.0.0',
 'PyJWT[crypto]>=2.4.0,<3.0.0',
 'SQLAlchemy[asyncio]>=1.4.37,<2.0.0',
 'asyncpg>=0.25.0,<0.26.0',
 'fastapi==0.85.0',
 'firebase-admin>=6.0.1,<7.0.0',
 'google-cloud-storage>=2.4.0,<3.0.0',
 'greenlet>=1.1.2,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'importlib-resources>=5.7.1,<6.0.0',
 'jsonpickle>=2.2.0,<3.0.0',
 'multimethod>=1.9,<2.0',
 'multipledispatch>=0.6.0,<0.7.0',
 'pika>=1.3.1,<2.0.0',
 'pre-commit>=2.20.0,<3.0.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pyramda>=0.1,<0.2',
 'pytest-asyncio>=0.18.3,<0.19.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'python-multipart>=0.0.5,<0.0.6',
 'pytz>=2022.1,<2023.0',
 'respx>=0.19.2,<0.20.0',
 'returns>=0.19.0,<0.20.0',
 'sqlalchemy-utils>=0.38.3,<0.39.0',
 'toolz>=0.11.2,<0.12.0',
 'uvicorn[standard]>=0.17.6,<0.18.0',
 'validators>=0.19.0,<0.20.0']

setup_kwargs = {
    'name': 'dinohub-seedwork-be',
    'version': '0.1.9',
    'description': 'A seedwork for DinoHub service',
    'long_description': '# DINO hub seedwork\n\nThis is a package contains\n  * DDD (Domain Driven Design) artifact\n  * Functional programming with Returns\n  * Basic helpers function\n',
    'author': 'Tuan Cau Rao',
    'author_email': 'tuan.pt@orai.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
