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

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        open('list.xlsx', "wb").write(response.content)
