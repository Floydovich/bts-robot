import os.path

from db import Database
from excel_reader import Reader
from robot import Robot


def main():
    robot = Robot('https://nursultan.kgd.gov.kz/', 'ru')

    steps = [
        "Юридическим лицам",
        "Реабилитация и банкротство",
        "2018 год",
        "Информационное сообщение",
        "Объявления о возбуждении дела о банкротстве  и порядке заявления требований кредиторами временному управляющему"
    ]

    while True:
        text = input('Введите раздел который вы хотите найти')

        link = robot.open_link(text)

        if link is None:
            continue

        if os.path.exists('list.xlsx'):
            break

    rows = Reader('list.xlsx').all()

    db = Database('companies.db')
    db.add_rows(rows)

    print(db.all())


if __name__ == '__main__':
    main()
