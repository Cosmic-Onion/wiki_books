import requests
import json

ENDPOINT = "http://libgen.org/json.php"

req = requests.Session()

params = {
    "action" : "parse",
    "page" : "Dollie_Radford",
    "prop"   : "wikitext|sections",
    "format" : "json"
}

jsonReq = req.get(ENDPOINT, params=params).json()

with open("./json/api3.json","w") as outfile:
    json.dump(jsonReq,outfile)

print(jsonReq)