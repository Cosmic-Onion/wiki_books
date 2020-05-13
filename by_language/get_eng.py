import requests
import json
import lxml.html
import re
import string

url_list = ["A-C","D-J","K-Q","R-Z"]
listOfWritersURL = "https://en.wikipedia.org/wiki/List_of_English_writers_("
req = requests.Session()

for page in url_list:
    request_url = req.get(listOfWritersURL+page+")")
    print(request_url)
    lupine = lxml.html.fromstring(request_url.text)
    writerList = []

    #TODO: add if statement to check if this even exists

    body = lupine.xpath('/html/body/div[3]/div[3]/div[4]/div/div/ul/li')
                        
    for writer in body:             
        writerLinks = writer.xpath("a")
        if writerLinks == []:
            continue
        else:
            writerName = writerLinks[0].text_content()
            for writerPage in writer.iterlinks():
                writerURL = writerPage[2]
                #check if writerURL contains list, if so add to linklist
                break

            temp = {writerName : writerURL}
            writerList.append(temp) #improve memory usage

with open("../../json/eng0.json", "w", encoding="utf8") as outfile:
    json.dump(writerList, outfile)





'''
def addNationalities(page):
    print("\n",page,"\n")
    eggo = req.get(page).text
    eggo = lxml.html.fromstring(eggo)

    for item in eggo.xpath("//i"):
        if "See:" in item.text_content():
            for link in item.iterlinks():
                linkList.append(baseURL + link[2])
                addNationalities(baseURL + link[2])




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


with open("linkList1.txt","w") as txtFile:
    for item in linkList:
        txtFile.write("%s\n" % item)

writerDict = {}

for link in linkList:
    writerList = []
    lupine = lxml.html.fromstring(req.get(link).text)

    #TODO: add if statement to check if this even exists

    body_1 = lupine.xpath("/html/body/div[3]/div[3]/div[4]/div/ul/li")
    body_2 = lupine.xpath("/html/body/div[3]/div[3]/div[4]/div/div/ul/li")

    if len(body_2) > len(body_1):
        body = body_2
    else:
        body = body_1

    for writer in body:             
        writerLinks = writer.xpath("a")
        if writerLinks == []:
            continue
        else:
            writerName = writerLinks[0].text_content()
            for writerPage in writer.iterlinks():
                writerURL = writerPage[2]
                #check if writerURL contains list, if so add to linklist
                break

            temp = {writerName : writerURL}
            writerList.append(temp) #improve memory usage

    writerDict[link] = []
    writerDict[link].append(writerList)

with open("../json/author8.json", "w", encoding="utf8") as outfile:
    json.dump(writerDict, outfile)
'''