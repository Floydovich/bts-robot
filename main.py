import os.path

from db import Database
from excel_reader import Reader
from sites import SITES
from webparser import WebParser


categories = [
    "Реабилитация и банкротство",
    "год",
    "Информационные сообщения",
]

file_name = "Объявления о возбуждении дела о банкротстве и порядке заявления требовании кредиторами временному управляющему"

years = ['2018', '2019', '2020', '2021']


def main():
    db = Database('companies.db')

    for url in SITES:
        parser = WebParser(url, 'ru')

        for year in years:
            parser.open_link("Юридическим лицам")
            for category in categories:
                print(">> page=", parser.current_page.url)
                if "год" in category:
                    parser.find_link_in_content(f'{year} год')
                parser.find_link_in_content(category)

            parser.find_file_link(file_name)

            if os.path.exists('list.xlsx'):
                print("file is there")
                rows = Reader('list.xlsx').all_rows()
                for i, r in enumerate(rows[0]):
                    print(i, r)
                db.insert_rows(rows)
                os.remove('list.xlsx')

    db.close()


if __name__ == '__main__':
    main()
