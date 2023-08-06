# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dynamodb_garbage_collector']
install_requires = \
['boto3>=1.26.41,<2.0.0', 'botocore>=1.29.41,<2.0.0']

setup_kwargs = {
    'name': 'dynamodb-garbage-collector',
    'version': '1.1.0',
    'description': 'Remove garbage items from DynamoDB tables',
    'long_description': "# DynamoDB Garbage Collector\n\n[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://shields.io/)\n\nThe DynamoDB Garbage Collector is a Python library that allows you to delete garbage items in DynamoDB tables.\n\n## Table of Contents\n\n- [Installation](#installation)\n- [Usage](#usage)\n- [Contributing](#contributing)\n- [License](#license)\n\n## Installation\n\nTo install the DynamoDB Garbage Collector, use `pip`:\n\n```bash\n$ pip install dynamodb-garbage-collector\n```\n\n## Usage\n\nThe DynamoDB Garbage Collector currently provides a single function called `purge_orphan_items`, which allows you to delete orphan items in a child table that reference a non-existent item in a parent table. If optional timestamp attributes are provided only will be delete orphan items earlier than a specified maximum time (by default, one hour ago).\n\nTo use `purge_orphan_items`, you need to provide the following parameters:\n\n- `logger`: a logger object to log messages during the execution of the function.\n- `region`: the AWS region where the parent and child tables are located.\n- `parent_table`: the name of the parent table.\n- `child_table`: the name of the child table.\n- `key_attribute`: the name of the key attribute for both tables.\n- `child_reference_attribute`: the name of the reference attribute in the child table.\n- `max_workers` (optional): the maximum number of workers to use for concurrent operations. If not provided, a default value of 100 will be used.\n- `timestamp_attribute` (optional): the name of the attribute that contains the timestamp of the records in the child table. If not provided, timestamp will not be taken into account when deleting items.\n- `timestamp_format` (optional): the format of the timestamp attribute. If not provided, timestamp will not be taken into account when deleting items.\n\nHere is an example of how to use the `purge_orphan_items` function:\n\n```python\nimport logging\nfrom dynamodb_garbage_collector import purge_orphan_items\n\n# Set up the logger\nlogging.basicConfig()\nlogger = logging.getLogger()\nlogger.setLevel(logging.INFO)\n\n# Set the AWS region where the parent and child tables are located\nregion = 'eu-west-1'\n\n# Set the names of the parent and child tables, and the key and reference attributes\nparent_table = 'ParentTable'\nchild_table = 'ChildTable'\nkey_attribute = 'id'\nchild_reference_attribute = 'parentId'\n\n# Set the maximum number of workers\nmax_workers = 50\n\n# Set the name of the timestamp attribute and the timestamp format\ntimestamp_attribute = 'createdAt'\ntimestamp_format = '%Y-%m-%dT%H:%M:%S.%fZ'\n\n# Call the function\npurge_orphan_items(logger, region, parent_table, child_table, key_attribute, child_reference_attribute, max_workers, timestamp_attribute, timestamp_format)\n```\n\n## Contributing\n\nWe welcome contributions to the DynamoDB Garbage Collector. To contribute, please fork the repository and create a pull request with your changes.\n\n## License\n\nThe DynamoDB Garbage Collector is released under the MIT License.",
    'author': 'Marçal Pla',
    'author_email': 'marcal.pla@shimoku.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
