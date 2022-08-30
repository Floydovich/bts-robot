from db import Database
from excel_reader import Reader
from sites import SITES
from webparser import WebParser


STEPS = [
    "Юридическим лицам",
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
            for step in STEPS:
                if "год" in step:
                    parser.open_link(f'{year} год')
                parser.open_link(step)

            rows = Reader('list.xlsx').all_rows()

            db.insert_rows(rows)

    db.close()


if __name__ == '__main__':
    main()
