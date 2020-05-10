import requests
import json
import lxml.html
import re

def addNationalities(page):
    print("\n",page,"\n")
    eggo = req.get(page).text
    eggo = lxml.html.fromstring(eggo)

    for item in eggo.xpath("//i"):
        if "See:" in item.text_content():
            for link in item.iterlinks():
                linkList.append(baseURL + link[2])

req = requests.Session()

listOfWritersURL = "https://en.wikipedia.org/wiki/Lists_of_writers"
baseURL = "https://en.wikipedia.org"

gnocchi = req.get(listOfWritersURL).text

gnocchi = lxml.html.fromstring(gnocchi)

writers = gnocchi.xpath("//div[@style='-moz-column-width: 18em; -webkit-column-width: 18em; column-width: 18em;']")[1]

linkList = []

for nationality in writers:
   for link in nationality.iterlinks():
       nextPage = baseURL + link[2]
       linkList.append(nextPage)
       addNationalities(nextPage)

with open("linkList0.txt","w") as txtFile:
    for item in linkList:
        txtFile.write("%s\n" % item)