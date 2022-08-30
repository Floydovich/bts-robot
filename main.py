from db import Database
from excel_reader import Reader
from sites import select_site
from webparser import WebParser


def main():
    url = select_site()

    parser = WebParser(url, 'ru')

    while True:
        text = input('Введите раздел который вы хотите найти: ')

        link = parser.open_link(text)

        if link is None:
            similar_link = parser.find_similar_links(text)
            print(f"{text} не найдено. Может вы имели ввиду: ")
            for link in similar_link:
                print(link.text)
            continue
        if '.xlsx' in link['href']:
            break

    rows = Reader('list.xlsx').all_rows()

    db = Database('companies.db')
    db.add_rows(rows)

    db.close()


if __name__ == '__main__':
    main()
