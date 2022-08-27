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

    def __init__(self, start_url):
        self.start_url = start_url

    def start(self):
        self.current_page = Page(self.start_url)


class RobotBrowsePagesTest(TestCase):

    def test_can_open_start_page(self):
        given_url = 'https://nursultan.kgd.gov.kz/'

        robot = Robot(start_url=given_url)
        robot.start()

        self.assertEqual(robot.current_page.status, 200)
        self.assertEqual(robot.current_page.url, given_url)

    def test_can_get_page_content(self):
        given_url = 'https://nursultan.kgd.gov.kz/'
        page_title = "Мемлекеттік Кірістер Департаменті"

        robot = Robot(start_url=given_url)
        robot.start()

        self.assertIn(page_title, robot.current_page.content)
