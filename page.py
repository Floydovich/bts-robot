from bs4 import BeautifulSoup


class Page:
    def __init__(self, response):
        self.status = response.status_code
        self.url = response.url
        self.html = BeautifulSoup(response.text, 'html.parser')
