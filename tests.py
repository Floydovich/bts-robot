from unittest import TestCase

from robot import Robot


class RobotBrowsePagesTest(TestCase):

    def setUp(self):
        self.url = 'https://nursultan.kgd.gov.kz/'
        self.robot = Robot()
        self.robot.open_page(self.url)

    def test_can_open_start_page(self):
        self.assertEqual(self.robot.current_page.status, 200)
        self.assertEqual(self.robot.current_page.url, self.url)

    def test_can_get_page_content(self):
        page_title = "Мемлекеттік Кірістер Департаменті"

        self.assertIn(page_title, self.robot.current_page.content)

    def test_can_find_link_on_page(self):
        link_text = "Заңды тұлғаларға"

        found_link = self.robot.find_link(link_text)

        self.assertIn('<a', str(found_link))
        self.assertEqual(link_text, found_link.text)
