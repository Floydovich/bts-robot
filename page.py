import requests


class Page:
    def __init__(self, url):
        response = requests.get(url)
        self.status = response.status_code
        self.url = response.url
        self.content = response.text
