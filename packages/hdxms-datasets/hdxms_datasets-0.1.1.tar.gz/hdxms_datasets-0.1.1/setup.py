# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hdxms_datasets']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'omegaconf>=2.3.0,<3.0.0',
 'packaging>=22.0,<23.0',
 'pandas>=1.5.2,<2.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'hdxms-datasets',
    'version': '0.1.1',
    'description': 'Download and parse curated HDX-MS datasets',
    'long_description': '# HDXMS Datasets\n\n\n* Free software: MIT license\n\n### Installation\n\n```bash\n$ pip install hdxms-datasets\n```\n\n### Example code\n\n\n```python\nfrom hdxms_datasets import DataVault\n\nvault = DataVault()\n\n# Download a specific HDX dataset\nvault.fetch_dataset("20221007_1530_SecA_Krishnamurthy")\n\n# Load the dataset\nds = vault.load_dataset("20221007_1530_SecA_Krishnamurthy")\n\n# Load the FD control of the first \'state\' in the dataset.\nfd_control = ds.load_peptides(0, "FD_control")\n\n# Load the corresponding experimental peptides.\npeptides = ds.load_peptides(0, "experiment")\n\n```\n\n',
    'author': 'Jochem Smit',
    'author_email': 'jhsmit@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
