from robot import Robot


def main():
    robot = Robot('https://nursultan.kgd.gov.kz/', 'ru')

    section = select_section(robot.main_menu())
    print(section)


def select_section(menu):
    for i, section_index in enumerate(menu, 1):
        print(i, section_index)
    while True:
        try:
            section_index = int(input("Выберите раздел сайта: "))
            if section_index in range(len(menu)):
                break
        except ValueError:
            print("Пожалуйста, введите число")

    return menu[section_index - 1]


if __name__ == '__main__':
    main()
