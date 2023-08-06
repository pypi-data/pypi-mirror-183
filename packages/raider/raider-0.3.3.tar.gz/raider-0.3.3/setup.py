# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raider', 'raider.parsers', 'raider.plugins', 'raider.plugins.basic']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'funcparserlib>=1.0.0a0,<2.0.0',
 'hy>=1.0.a4,<2.0',
 'igraph>=0.10.2,<0.11.0',
 'ipython>=8.4.0,<9.0.0',
 'pkce>=1.0.3,<2.0.0',
 'requests-toolbelt>=0.10.1,<0.11.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['raider = raider.cli:main']}

setup_kwargs = {
    'name': 'raider',
    'version': '0.3.3',
    'description': 'OWASP Raider: a novel framework for manipulating the HTTP processes of persistent sessions.',
    'long_description': '![Raider logo](https://raiderauth.com/images/logo/logo.png)\n\n# Quick links\n\n- [Website](https://raiderauth.com/).\n- [OWASP page](https://owasp.org/www-project-raider/).\n- [Documentation](https://docs.raiderauth.com/en/latest/).\n- [Installation](https://docs.raiderauth.com/en/latest/overview/install.html).\n- [FAQ](https://docs.raiderauth.com/en/latest/overview/faq.html).\n- [Getting started](https://docs.raiderauth.com/en/latest/tutorials/getting_started.html).\n- [Architecture](https://docs.raiderauth.com/en/latest/case_studies/architecture.html).\n- [Discussions](https://github.com/OWASP/raider/discussions).\n- [Issues](https://github.com/OWASP/raider/issues).\n- [Twitter](@raiderauth).\n- [Fediverse](@raiderauth@infosec.exchange).\n\n# What is Raider\n\nOWASP Raider was developed with the goal to improve web authentication\ntesting. By now it has evolved and can be used for all kinds of\nstateful HTTP processes.  It abstracts the client-server information\nexchange as a finite state machine. Each step comprises one request\nwith inputs, one response with outputs, arbitrary actions to do on the\nresponse, and conditional links to other stages. Thus, a graph-like\nstructure is created. Raider allows you to simulate complex systems\nwhile allowing you to control each piece of data you get in and out of\nthe system.\n\n# Graph-like architecture\n\nRaider defines a DSL to describe the information flow between the\nclient and the server for HTTP processes. Each step of the process is\ndescribed by a Flow, which contains the Request with inputs, Response\nwith outputs, and arbitrary actions including links to other Flows:\n\n![Flows](https://raiderauth.com/images/illustrations/raider_flows.png)\n\nChaining several Flows together can be used to simulate any stateful\nHTTP process. FlowGraphs indicate the starting point. They can be\nplaced on any Flow. A FlowGraphs runs all Flows in the link until\nSuccess/Failure is returned or if there are no more links.\n\n![Flows and FlowGraphs](https://raiderauth.com/images/illustrations/graph.png)\n\n# Configuration\n\nRaider\'s configuration is inspired by Emacs. Hylang is used, which is\nLISP on top of Python. LISP is used because of its "Code is Data, Data\nis Code" property. With the magic of LISP macros generating\nconfiguration automatically becomes easy. Flexibility is in its DNA,\nmeaning it can be infinitely extended with actual code. \nYou can use it for example to create, store, reproduce, and share\nproof-of-concepts easily for HTTP attacks. With Raider you can also\nsearch through your Projects, filter by hyfile, Flows, FlowGraphs,\netc... Then you run either just one step, or a chain of steps, so you\ncan automate and run tests on any HTTP process.\n\n\n![Example hylang configuration](https://raiderauth.com/images/illustrations/config.png)\n\n\n# Command line interface\n\nYou can use it for example to create, store, reproduce, and share\nproof-of-concepts easily for HTTP attacks. With Raider you can also\nsearch through your Projects, filter by hyfile, Flows, FlowGraphs,\netc... Then you run either just one step, or a chain of steps, so you\ncan automate and run tests on any HTTP process.\n\nYou can also search through your Projects, filter by hyfile, Flows,\nFlowGraphs, etc… Then you run either just one step, or a chain of\nsteps, so you can automate and run tests the HTTP process.\n',
    'author': 'Daniel Neagaru',
    'author_email': 'daniel@digeex.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://raiderauth.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
