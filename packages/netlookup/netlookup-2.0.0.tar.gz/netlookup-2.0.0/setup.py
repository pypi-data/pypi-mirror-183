# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netlookup',
 'netlookup.bin',
 'netlookup.bin.commands',
 'netlookup.network_sets']

package_data = \
{'': ['*']}

install_requires = \
['cli-toolkit>=2,<3', 'dnspython>=2,<3', 'netaddr>=0.8,<0.9', 'requests>=2,<3']

entry_points = \
{'console_scripts': ['netlookup = netlookup.bin.netlookup:main']}

setup_kwargs = {
    'name': 'netlookup',
    'version': '2.0.0',
    'description': 'Python tools to look up information about networks',
    'long_description': "![Unit Tests](https://github.com/hile/netlookup/actions/workflows/unittest.yml/badge.svg)\n![Style Checks](https://github.com/hile/netlookup/actions/workflows/lint.yml/badge.svg)\n\n# Command line network lookups and operations\n\nThis python tool implements pretty much same things as `netcalc` and `netblocks` libraries, but\nwith minor differences in the way things are done.\n\nThe library is intended to be usable both as a command line tool `netlookup` and as a library from\nserver code. Personally I use it for splitting IP ranges to subnets.\n\n## Installing\n\n```bash\npip install netlookup\n```\n\n# Command line tool `netlookup` basic usage\n\nFollowing examples illustrate Usage of netlookup tool.\n\nLookup details for IPv4 host with CIDR mask and IPv6 subnet:\n\n```bash\nnetlookup info 172.31.1.19/17 2c0f:fb50:4000::/56\n             CIDR 172.31.0.0/17\n          Netmask 255.255.128.0\n          Network 172.31.0.0\n        Broadcast 172.31.127.255\n       First host 172.31.0.1\n        Last host 172.31.127.254\n      Total hosts 32766\n             Next 172.31.128.0/17\n         Previous 172.30.128.0/17\n             Bits 10101100.00011111.00000000.00000000\n      Reverse DNS 0.0.31.172.in-addr.arpa.\n             CIDR 2c0f:fb50:4000::/56\n          Netmask ffff:ffff:ffff:ff00::\n          Network 2c0f:fb50:4000::\n        Broadcast 2c0f:fb50:4000:ff:ffff:ffff:ffff:ffff\n       First host 2c0f:fb50:4000::1\n        Last host 2c0f:fb50:4000:ff:ffff:ffff:ffff:fffe\n      Total hosts 4722366482869645213694\n             Next 2c0f:fb50:4000:100::/56\n         Previous 2c0f:fb50:3fff:ff00::/56\n             Bits 0010110000001111:1111101101010000:0100000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000:0000000000000000\n      Reverse DNS 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.4.0.5.b.f.f.0.c.2.ip6.arpa.\n```\n\nSplit subnet with defaults (to next smaller subnet / larger prefix):\n\n```bash\nnetlookup split 172.31.1.19/17 2c0f:fb50:4000::/56\n    172.31.0.0/18\n    172.31.64.0/18\n    2c0f:fb50:4000::/57\n    2c0f:fb50:4000:80::/57\n```\n\nSplit IPv4 subnets with specific prefix:\n\n```bash\nnetlookup split --mask 19 172.31.1.19/17 172.31.5.39/17\n    172.31.0.0/19\n    172.31.32.0/19\n    172.31.64.0/19\n    172.31.96.0/19\n    172.31.0.0/19\n    172.31.32.0/19\n    172.31.64.0/19\n    172.31.96.0/19\n```\n\nUsing the python library\n------------------------\n\nSome practical examples for using the API where a CLI command is not yet available.\n\nCreate set of networks and show minimal merged CIDR prefixes to cover this range:\n\n```python\nfrom netlookup.network_sets.base import NetworkSet\nns = NetworkSet()\nns.add_network('172.31.0.0/23')\nns.add_network('172.31.4.0/22')\nns.add_network('172.31.8.0/24')\nns.add_network('172.31.9.0/25')\nns.add_network('172.31.9.128/25')\nprint('\\n'.join(str(x.cidr) for x in ns.merged))\n```\n\nPrevious example returns\n\n```bash\n172.31.0.0/23\n172.31.4.0/22\n172.31.8.0/23\n```\n\nUsing same example, remove one /29 from the result set\n\n```python\nfrom netlookup.network_sets.base import NetworkSet\nns = NetworkSet()\nns.add_network('172.31.0.0/23')\nns.add_network('172.31.4.0/22')\nns.add_network('172.31.8.0/24')\nns.add_network('172.31.9.0/25')\nns.add_network('172.31.9.128/25')\nprint('\\n'.join(str(x.cidr) for x in ns.substract('172.31.8.64/29')))\n```\n\nThis example returns\n\n```bash\n172.31.0.0/23\n172.31.4.0/22\n172.31.8.0/26\n172.31.8.72/29\n172.31.8.80/28\n172.31.8.96/27\n172.31.8.128/25\n172.31.9.0/24\n````\n\n# Cloud vendor prefixes\n\nThis tool contains lookup caches for some cloud vendors. Currently supported vendors are:\n\n- AWS\n- Cloudflare\n- Google Cloud\n- Google Services\n\nNote: Azure support was removed because their data is in a silly URL and I just don't\ncare about them.\n\nExample to load data for cloud vendor IP prefix lookups and save it to user specific cache\ndirectory `~/.config/netlookup`.\n\nFollowing command requires internet connection to update the prefix lists.\n\n```python\nfrom netlookup.prefixes import Prefixes\nns = Prefixes()\nprint(ns.cache_directory)\nns.update()\nns.save()\n````\n\n## Get prefixes for cloud vendors\n\nUse the previously loaded cached cloud vendor IP prefix lookup and find some addresses.\n\n```python\n>>> ns.find('3.81.2.1')\naws us-east-1 3.80.0.0/12\n````\n\nSimilarly, you can get specific vendor network set and lookup address from there:\n\n```python\n>>> ns.get_vendor('google').find('216.58.210.142')\ngoogle 216.58.192.0/19\n```\n",
    'author': 'Ilkka Tuohela',
    'author_email': 'hile@iki.fi',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
