import requests
from urllib.parse import quote


def fetch(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print('Unable to connect to server')
        print(e)


def url_safe(raw):
    clean = raw.replace(',', ' ').replace('  ', ' ')
    return quote(clean)
