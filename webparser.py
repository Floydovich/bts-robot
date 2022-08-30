from difflib import SequenceMatcher

import requests
from bs4 import BeautifulSoup


class WebParser:
    current_page = None

    def __init__(self, base_url, language):
        self.base_url = base_url + language
        self.open_page(self.base_url)

    def open_page(self, url):
        response = requests.get(url)
        self.current_page = Page(response)

    def find_link(self, text):
        return self.current_page.html.find('a', string=text)

    def open_link(self, link_text):
        link = self.find_link(link_text)

        if link is None: return None

        if '.xlsx' in link['href']:
            self.save_file(link.string)
        else:
            self.open_link_href(link)

        return link

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        with open('list.xlsx', "wb") as f:
            f.write(response.content)

    def open_link_in_div(self, text, div):
        catmenu = self.current_page.html.select(f'div.{div}')
        for cat in catmenu:
            link = cat.find('a', string=text)
            if link:
                self.open_link_href(link)

    def open_link_href(self, link):
        next_page_url = link['href'][3:]  # убираем /ru из ссылок
        self.open_page(self.base_url + next_page_url)


class Page:
    def __init__(self, response):
        self.status = response.status_code
        self.url = response.url
        self.html = BeautifulSoup(response.text, 'html.parser')
