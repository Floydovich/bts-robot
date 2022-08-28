import requests
from bs4 import BeautifulSoup

from page import Page


class Robot:
    current_page = None

    def __init__(self, base_url, language):
        self.base_url = base_url + language
        self.open_page(self.base_url)

    def open_page(self, url):
        response = requests.get(url)
        self.current_page = Page(response)

    def find_link(self, text):
        soup = BeautifulSoup(self.current_page.content, 'html.parser')
        return soup.find('a', string=text)

    def open_page_from_link(self, link_text):
        link = self.find_link(link_text)
        next_page_url = link['href'][3:]  # убираем /ru из ссылок
        self.open_page(self.base_url + next_page_url)

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        with open('list.xlsx', "wb") as f:
            f.write(response.content)
