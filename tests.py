from unittest import TestCase

import requests


class Page:
    def __init__(self, url):
        response = requests.get(url)
        self.status = response.status_code
        self.url = response.url.rstrip('kk')
        self.content = response.text


class Robot:
    current_page = None

    def open_page(self, url):
        self.current_page = Page(url)


class RobotBrowsePagesTest(TestCase):

    def setUp(self):
        self.url = 'https://nursultan.kgd.gov.kz/'
        self.robot = Robot()

    def test_can_open_start_page(self):
        self.robot.open_page(self.url)

        self.assertEqual(self.robot.current_page.status, 200)
        self.assertEqual(self.robot.current_page.url, self.url)

    def test_can_get_page_content(self):
        page_title = "Мемлекеттік Кірістер Департаменті"

        self.robot.open_page(self.url)

        self.assertIn(page_title, self.robot.current_page.content)
