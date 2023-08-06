# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tmac', 'tmac.plus', 'tmac.plus_aws', 'tmac.threatlib']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.20.1,<0.21.0', 'tabulate>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'tmac',
    'version': '0.0.2',
    'description': 'Agile Threat Modeling as Code',
    'long_description': '# tmac\n> Agile Threat Modeling as Code\n\n## Install\n```bash\npip install tmac\n```\n\n## How to use\n```bash\npython3 tmac.py\n```\n\n```python\n#!/usr/bin/env python3\n\nfrom tmac import (Asset, DataFlow, DataStore, Machine, Model,\n                  Process, Protocol, Score, TableFormat, Technology)\nfrom tmac.plus import Browser\n\nmodel = Model("Login Model")\n\nuser = Browser(model, "User")\n\nweb_server = Process(\n    model, "WebServer",\n    machine=Machine.VIRTUAL,\n    technology=Technology.WEB_WEB_APPLICATION,\n)\n\nlogin = DataFlow(\n    model, "Login",\n    source=user,\n    destination=web_server,\n    protocol=Protocol.HTTPS,\n)\n\nlogin.transfers(\n    "UserCredentials",\n    confidentiality=Score.HIGH,\n    integrity=Score.HIGH,\n    availability=Score.HIGH,\n)\n\ndatabase = DataStore(\n    model, "Database",\n    machine=Machine.VIRTUAL,\n    technology=Technology.DATABASE,\n)\n\nauthenticate = DataFlow(\n    model, "Authenticate",\n    source=web_server,\n    destination=database,\n    protocol=Protocol.SQL,\n)\n\nuser_details = Asset(\n    model, "UserDetails",\n    confidentiality=Score.HIGH,\n    integrity=Score.HIGH,\n    availability=Score.HIGH,\n)\n\nauthenticate.transfers(user_details)\n\nprint(model.risks_table(table_format=TableFormat.GITHUB))\n```\nOutput:\n| SID                 | Severity   | Category                   | Name                                | Affected   | Treatment   |\n|---------------------|------------|----------------------------|-------------------------------------|------------|-------------|\n| CAPEC-63@WebServer  | elevated   | Inject Unexpected Items    | Cross-Site Scripting (XSS)          | WebServer  | mitigated   |\n| CAPEC-100@WebServer | high       | Manipulate Data Structures | Overflow Buffers                    | WebServer  | unchecked   |\n| CAPEC-101@WebServer | elevated   | Inject Unexpected Items    | Server Side Include (SSI) Injection | WebServer  | mitigated   |\n| CAPEC-62@WebServer  | high       | Subvert Access Control     | Cross Site Request Forgery          | WebServer  | unchecked   |\n| CAPEC-66@WebServer  | elevated   | Inject Unexpected Items    | SQL Injection                       | WebServer  | unchecked   |\n|...|...|...|...|...|...|\n\n## Jupyter Threatbooks\n> Threat modeling with jupyter notebooks\n\n![threatbook.png](https://github.com/hupe1980/tmac/raw/main/.assets/threatbook.png)\n\n## Generating Diagrams\n```python\nmodel.data_flow_diagram()\n```\n![threatbook.png](https://github.com/hupe1980/tmac/raw/main/.assets/data-flow-diagram.png)\n\n## High level elements (tmac/plus*)\n```python\nfrom tmac.plus_aws import ApplicationLoadBalancer\n\n# ...\n\nalb = ApplicationLoadBalancer(model, "ALB", waf=True)\n\n```\n\n## Custom threatlib\n```python\nfrom tmac import Model, Threatlib\n\nthreatlib = Threatlib()\n\nthreatlib.add_threat("""... your custom threats ...""")\n\nmodel = Model("Demo Model", threatlib=threatlib)\n```\n## Examples\n\nSee more complete [examples](https://github.com/hupe1980/tmac/tree/master/examples).\n\n## Prior work and other related projects\n- [pytm](https://github.com/izar/pytm) - A Pythonic framework for threat modeling\n- [threagile](https://github.com/Threagile/threagile) - Agile Threat Modeling Toolkit\n- [cdk-threagile](https://github.com/hupe1980/cdk-threagile) - Agile Threat Modeling as Code\n- [OpenThreatModel](https://github.com/iriusrisk/OpenThreatModel) - OpenThreatModel\n\n## License\n\n[MIT](LICENSE)',
    'author': 'hupe1980',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hupe1980/tmac',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
