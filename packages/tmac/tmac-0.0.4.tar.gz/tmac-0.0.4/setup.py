# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tmac', 'tmac.plus', 'tmac.plus_aws', 'tmac.threat_library']

package_data = \
{'': ['*'], 'tmac': ['templates/*'], 'tmac.threat_library': ['templates/*']}

install_requires = \
['diagrams>=0.23.1,<0.24.0', 'jinja2>=3.1.2,<4.0.0', 'tabulate>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'tmac',
    'version': '0.0.4',
    'description': 'Agile Threat Modeling as Code',
    'long_description': '# tmac\n> Agile Threat Modeling as Code\n- Close to the code - close to developers\n- Optimized for jupyter notebooks\n- Generates data-flow diagrams\n\n## Install\n```bash\npip install tmac\n```\n\n## How to use\n```bash\npython3 tmac.py\n```\n\n```python\n#!/usr/bin/env python3\n\nfrom tmac import (Asset, DataFlow, Machine, Model, Process, Protocol, \n                    Score, TableFormat, Technology)\nfrom tmac.plus import Browser, Database\n\nmodel = Model("REST API Model")\n\nuser = User(model, "User")\n\nweb_server = Process(\n    model,\n    "WebServer",\n    machine=Machine.VIRTUAL,\n    technology=Technology.WEB_APPLICATION,\n)\n\ndatabase = Database(\n    model,\n    "Database",\n    machine=Machine.VIRTUAL,\n)\n\nweb_traffic = user.add_data_flow(\n    "WebTraffic",\n    destination=web_server,\n    protocol=Protocol.HTTPS,\n)\n\nweb_traffic.transfers(\n    "UserCredentials",\n    confidentiality=Score.HIGH,\n    integrity=Score.HIGH,\n    availability=Score.HIGH,\n)\n\ndatabase_traffic = web_server.add_data_flow(\n    "DatabaseTraffic",\n    destination=database,\n    protocol=Protocol.SQL,\n)\n\ndatabase_traffic.transfers(\n    "UserDetails",\n    confidentiality=Score.HIGH,\n    integrity=Score.HIGH,\n    availability=Score.HIGH,\n)\n\nprint(model.risks_table(table_format=TableFormat.GITHUB))\n```\nOutput:\n| ID                 | Risk                                         |\n|--------------------|----------------------------------------------|\n| CAPEC-63@WebServer | Cross-Site Scripting (XSS) risk at WebServer |\n| CAPEC-66@WebServer | SQL Injection risk at WebServer              |\n|...|...|\n```python\nprint(model.create_backlog_table(table_format=TableFormat.GITHUB))\n```\nOutput:\n| ID                            | User Story                                                                                                                                                                                                                              |\n|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n| ASVS-5.1.3@CAPEC-63@WebServer | As a Security Champion I want all of the input which can affect control or data flow to be validated so that I can protect my application from malicious manipulation which could lead to unauthorised disclosure or loss of integrity. |\n| ASVS-5.3.3@CAPEC-63@WebServer | As a Security Champion I want all of the output to be escaped so that I can protect my application against reflected, stored, and DOM based XSS.                                                                                        |\n| ASVS-5.3.4@CAPEC-66@WebServer | As a Security Champion I want all data selection or database queries use parameterized queries so that my application is protected against database injection attacks.                                                                  |\n## Jupyter Threatbooks\n> Threat modeling with jupyter notebooks\n\n![threatbook.png](https://github.com/hupe1980/tmac/raw/main/.assets/threatbook.png)\n\n## Generating Diagrams\n```python\nmodel.create_data_flow_diagram()\n```\n![threatbook.png](https://github.com/hupe1980/tmac/raw/main/.assets/data-flow-diagram.png)\n\n## High level elements (tmac/plus*)\n```python\nfrom tmac.plus_aws import ApplicationLoadBalancer\n\n# ...\n\nalb = ApplicationLoadBalancer(model, "ALB", waf=True)\n\n```\n\n## Custom threatlib\n```python\nfrom tmac import Model, Threatlib\n\nthreatlib = Threatlib()\n\nthreatlib.add_threat("""... your custom threats ...""")\n\nmodel = Model("Demo Model", threatlib=threatlib)\n```\n## Examples\n\nSee more complete [examples](https://github.com/hupe1980/tmac/tree/master/examples).\n\n## Prior work and other related projects\n- [pytm](https://github.com/izar/pytm) - A Pythonic framework for threat modeling\n- [threagile](https://github.com/Threagile/threagile) - Agile Threat Modeling Toolkit\n- [cdk-threagile](https://github.com/hupe1980/cdk-threagile) - Agile Threat Modeling as Code\n- [OpenThreatModel](https://github.com/iriusrisk/OpenThreatModel) - OpenThreatModel\n\n## License\n\n[MIT](LICENSE)',
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
