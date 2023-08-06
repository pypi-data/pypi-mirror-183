# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['byproxy', 'byproxy.proxy_checker', 'byproxy.proxy_maker']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<2.29.0']

setup_kwargs = {
    'name': 'byproxy',
    'version': '0.1.4',
    'description': 'ByProxy is a library to generate proxy dictionaries from a list of urls and gain information about the proxies.',
    'long_description': '# ByProxy\n\nByProxy is a simple package contains simple tools for proxy management and usage. You can generate proxy dictionaries from a list of urls and gain information about the proxies.\n\nCheck out the [byproxy API documentation](https://vimevim.github.io/byproxy/) for more information.\n\n## Todos\n\n- [x] Implement a ProxyChecker class to get information about the proxies.\n  - [x] Implement a check_my_ip method to verify the ip of the proxy.\n  - [x] Implement a check_target_url method to verify if the proxy is working with the target url.\n  - [x] Implement a target_ip_details method to get more information about the target ip.\n  - [x] Implement an async_api method to make async requests.\n- [x] Implement a ProxyMaker class to prepare the proxy dictionary.\n  - [x] Implement a read_lines method to read the lines from a file with given path and returns a list.\n  - [x] Implement a split_lines method to split the lines from the list. It takes two arguments, lines and separator. It returns a list of lists.\n  - [x] Implement a lines_to_dict method to convert the list of lists to a dictionary. It takes two arguments, lines and keys.\n  - [x] Implement a make_proxies method to make the proxy dictionary. It takes three arguments, lines, type and password_enabled. It returns a dictionary of proxies which you can use with requests.Session object.\n- [ ] Find a way to validate the proxy format and implement a method to validate proxies.\n- [ ] Improve documentation, changelog, dependencies and readme.\n- [ ] Add examples.\n',
    'author': 'uykusuz',
    'author_email': 'vimevim@gmail.com',
    'maintainer': 'uykusuz',
    'maintainer_email': 'vimevim@gmail.com',
    'url': 'https://vimevim.github.io/byproxy/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.8,<3.9.0',
}


setup(**setup_kwargs)
