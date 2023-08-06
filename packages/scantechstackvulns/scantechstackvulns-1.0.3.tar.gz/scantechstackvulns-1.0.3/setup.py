# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scantechstackvulns']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'lxml>=4.9.2,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'simplexl>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'scantechstackvulns',
    'version': '1.0.3',
    'description': '',
    'long_description': '## Get Technology Stack Vulnerabilities\n\nThis package is useful for fetching known vulnerabilities of third party components used in projects from [NVD](https://nvd.nist.gov/general) site.\n\n## Getting Started\nUsing get-techstack-vulnerabilities takes almost no time! Simply install via the pip command:\n\n```\npip install scantechstackvulns\n```\n\nFrom here you can import it into your source file by calling:\n\n```\nfrom scantechstackvulns import TechStack\n```\n\n## How it works\nIt takes list of thirdparty components with versions as a input and generates an excel file of known vulnerabilities of that list of components.\n\n## Usage\n\nThe below is the way to use of this package\n\n```\nfrom scantechstackvulns import TechStack\n\ntechnology_stack = [\n    "postgresql 11.11",                     #|\n    "spring framework vmware 4.3.25",       #| \n    "spring framework pivotal 4.3.25",      #|----- sample data\n    "apache tomcat 9.0.58",                 #|\n    "oracle jdk 1.8.0 update 252"           #|\n]\n\noutput_file = "directory/file_name.xlsx"\n\nTechStack.scan(techstack, output_file)\n```\n\n## Note\n- technology stack must contain exact version\n- as of now only xlsx extension supports in output file\n- [here](https://github.com/devarajug/getTechStackVulns/blob/main/sample.xlsx) is the sample xlsx file to verify\n\n\n# License\n\nThis repository is licensed under the [MIT](https://opensource.org/licenses/MIT) license.\nSee [LICENSE](https://opensource.org/licenses/MIT) for details.',
    'author': 'Devaraju Garigapati',
    'author_email': 'devarajugarigapati@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/devarajug/getTechStackVulns',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
