# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eks_pv_encrypter']

package_data = \
{'': ['*']}

install_requires = \
['black[jupyter]>=22.12.0,<23.0.0',
 'boto3>=1.26.41,<2.0.0',
 'fire>=0.5.0,<0.6.0',
 'ipykernel>=6.19.4,<7.0.0',
 'kubernetes>=25.3.0,<26.0.0',
 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['pv-encrypter = eks_pv_encrypter.cli:main']}

setup_kwargs = {
    'name': 'eks-pv-encrypter',
    'version': '0.1.0',
    'description': 'A simple tool to encrypt the EBS volumes linked to your EKS Persistent Volumes.',
    'long_description': "# EKS Persistent Volume Encrypter\n\n##  What is it?\n\nA tool to detect Persistent Volumes (PVs) in your EKS cluster that are backed by\nunencrypted EBS Volumes and encrypt them.\n\n## Do I need it?\n\nIf you:\n\n➡️ Have an EKS Cluster.  \n➡️ Use Persistent Volumes backed by EBS Volumes.  \n➡️ Want to make sure all the EBS Volumes you use are encrypted.  \n➡️ Don't want to do it one-by-one.  \n\nThen this tool will help you speed up this process.\n\n## What does it contain?\n\n* A Jupyter Notebook which is the main interface.\n* A simple CLI that displays relevant information about your cluster.\n\nThe CLI will be limited to read-only actions. The Notebook is the only way to execute\nconstructive/destructive actions.\n\n## Installation\n\n`pip install .`\n\n## Usage\n\n1. Use the `pv_encrypter.ipynb` Notebook.\n2. If you want a read-only overview of your Cluster. Just run `pv-encrypter status`. \n\n## Overview of the Process\n\n![Overview](ebs-pv-encrypter.jpg)\n",
    'author': 'Vishnu Deva',
    'author_email': 'vishnu.d@madstreetden.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
