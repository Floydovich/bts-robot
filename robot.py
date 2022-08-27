from bs4 import BeautifulSoup

from page import Page


class Robot:
    current_page = None

    def open_page(self, url):
        self.current_page = Page(url)

    def find_link(self, text):
        soup = BeautifulSoup(self.current_page.content)
        link = soup.find('a', text=text)
        return link
