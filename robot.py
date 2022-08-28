import requests
from bs4 import BeautifulSoup

from page import Page


class Robot:
    current_page = None

    def __init__(self, base_url):
        self.base_url = base_url
        self.open_page(base_url)

    def open_page(self, url):
        self.current_page = Page(url)

    def find_link(self, text):
        soup = BeautifulSoup(self.current_page.content, 'html.parser')
        return soup.find('a', string=text)

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        with open('list.xlsx', "wb") as f:
            f.write(response.content)

    def open_page_from_link(self, link_text):
        link = self.find_link(link_text)
        self.open_page(self.base_url + link['href'].lstrip('/'))
