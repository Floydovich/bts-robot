from robot import Robot


def main():
    robot = Robot('https://nursultan.kgd.gov.kz/', 'ru')

    section = input("Введите название нужного раздела сайта: ")

    page = robot.find_link(section)
    print(page)


if __name__ == '__main__':
    main()
