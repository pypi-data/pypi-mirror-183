import requests
import warnings


warnings.filterwarnings('ignore')
CPESEARCHURL = "https://services.nvd.nist.gov/rest/json/cpes/2.0?keywordSearch={}&resultsPerPage=10000"

def getDataFromWeb(url):
    try:
        with requests.Session() as request:
            request.verify = False
            return request.get(url=url)
    except Exception as err:
        # TODO Add logger
        pass

def getCpeMatchStrings(techstack):
    
    cpeMatchStrings = {}
    for each in techstack:
        response = getDataFromWeb(url=CPESEARCHURL.format(each))
        if response.status_code == 200:
            result = response.json()
            for product in result.get("products"):
                match_string = product.get("cpe", {}).get("cpeName")
                if all(x.lower() in match_string.lower() for x in each.split(" ")):
                    cpeMatchStrings[str(each)] = str(match_string)
        print(f"CPE Match String for {each}: {cpeMatchStrings.get(each)}")
    print()
    print("Analysis Started. It Takes Time to Complete, Please Wait Patiently")
    return cpeMatchStrings



def sepScrappedTechStackData(issues_table, noOfIssuesCount, cve, description, severity, productname, status, product):
    count = 0
    for i in range(noOfIssuesCount):
        description_data = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td p[data-testid=vuln-summary-{i}]').text.strip()
        if "unspecified vulnerability" in description_data.lower() or "disputed" in description_data.lower():
            continue
        else:
            productname.append(product.strip())
            cve.append(issues_table.select_one(f'tr[data-testid=vuln-row-{i}] th strong a[href]').text.strip())
            description.append(description_data)
            cvss3 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss3-link]')
            
            if cvss3:
                cvss3_score_severity = cvss3.text.split(":")[-1]
                cvss3_severity = cvss3_score_severity.split(" ")[-1]
                severity.append(cvss3_severity.strip())
            else:
                cvss2 = issues_table.select_one(f'tr[data-testid=vuln-row-{i}] td[nowrap=nowrap] span[id=cvss2-link{i}]').text
                cvss2_score_severity = cvss2.split(":")[-1]
                cvss2_severity = cvss2_score_severity.split(" ")[-1]
                severity.append(cvss2_severity.strip())
            status.append("Open")
            count+=1
        print(f"{productname[-1]} : {cve[-1]} : {severity[-1]}")
    else:
        
        if count == 0:
            productname.append(product.strip())
            cve.append("No vulnerability")
            severity.append("No vulnerability")
            description.append("No vulnerability")
            status.append("Closed")
            print(f"{productname[-1]} : {cve[-1]} : {severity[-1]}")
    
    return count