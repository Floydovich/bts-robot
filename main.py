from db import Database
from excel_reader import Reader
from sites import SITES
from webparser import WebParser


categories = [
    "Реабилитация и банкротство",
    "год",
    "Информационное сообщение",
    "Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему"
]


def main():
    db = Database('companies.db')

    for url in SITES:
        parser = WebParser(url, 'ru')

        for year in ['2018', '2019', '2020', '2021']:
            parser.open_link("Юридическим лицам")
            print(">> page=", parser.current_page.url)
            for category in categories:
                if "год" in category:
                    parser.find_link_in_content(f'{year} год')
                parser.find_link_in_content(category)
                print('<< page=', parser.current_page.url)

            rows = Reader('list.xlsx').all_rows()

            db.insert_rows(rows)

    db.close()


if __name__ == '__main__':
    main()
