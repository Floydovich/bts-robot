from unittest import TestCase

from robot import Robot


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

    def test_can_find_link_on_page(self):
        self.robot.open_page(self.url)
        link_text = "Заңды тұлғаларға"

        found_link = self.robot.find_link(link_text)

        self.assertIn('<a', str(found_link))
        self.assertEqual(link_text, found_link.string)

    def test_can_download_file_from_link(self):
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2')

        file_link = self.robot.find_link('Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему')

        self.assertTrue(
            'http://astana.kgd.gov.kz/sites/default/files/u1323/kopiya_kopiya_4_rus_263_67_58.xlsx',
            file_link.string
        )
