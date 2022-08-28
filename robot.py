import requests
from bs4 import BeautifulSoup

from page import Page


class Robot:
    current_page = None

    def open_page(self, url):
        self.current_page = Page(url)

    def find_link(self, text):
        soup = BeautifulSoup(self.current_page.content, 'html.parser')
        link = soup.find('a', string=text)
        return link

    def get_file(self, file_link):
        return requests.get(file_link['href'])
