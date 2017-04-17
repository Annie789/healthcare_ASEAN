#This script downloads disease statistics from data.gov.sg
#download for the month.

import sys
import os

DIRECTORY = '../../Data/raw/disease_SG'
OUTFILE = "../../Data/raw/disease_SG/weekly-dengue-malaria.csv"
DISEASE_LIST = ["Dengue Fever", "Dengue Haemorrhagic Fever", "Malaria"]

def download():
    if sys.version_info < (3, 0):
        try:
            os.makedirs(DIRECTORY)
        except OSError as e:
            pass
        
        import urllib2
        import json
        import csv
        url = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=50000'
        #request = urllib2.Request(url)
        request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        fileobj = urllib2.urlopen(request)
     
        temp=json.loads(fileobj.read())
        with open(OUTFILE, 'wb') as csvfile:
            writethis = csv.writer(csvfile, delimiter=',')
            for i in temp["result"]["records"]:
                if i["disease"] in DISEASE_LIST:
                    writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])

    else:
        os.makedirs(DIRECTORY, exist_ok=True)
        import json
        import csv
        import requests
    
        url = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=50000'
        fileobj = requests.get(url)
        temp=json.loads(fileobj.text)
    
        with open(OUTFILE, 'w', newline='') as csvfile:
            writethis = csv.writer(csvfile, delimiter=',')
            for i in temp["result"]["records"]:
                if i["disease"] in DISEASE_LIST:
                    writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])