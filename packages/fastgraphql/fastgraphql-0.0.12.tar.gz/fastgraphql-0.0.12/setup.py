# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastgraphql']

package_data = \
{'': ['*']}

install_requires = \
['graphql-core>=3.0,<4.0', 'pydantic>=1.10.2,<2.0.0']

extras_require = \
{'all': ['ariadne>=0.14,<1.0',
         'fastapi>=0.70,<1.0',
         'SQLAlchemy[mypy]>=1.4.0,<1.5.0'],
 'ariadne': ['ariadne>=0.14,<1.0'],
 'fastapi': ['fastapi>=0.70,<1.0'],
 'sqlalchemy': ['SQLAlchemy[mypy]>=1.4.0,<1.5.0']}

setup_kwargs = {
    'name': 'fastgraphql',
    'version': '0.0.12',
    'description': 'FastGraphQL is intended to help developer create code driven GraphQL APIs',
    'long_description': '# FastGraphQL\n![FastGraphQL](docs/pages/assets/logo_text.svg)\n<p style="text-align: center;">FastGraphQL is a tool for creating code-driven GraphQL APIs.</p>\n\n----------\n\n![pypi](https://img.shields.io/pypi/v/fastgraphql)\n![Python Versions](https://img.shields.io/pypi/pyversions/fastgraphql.svg?color=%2334D058)\n![License](https://img.shields.io/pypi/l/fastgraphql)\n\n[![codecov](https://codecov.io/gh/hugowschneider/fastgraphql/branch/main/graph/badge.svg?token=FCC5LMA0IQ)](https://codecov.io/gh/hugowschneider/fastgraphql)\n![tests](https://github.com/hugowschneider/fastgraphql/actions/workflows/test.yaml/badge.svg)\n\n\n[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=bugs)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n\n-------\nDocumentation: <a href="https://hugowschneider.github.io/fastgraphql" target="_blank">https://hugowschneider.github.io/fastgraphql</a>\n\nSource Code: <a href="https://github.com/hugowschneider/fastgraphql" target="_blank">https://github.com/hugowschneider/fastgraphql</a>\n\n# Disclaimer\n\n*This is still a work in progress and all support is welcomed*\n\n# Motivation\n\nSo far most of the projects that use GraphQL need to duplicate\nmany definitions to be able to have a consistent GraphQL API schema\nalongside well-defined models that governs the development and the application.\n\nFastGraphQL proposes to shortcut the path between python models and GraphQL schema\nusing **Pydantic** models. This ensures not only a single source of truth when comes to\ntype, input, query and mutation definitions, but also the\nability to use **Pydantic** to features on models and inputs.\n\n# Installation\n\n```shell\n$ pip install "fastgraphql[all]"\n```\nYou will also need an ASGI server as well to serve your API\n\n```shell\n$ pip install "uvicorn[standard]"\n```\n\n# Usage\n\nThe very first Hello Work example.\n\n```python\nfrom fastapi import FastAPI\nfrom fastgraphql import FastGraphQL\nfrom fastgraphql.fastapi import make_ariadne_fastapi_router\n\napp = FastAPI()\nfast_graphql = FastGraphQL()\n\n\n@fast_graphql.query()\ndef hello() -> str:\n    return "Hello FastGraphQL!!!"\n\n\napp.include_router(make_ariadne_fastapi_router(fast_graphql=fast_graphql))\n\n```\n\n```shell\n$ uvicorn main:app --reload\n```\n\nA simple example will not show you the all **FastGraphQL** capabilities, but it\nshows how simple this can be.\n\n# Learn\n\nTo start your journey into **FastGraphQL**, please refer to [Getting Started](https://hugowschneider.github.io/fastgraphql/tutorial/).\n\nYou can find the API documentation [here](https://hugowschneider.github.io/fastgraphql/api/fastgraphql/).\n\n# Integration\n\nFastGraphQL generates independently of any integration a data structure containing all GraphQL definitions and resolvers, which\ngenerates a GraphQL schema.\n\nWith that said, all integration will add functionalities and provide\neasy and alternative deployments of the defined API.\n\nYou can find out more about the different integrations under [Integrations](https://hugowschneider.github.io//fastgraphql/under-construction/)\n\n# Acknowledgment\n\nThanks to [FastAPI](https://fastapi.tiangolo.com) for the inspiration!\n',
    'author': 'Hugo Wruck Schneider',
    'author_email': 'hugowschneider@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hugowschneider/fastgraphql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
