import os.path

from db import Database
from excel_reader import Reader
from webparser import WebParser


def main():
    robot = WebParser('https://nursultan.kgd.gov.kz/', 'ru')

    steps = [
        "Юридическим лицам",
        "Реабилитация и банкротство",
        "2018 год",
        "Информационное сообщение",
        "Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему"
    ]

    while True:
        text = input('Введите раздел который вы хотите найти: ')

        link = robot.open_link(text)

        if link is None:
            similar_link = robot.find_similar_links(text)
            print(f"{text} не найдено. Может вы имели ввиду: ")
            for link in similar_link:
                print(link.text)
            continue
        if '.xlsx' in link['href']:
            break

    rows = Reader('list.xlsx').all()

    db = Database('companies.db')
    db.add_rows(rows)

    db.close()


if __name__ == '__main__':
    main()
