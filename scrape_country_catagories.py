import requests
import json
import lxml.html
import re


def cleanText(text):
    banana = re.sub("\W|books", "", text)
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

    #loop = 0  # two main groups, first more subgroups, the second are books
    

        
    for links in subCategory.xpath("//div[@class='CategoryTreeItem']"):

        text = cleanIterLinks(cleanText(links.text_content()))

        for link in links.iterlinks():
            URL = ROOTURL + link[2]

        pageJSON = {
            "title": text,
            "URL": URL
        }
        subPages.append(pageJSON)
    
    # groupsJSON[title] = []
    # # groupJSON = {
    # #     title: subPages
    # # }
    # groupsJSON[title].append(subPages)



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

    title = cleanIterLinks(cleanText(links.text_content()))
    for link in links.iterlinks():
        groupURL = ROOTURL + link[2]

    subgruups = scrapeSubcategory(groupURL)

    group[title] = []
    group[title].append(subgruups)

    # rootPages.append(
    #     group)


#print(rootPages)


with open("test6.json", "w", encoding="utf8") as outfile:
    json.dump(group, outfile)
