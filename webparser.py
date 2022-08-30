from difflib import SequenceMatcher

import requests

from page import Page


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
            next_page_url = link['href'][3:]  # убираем /ru из ссылок
            self.open_page(self.base_url + next_page_url)

        return link

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        with open('list.xlsx', "wb") as f:
            f.write(response.content)

    def find_similar_links(self, searched_text):
        all_links = self.current_page.html.find_all(lambda a: a.has_attr('href'))
        similar_links = []
        for link in all_links:
            ratio = SequenceMatcher(None, searched_text, link.text).ratio()
            if ratio >= 0.4:
                similar_links.append(link)
        return similar_links
