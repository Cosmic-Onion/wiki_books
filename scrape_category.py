import requests
import json
import lxml.html

ENDPOINT = "https://en.wikipedia.org/w/api.php"


index = requests.get("https://en.wikipedia.org/wiki/Category:Books_by_country")

vulcan = lxml.html.fromstring(index.text)

indexPages = []


for groups in vulcan.xpath("//div[@class='mw-category-group']"):
    innerArray = []
    for links in groups.xpath("//div[@class='CategoryTreeItem']"):
        innerArray.append(links.text_content())
        for link in links.iterlinks():
            innerArray.append(link[2])
    indexPages.append(innerArray)

print(indexPages)

# result = requests.get(ENDPOINT, params=params)

# return result
# data = result.json()

# with open("test0.json", "w") as outfile:
#     json.dump(data, outfile)
