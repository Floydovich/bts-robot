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

    for step in steps:
        print(step)
        robot.open_page_from_link(step)
        print(robot.current_page.url)


if __name__ == '__main__':
    main()
