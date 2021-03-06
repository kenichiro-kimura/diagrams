# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diagrams',
 'diagrams.alibabacloud',
 'diagrams.aws',
 'diagrams.azure',
 'diagrams.base',
 'diagrams.custom',
 'diagrams.elastic',
 'diagrams.firebase',
 'diagrams.gcp',
 'diagrams.generic',
 'diagrams.k8s',
 'diagrams.oci',
 'diagrams.onprem',
 'diagrams.openstack',
 'diagrams.outscale',
 'diagrams.programming',
 'diagrams.saas','resources']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.13.2,<0.14.0', 'jinja2>=2.10,<3.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['contextvars>=2.4,<3.0']}

setup_kwargs = {
    'name': 'diagrams',
    'version': '0.17.0',
    'description': 'Diagram as Code',
    'long_description': '![diagrams logo](assets/img/diagrams.png)\n\n# Diagrams\n\n[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)\n[![pypi version](https://badge.fury.io/py/diagrams.svg)](https://badge.fury.io/py/diagrams)\n![python version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python)\n![Run tests](https://github.com/mingrammer/diagrams/workflows/Run%20tests/badge.svg?branch=master)\n[![todos](https://badgen.net/https/api.tickgit.com/badgen/github.com/mingrammer/diagrams?label=todos)](https://www.tickgit.com/browse?repo=github.com/mingrammer/diagrams)\n\n![on premise provider](https://img.shields.io/badge/provider-OnPremise-orange?color=5f87bf)\n![aws provider](https://img.shields.io/badge/provider-AWS-orange?logo=amazon-aws&color=ff9900)\n![azure provider](https://img.shields.io/badge/provider-Azure-orange?logo=microsoft-azure&color=0089d6)\n![gcp provider](https://img.shields.io/badge/provider-GCP-orange?logo=google-cloud&color=4285f4)\n![kubernetes provider](https://img.shields.io/badge/provider-Kubernetes-orange?logo=kubernetes&color=326ce5)\n![alibaba cloud provider](https://img.shields.io/badge/provider-AlibabaCloud-orange)\n![oracle cloud provider](https://img.shields.io/badge/provider-OracleCloud-orange?logo=oracle&color=f80000)\n![openstack provider](https://img.shields.io/badge/provider-OpenStack-orange?logo=openstack&color=da1a32)\n![firebase provider](https://img.shields.io/badge/provider-Firebase-orange?logo=firebase&color=FFCA28)\n![outscale provider](https://img.shields.io/badge/provider-OutScale-orange?color=5f87bf)\n![elastic provider](https://img.shields.io/badge/provider-Elastic-orange?logo=elastic&color=005571)\n![generic provider](https://img.shields.io/badge/provider-Generic-orange?color=5f87bf)\n![programming provider](https://img.shields.io/badge/provider-Programming-orange?color=5f87bf)\n![saas provider](https://img.shields.io/badge/provider-SaaS-orange?color=5f87bf)\n\n<a href="https://www.buymeacoffee.com/mingrammer" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>\n\n**Diagram as Code**.\n\nDiagrams lets you draw the cloud system architecture **in Python code**. It was born for **prototyping** a new system architecture design without any design tools. You can also describe or visualize the existing system architecture as well. Diagrams currently supports main major providers including: `AWS`, `Azure`, `GCP`, `Kubernetes`, `Alibaba Cloud`, `Oracle Cloud` etc... It also supports `On-Premise` nodes, `SaaS` and major `Programming` frameworks and languages.\n\n**Diagram as Code** also allows you to **track** the architecture diagram changes in any **version control** system.\n\n>  NOTE: It does not control any actual cloud resources nor does it generate cloud formation or terraform code. It is just for drawing the cloud system architecture diagrams.\n\n## Getting Started\n\nIt requires **Python 3.6** or higher, check your Python version first.\n\nIt uses [Graphviz](https://www.graphviz.org/) to render the diagram, so you need to [install Graphviz](https://graphviz.gitlab.io/download/) to use **diagrams**. After installing graphviz (or already have it), install the **diagrams**.\n\n> macOS users can download the Graphviz via `brew install graphviz` if you\'re using [Homebrew](https://brew.sh).\n\n```shell\n# using pip (pip3)\n$ pip install diagrams\n\n# using pipenv\n$ pipenv install diagrams\n\n# using poetry\n$ poetry add diagrams\n```\n\nYou can start with [quick start](https://diagrams.mingrammer.com/docs/getting-started/installation#quick-start). Check out [guides](https://diagrams.mingrammer.com/docs/guides/diagram) for more details, and you can find all available nodes list in [here](https://diagrams.mingrammer.com/docs/nodes/aws).\n\n## Examples\n\n| Event Processing                                             | Stateful Architecture                                        | Advanced Web Service                                         |\n| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |\n| ![event processing](https://diagrams.mingrammer.com/img/event_processing_diagram.png) | ![stateful architecture](https://diagrams.mingrammer.com/img/stateful_architecture_diagram.png) | ![advanced web service with on-premise](https://diagrams.mingrammer.com/img/advanced_web_service_with_on-premise.png) |\n\nYou can find all the examples on the [examples](https://diagrams.mingrammer.com/docs/getting-started/examples) page.\n\n## Contributing\n\nTo contribute to diagram, check out [contribution guidelines](CONTRIBUTING.md).\n\n> Let me know if you are using diagrams! I\'ll add you in showcase page. (I\'m working on it!) :)\n\n## Who uses it?\n\n[![GitPitch](https://gitpitch.com/gpimg/logo.png)](https://gitpitch.com/)\n\n[GitPitch](https://gitpitch.com/) is a markdown presentation service for developers. Diagrams is now integrated as [Cloud Diagram Widget](https://gitpitch.com/docs/diagram-features/cloud-diagrams/) of GitPitch, so you can use the Diagrams when to create slide decks for Tech Conferences, Meetups, and Training with GitPitch.\n\n[Cloudiscovery](https://github.com/Cloud-Architects/cloudiscovery) helps you to analyze resources in your cloud (AWS/GCP/Azure/Alibaba/IBM) account. It allows you to create a diagram of analyzed cloud resource map based on this Diagrams library, so you can draw the your existing cloud infratructure with Cloudicovery.\n\n[Airflow Diagrams](https://github.com/feluelle/airflow-diagrams) is an Airflow plugin that aims to easily visualise your Airflow DAGs on service level from providers like AWS, GCP, Azure, etc. via diagrams.\n\n## License\n\n[MIT](LICENSE)\n',
    'author': 'mingrammer',
    'author_email': 'mingrammer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://diagrams.mingrammer.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
    'include_package_data': True
}


setup(**setup_kwargs)
