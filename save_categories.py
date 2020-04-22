import requests
import json
import lxml.html
import re

ENDPOINT = "https://en.wikipedia.org/w/api.php"
REQUEST = "https://en.wikipedia.org/wiki/Category:Books_by_country"
ROOTURL = "https://en.wikipedia.org"

index = requests.get(REQUEST)

vulcan = lxml.html.fromstring(index.text)

indexPages = []


def cleanText(text):
    banana = re.sub("\W|books|[0-9]*", "", text)
    return banana

def cleanIterLinks(text):
    banana = re.sub("CP*F*$|PF*$", "", text)
    return banana

for groups in vulcan.xpath("//div[@class='mw-category-group']"):
    
    for links in groups.xpath("//div[@class='CategoryTreeItem']"):
        
        country = cleanIterLinks(cleanText(links.text_content()))
        for link in links.iterlinks():
            url = ROOTURL + link[2]
        
        page = {
            "country" : country,
            "url" : url
        }

        indexPages.append(page)


print(indexPages)

# result = requests.get(ENDPOINT, params=params)

# return result
# data = result.json()

with open("test0.json", "w", encoding="utf8") as outfile:
     json.dump(indexPages, outfile)
