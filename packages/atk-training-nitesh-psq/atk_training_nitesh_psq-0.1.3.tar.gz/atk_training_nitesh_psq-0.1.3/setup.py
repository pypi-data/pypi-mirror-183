# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atk_training_nitesh_psq',
 'atk_training_nitesh_psq.consumer',
 'atk_training_nitesh_psq.manager',
 'atk_training_nitesh_psq.producer',
 'atk_training_nitesh_psq.sqlite_']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'db-sqlite3>=0.0.1,<0.0.2',
 'schedule>=1.1.0,<2.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['atk-nitesh-consumer = '
                     'atk_training_nitesh_psq.consumer:main',
                     'atk-nitesh-manager = '
                     'atk_training_nitesh_psq.manager:main',
                     'atk-nitesh-producer = '
                     'atk_training_nitesh_psq.producer:main',
                     'atk-nitesh-queue = '
                     'atk_training_nitesh_psq.sqlite_:init_']}

setup_kwargs = {
    'name': 'atk-training-nitesh-psq',
    'version': '0.1.3',
    'description': '',
    'long_description': '# a Very simple Persistant queue service using sqlite3\n\nHow to intialize the queue using  the package (to instialize the db)\n```\npip install atk_training_nitesh_psq\nfrom atk_training_nitesh_psq.sqlite_ import SQLITE\nqueue=SQLITE(\'db_name\')\n\n# if someone is directly jumping to producer queue is automaticallt initialized\n```\nHow to run intialize the queue using command\n```\nqueue --db-name db_name\n```\n\nHow to initialize the producer using the package\n```\n---> Given one has installed the package\nfrom atk_training_nitesh_psq.producer import producer_\nproducer_("queue.db")\n```\nHow to initialize the producer using the command\n```\nproducer "queue.db"\n```\n\nHow to initialize the consumer using the package\n```\nfrom atk_training_nitesh_psq.consumer import cons\n\ncons(\'queue.db\')\n```\nHow to initailize the consumer using the command\n```\nconsumer "queue.db" or empty\n(automatically initializes to queue.db)\n```\n\n```\nNeed to implement a manager schuduled to push pending tasks to queue back to procesing and a ops manager\n```\n',
    'author': 'Nitesh',
    'author_email': 'nitesh@aganitha.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
