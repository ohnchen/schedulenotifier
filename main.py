#!/bin/usr/env python

import requests
from bs4 import BeautifulSoup
import time
import re
import datetime 
from datetime import datetime
from datetime import timedelta, date
from timeit import default_timer as timer
start = timer() # start the timer for controlling how long the program takes

allurl = []
kurse =  ["Q2"] # , "MA11", "PH11", "CH12", "de15", "la15", "po15", "rk15", "sf13", "sp1323", "fn15, la15, ln15"] # for future features

url1_1 = "https://emaos.de/ExportSchueler/Schueler1/subst_001.htm"
url1_2 = "https://emaos.de/ExportSchueler/Schueler1/subst_002.htm"
url1_3 = "https://emaos.de/ExportSchueler/Schueler1/subst_003.htm"
url2_1 = "https://emaos.de/ExportSchueler/Schueler2/subst_001.htm"
url2_2 = "https://emaos.de/ExportSchueler/Schueler2/subst_002.htm"
url2_3 = "https://emaos.de/ExportSchueler/Schueler2/subst_003.htm"

# Squeezing the urls inside a list to be able to iterate over them
urls = [url1_1, url1_2, url1_3, url2_1, url2_2, url2_3] 

# Get the content of all the sites and join them together
for url in urls:
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    allurl.append(soup)
html = "".join(str(allurl))

# Preparing to get the information by the date (of today and tomorrow) if this is the desired feature just uncomment next three lines.

# datum = str(datetime.now().day) + "." + str(datetime.now().month) + "."  # e.g. 2.11.
# next_date = date.today() + timedelta(days=1)  
# tomorrow = str(next_date.day) + "." + str(next_date.month) + "." # e.g. 3.11

# filter() is used to delete everything from the list that is a empty string; list() turns the filterobject back into a list
liste = list(filter(None, re.findall(">(.*?)<", html)))

# Get the index of every date I am searching for; enumerate() so it doesn't only take the firstitem and repeats to return that index every iteration
index = [i for i, e in enumerate(liste) for j in kurse if e == j] 
for k in index:
    print("")
    for i in range(9):
        print(liste[k+i], end=" ")

# Print the time the program needed to complete
elapsed_time = timer() - start
print("\n\n" + str(round(elapsed_time, 3)))
