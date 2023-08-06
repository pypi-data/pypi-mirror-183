__version__ = '1.0.0'

import sys
import warnings
import requests
from bs4 import BeautifulSoup
from simplexl import CreateExcel
from .utils import (
    getCpeMatchStrings,
    getDataFromWeb,
    sepScrappedTechStackData
)


class TechStack:
    
    def __init__(self, techstack, output_file):
        warnings.filterwarnings('ignore')
        self.techstack = techstack
        self.output_file = output_file
        self.noOfIssuesCount = None
        self.countFrom = None
        self.countThrough = None
        self.startIndex = 0
        self.vulnSearchUrl = "https://nvd.nist.gov/vuln/search/results?adv_search=true&isCpeNameSearch=true&query="
          

    @property
    def cpeMatchStrings(self):
        return getCpeMatchStrings(self.techstack)
    

    def scrapeTechStackData(self, cpe, startIndex=0):
        try:
            vulnSearchUrl = f"{self.vulnSearchUrl}{cpe}&startIndex={startIndex}"
            response = getDataFromWeb(url=vulnSearchUrl)
            if response.status_code == 200:
                parsed_data = BeautifulSoup(response.text, 'lxml')
                self.noOfIssuesCount = int(parsed_data.select_one('strong[data-testid=vuln-matching-records-count]').text)
                self.countFrom = int(parsed_data.select_one('strong[data-testid=vuln-displaying-count-from]').text)
                self.countThrough = int(parsed_data.select_one('strong[data-testid=vuln-displaying-count-through]').text)
                TechStackData = parsed_data.select_one('table[data-testid=vuln-results-table]')
            else:
                #ToDo add logger
                pass


        except Exception as e:
            TechStackData = None
            print("Unable fetch data from nvd database please try after sometime........")
            sys.exit(e)
        return TechStackData
    

    def techStackDataToList(self):
        try:
            print()
            print("Getting CPE Match Strings for TechStack...")
            productname, cve, severity, description, status = [[] for i in range(5)]
            for product, cpe in self.cpeMatchStrings.items():
                print()
                data = self.scrapeTechStackData(cpe=cpe)
                if self.noOfIssuesCount == 0:
                    productname.append(product.strip())
                    cve.append("No vulnerability")
                    severity.append("No vulnerability")
                    description.append("No vulnerability")
                    status.append("Closed")
                    print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                elif self.noOfIssuesCount <= 20:
                    issues_table = self.scrapeTechStackData(cpe=cpe)
                    count = sepScrappedTechStackData(
                        issues_table=issues_table,
                        noOfIssuesCount=self.noOfIssuesCount,
                        productname=productname,
                        cve=cve,
                        severity=severity,
                        description=description,
                        status=status,
                        product=product
                    )
                    
                elif self.noOfIssuesCount > 20:
                    count_while = 0
                    while self.noOfIssuesCount - self.startIndex >= 0 :
                        issues_table = self.scrapeTechStackData(
                            cpe=cpe,
                            startIndex=self.startIndex
                        )
                        count_while += sepScrappedTechStackData(
                            issues_table=issues_table,
                            noOfIssuesCount=self.noOfIssuesCount,
                            productname=productname,
                            cve=cve,
                            severity=severity,
                            description=description,
                            status=status,
                            product=product
                        )
                        self.startIndex+=20
                    else:
                        if count_while == 0:
                            productname.append(product)
                            cve.append("No vulnerability")
                            severity.append("No vulnerability")
                            description.append("No vulnerability")
                            status.append("Closed")
                            print(productname[-1]+ " : " + cve[-1] + " : " + severity[-1])
                else:
                    sys.exit("some thing went wrong pls re run the script")
            tech_stack_data = zip(productname, description, cve, severity, status)

        except Exception as e:
            df_tech_stack = None
            print("Unable fetch data from nvd database please try after sometime........")
            sys.exit(e)

        return tech_stack_data
    

    def makeXL(self):
        try:
            tech_stack_data = self.techStackDataToList()
            
            tech_stack_sheet_columns = [
                "DependencyName",
                "Description",
                "CVE",
                "Severity",
                "Status"
            ]

            xl = CreateExcel()
            xl.create_sheet(
                col_data=tech_stack_sheet_columns,
                row_data=list(tech_stack_data)
            )
            xl.save(self.output_file)   
            print()
            print('execl created successfully....')
            print()
            return
        except Exception as e:
            print("Unable to create xls....")
            sys.exit(e)
    

    @classmethod
    def scan(cls, techstack, output_file):
        obj = cls(techstack, output_file)
        return obj.makeXL()

