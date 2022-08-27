from unittest import TestCase

import requests


class Page:
    def __init__(self, url):
        response = requests.get(url)
        self.status = response.status_code
        self.url = response.url.rstrip('kk')


class Robot:
    def start(self, url):
        return Page(url)


class RobotBrowsePagesTest(TestCase):

    def test_can_open_start_page(self):
        given_url = 'https://nursultan.kgd.gov.kz/'
        robot = Robot()
        current_page = robot.start(given_url)
        self.assertEqual(current_page.status, 200)
        self.assertEqual(current_page.url, given_url)
