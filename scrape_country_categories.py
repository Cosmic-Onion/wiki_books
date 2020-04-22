import requests
import json
import lxml.html
import re

def cleanText(text):
    banana = re.sub("\W|books|[0-9]*", "", text)
    return banana

def cleanIterLinks(text):
    banana = re.sub("CP*F*$|PF*$", "", text)
    return banana

def scrapeSubcategory(url):
    subCategory = requests.get(url)
    subCategory = lxml.html.fromstring(subCategory.text)
   
    subPages = []
    groupsJSON = []

    '''
    check if mw-category-group is empty
    if so, scrape mw-content-ltr
    '''

    links = subCategory.xpath("//div[@class='CategoryTreeItem']")

    if links != []:
        for link in links:

            text = cleanIterLinks(cleanText(link.text_content()))

            for linkURL in link.iterlinks():
                URL = ROOTURL + linkURL[2]

            pageJSON = {
                "title": text,
                "URL": URL
            }
            subPages.append(pageJSON)
    else:
        print("hello")
        links = subCategory.xpath("//div[@class='mw-content-ltr']")
        for link in links:
            for bookPage in link.xpath("//li"):
                text = cleanIterLinks(cleanText(bookPage.text_content()))

                for linkURL in bookPage.iterlinks():
                    URL = ROOTURL + linkURL[2]

                pageJSON = {
                    "title": text,              ##TODO: clean code with function assignment here
                    "URL": URL
                }
                subPages.append(pageJSON)

    # with open("subTEst5.json", "a", encoding="utf8") as outfile:
    #     json.dump(groupsJSON, outfile)

    return subPages

ENDPOINT = "https://en.wikipedia.org/w/api.php"
REQUEST = "https://en.wikipedia.org/wiki/Category:Books_by_country"
ROOTURL = "https://en.wikipedia.org"

root = requests.get(REQUEST)
root = lxml.html.fromstring(root.text)
rootPages = []
group = {}

for links in root.xpath("//div[@class='CategoryTreeItem']"):

    categoryTitle = cleanIterLinks(cleanText(links.text_content()))
    for link in links.iterlinks():
        groupURL = ROOTURL + link[2]

    subGroups = scrapeSubcategory(groupURL)

    group[categoryTitle] = []
    group[categoryTitle].append(subGroups)

#print(rootPages)

with open("./json/categories2.json", "w", encoding="utf8") as outfile:
    json.dump(group, outfile)
