import requests
from flask import Flask
import json

ENDPOINT = "https://en.wikipedia.org/w/api.php"

APP = Flask(__name__)

@APP.route("/", methods=["GET"])
def get_json():

    params = {
        "action": "query",
        "Category":"Books_by_country",
        "prop": "pageimages|description|info",
        "format": "json",
    }

    result = requests.get(ENDPOINT, params=params)

    return result
    # data = result.json()

    # with open("test0.json", "w") as outfile:
    #     json.dump(data, outfile)


if __name__ == '__main__':
    APP.run(debug=True)