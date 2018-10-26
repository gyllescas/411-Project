import requests

beer_url = "https://api.punkapi.com/v2/beers/random"

def get_beer():
    r = requests.get(url=beer_url, params={}).json() 
    return "Recommended beer: {}".format(r[0]['name'])
