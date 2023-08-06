# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rdflib_store_trigdump']

package_data = \
{'': ['*']}

install_requires = \
['rdflib>=6.2.0,<7.0.0']

entry_points = \
{'rdf.plugins.store': ['TriGDump = rdflib_store_trigdump:TriGDumpStore']}

setup_kwargs = {
    'name': 'rdflib-store-trigdump',
    'version': '1.0.0',
    'description': 'RDFLib store that reads and dumps TriG data on open and close',
    'long_description': '# rdflib-store-trigdump\n\nThis is a thin wrapper around [RDFLib](https://github.com/RDFLib/rdflib)\'s\n[Memory store](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.plugins.stores.html#rdflib.plugins.stores.memory.Memory)\nadding (unsafe) persistence:\n\n * When opening the store, data is read from a TriG file\n * When closing the store, data is serialized to the TriG file\n\n## Usage\n\n```python\nfrom rdflib import Graph\n\ngraph = Graph("TriGDump")\ngraph.open("/path/to/my/file.trig", create=True)\n\n# do something\n\ngraph.close()\n```\n',
    'author': 'Dominik George',
    'author_email': 'nik@naturalnet.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/Denkar.io/rdflib-store-trigdump',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
