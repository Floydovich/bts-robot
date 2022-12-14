import os.path
from unittest import TestCase
from difflib import SequenceMatcher

from webparser import WebParser


class WebParserTest(TestCase):

    def setUp(self):
        self.base_url = 'https://nursultan.kgd.gov.kz/'
        self.robot = WebParser(self.base_url, 'ru')

    def test_can_open_home_page(self):
        self.assertEqual(self.robot.current_page.status, 200)
        self.assertIn(self.base_url, self.robot.current_page.url)

    def test_page_language_is_russian(self):
        wanted_language = 'ru'

        self.robot = WebParser(self.base_url, wanted_language)

        self.assertEqual(wanted_language, self.robot.current_page.url[-2:])

    def test_can_find_link_on_page(self):
        link_text = "Юридическим лицам"

        found_link = self.robot.find_link(link_text)

        self.assertIn('<a', str(found_link))
        self.assertEqual(link_text, found_link.string)

    def test_can_move_to_next_page_from_link(self):
        expected_url = 'https://nursultan.kgd.gov.kz/ru/depsection/yuridicheskim-licam'
        link_text = "Юридическим лицам"

        self.robot.open_link(link_text)

        self.assertEqual(self.robot.current_page.status, 200)
        self.assertIn(expected_url, self.robot.current_page.url)

    def test_can_find_file_link(self):
        file_name = 'kopiya_kopiya_4_rus_263_67_58.xlsx'
        link_string = 'Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему'
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2')

        file_link = self.robot.find_link(link_string)

        self.assertIn(file_name, file_link['href'])

    def test_can_save_file_from_page(self):
        file_name = 'list.xlsx'
        link_string = 'Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему'
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2')

        self.robot.save_file(link_string)

        self.assertTrue(os.path.exists(file_name))

    def test_can_save_file_if_opens_file_link(self):
        file_name = 'list.xlsx'
        link_string = 'Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему'
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2')

        self.robot.open_link(link_string)

        self.assertTrue(os.path.exists(file_name))

    def test_parser_can_find_link_in_content(self):
        text = 'Информационное сообщение'
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/depsection/2018-god')

        self.robot.find_link_in_content(text)

        self.assertEqual(200, self.robot.current_page.status)
        self.assertEqual('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2',
                         self.robot.current_page.url)

    def test_can_find_link_with_incorrect_ending(self):
        text = 'Информационные сообщения'
        self.robot.open_page('https://nursultan.kgd.gov.kz/ru/depsection/2018-god')

        self.robot.find_link_in_content(text)

        self.assertEqual(200, self.robot.current_page.status)
        self.assertEqual('https://nursultan.kgd.gov.kz/ru/content/informacionnoe-soobshchenie-2',
                         self.robot.current_page.url)

    def test_can_find_only_file_links(self):
        text = "Объявления о возбуждении дела о банкротстве и порядке заявления требовании кредиторами временному управляющему"
        self.robot.open_page('https://almaty.kgd.gov.kz/ru/content/informacionnye-soobshcheniya-3-3')

        link = self.robot.find_file_link(text)

        self.assertEqual(text, link.string)