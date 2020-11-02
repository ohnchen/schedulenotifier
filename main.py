#!/bin/usr/env python

import requests
from bs4 import BeautifulSoup
import time
import re
import datetime 
from datetime import datetime
from datetime import timedelta, date
from timeit import default_timer as timer
start = timer()

allurl = []
kurse = ["MA11"]

url1_1 = "https://emaos.de/ExportSchueler/Schueler1/subst_001.htm"
url1_2 = "https://emaos.de/ExportSchueler/Schueler1/subst_002.htm"
url1_3 = "https://emaos.de/ExportSchueler/Schueler1/subst_003.htm"
url2_1 = "https://emaos.de/ExportSchueler/Schueler2/subst_001.htm"
url2_2 = "https://emaos.de/ExportSchueler/Schueler2/subst_002.htm"
url2_3 = "https://emaos.de/ExportSchueler/Schueler2/subst_003.htm"

urls = [url1_1, url1_2, url1_3, url2_1, url2_2, url2_3]

for url in urls:
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    allurl.append(soup)

html = "".join(str(allurl))
datum = str(datetime.now().day) + "." + str(datetime.now().month) + "."  # e.g. 2.11.
next_date = date.today() + timedelta(days=1)  
tomorrow = str(next_date.day) + "." + str(next_date.month) + "." # e.g. 3.11

liste = list(filter(None, re.findall(">(.*?)<", html)))

index = [i for i, e in enumerate(liste) if e == datum or e == tomorrow] 
for j in index:
    print("")
    for i in range(9):
        print(liste[j-1+i], end=" ")

elapsed_time = timer() - start
print(elapsed_time)
