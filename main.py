import os.path

from db import Database
from excel_reader import Reader
from sites import SITES
from webparser import WebParser


years = ['2018', '2019', '2020', '2021']

categories_1 = [
    "Реабилитация и банкротство",
    "год",
    "Информационное сообщение",
]
categories_2 = [
    "Реабилитация и банкротство",
    "год",
    "Информационные сообщения",
]

file_name = "Объявления о возбуждении дела о банкротстве и порядке заявления требовании кредиторами временному управляющему"
file_name_nbsp = "Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему"

def main():
    db = Database('companies.db')

    for url in SITES:
        parser = WebParser(url, 'ru')

        if url == SITES[0]:
            categories = categories_1
        else:
            categories = categories_2

        for year in years:
            parser.open_link("Юридическим лицам")
            for category in categories:
                if "год" in category:
                    parser.find_link_in_content(f'{year} год')
                parser.find_link_in_content(category)

            file = parser.find_file_link(file_name)
            if file is None:
                parser.find_file_link(file_name_nbsp)

            if os.path.exists('list.xlsx'):
                rows = Reader('list.xlsx').all_rows()
                db.insert_rows(rows)
                os.remove('list.xlsx')

    db.close()


if __name__ == '__main__':
    main()
