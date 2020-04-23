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

def isCategory(link):
    ananas = re.search("Category:",link)
    return ananas

def scrapeSubcategory(url):
    subCategory = requests.get(url)
    subCategory = lxml.html.fromstring(subCategory.text)
   
    subPages = []
    groupsJSON = []
    subGroup = {}

    '''
    check if mw-category-group is empty
    if so, scrape mw-content-ltr
    '''
    
    

    Categorylinks = subCategory.xpath("//div[@class='CategoryTreeItem']")
    for link in Categorylinks:

        text = cleanIterLinks(cleanText(link.text_content()))

        for linkURL in link.iterlinks():
            URL = ROOTURL + linkURL[2]
        
        if isCategory(URL) == None:
            pageJSON = {
            "title": text,
            "URL": URL
            }
            subPages.append(pageJSON)
        else:
            subGroup[text] = []
            subGroup[text].append(scrapeSubcategory(URL))

           
    
        
    Pagelinks = subCategory.xpath("//div[@class='mw-content-ltr']")
    for Pagelink in Pagelinks[0].xpath("//li"):
        
        text = cleanIterLinks(cleanText(Pagelink.text_content()))
        print(text)
        for linkURL in Pagelink.iterlinks():
            URL = ROOTURL + linkURL[2]

        pageJSON = {
            "title": text,              ##TODO: clean code with function assignment here
            "URL": URL
        }
        subPages.append(pageJSON)
        return subPages
    
    with open("./json/subTEst5.json", "a", encoding="utf8") as outfile:
        json.dump(subGroup, outfile)

    return subGroup

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

    with open("./json/recursive.json", "a", encoding="utf8") as outfile:
        json.dump(group, outfile)

#print(rootPages)

