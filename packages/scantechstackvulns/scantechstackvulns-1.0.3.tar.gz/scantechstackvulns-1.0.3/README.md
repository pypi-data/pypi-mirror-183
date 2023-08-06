## Get Technology Stack Vulnerabilities

This package is useful for fetching known vulnerabilities of third party components used in projects from [NVD](https://nvd.nist.gov/general) site.

## Getting Started
Using get-techstack-vulnerabilities takes almost no time! Simply install via the pip command:

```
pip install scantechstackvulns
```

From here you can import it into your source file by calling:

```
from scantechstackvulns import TechStack
```

## How it works
It takes list of thirdparty components with versions as a input and generates an excel file of known vulnerabilities of that list of components.

## Usage

The below is the way to use of this package

```
from scantechstackvulns import TechStack

technology_stack = [
    "postgresql 11.11",                     #|
    "spring framework vmware 4.3.25",       #| 
    "spring framework pivotal 4.3.25",      #|----- sample data
    "apache tomcat 9.0.58",                 #|
    "oracle jdk 1.8.0 update 252"           #|
]

output_file = "directory/file_name.xlsx"

TechStack.scan(techstack, output_file)
```

## Note
- technology stack must contain exact version
- as of now only xlsx extension supports in output file
- [here](https://github.com/devarajug/getTechStackVulns/blob/main/sample.xlsx) is the sample xlsx file to verify


# License

This repository is licensed under the [MIT](https://opensource.org/licenses/MIT) license.
See [LICENSE](https://opensource.org/licenses/MIT) for details.