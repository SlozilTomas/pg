import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(prefix):
    # stahneme url + prefix
    url_prefix = url + prefix
    response = requests.get(url_prefix)
    # kontrola navratove hodnoty
    if response.status_code != 200:
        print("chyba")
        return []
    # stahneme json
    data = response.json()

    result = []

    # vytahneme nazvy brandu ["brands"]["name"]
    for brand in data["brands"]:
        result.append(brand["name"])
    return result


if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

    #pro prefix "ni" vypise Nissan a Nio