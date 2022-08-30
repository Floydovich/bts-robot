import requests
from bs4 import BeautifulSoup


def is_xlsx_link(tag):
    return tag.has_attr('href') and '.xlsx' in tag['href']


class WebParser:
    current_page = None

    def __init__(self, base_url, language):
        self.base_url = base_url + language
        self.open_page(self.base_url)

    def open_page(self, url):
        response = requests.get(url)
        self.current_page = Page(response)

    def open_link(self, link_text):
        link = self.find_link(link_text)
        self.open_link_href(link)

    def find_link(self, text):
        return self.current_page.html.find('a', string=text)

    def find_link_in_content(self, text):
        content = self.current_page.html.select('div.catmenu')
        for element in content:
            link = element.find('a', string=text)
            if link:
                self.open_link_href(link)

    def open_link_href(self, link):
        next_page_url = link['href'][3:]  # убираем /ru из ссылок
        self.open_page(self.base_url + next_page_url)

    def save_file(self, link_text):
        link = self.find_link(link_text)
        response = requests.get(link['href'])
        with open('list.xlsx', "wb") as f:
            f.write(response.content)

    def find_file_link(self, text):
        print(">> current page", self.current_page.url)
        file_links = self.current_page.html.find_all(is_xlsx_link)
        print(file_links)
        for link in file_links:
            print(link)
            if link.string == text:
                print(">>>> link found")
                response = requests.get(link['href'])
                with open('list.xlsx', "wb") as f:
                    f.write(response.content)
                return link


class Page:
    def __init__(self, response):
        self.status = response.status_code
        self.url = response.url
        self.html = BeautifulSoup(response.text, 'html.parser')
