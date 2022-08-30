SITES = ['http://nursultan.kgd.gov.kz/',
         'http://almaty.kgd.gov.kz/',
         'http://shymkent.kgd.gov.kz/',
         'http://akm.kgd.gov.kz/',
         'http://akb.kgd.gov.kz/',
         'http://alm.kgd.gov.kz/',
         'http://atr.kgd.gov.kz/',
         'http://vko.kgd.gov.kz/',
         'http://zhmb.kgd.gov.kz/',
         'http://zko.kgd.gov.kz/',
         'http://krg.kgd.gov.kz/',
         'http://kst.kgd.gov.kz/',
         'http://kzl.kgd.gov.kz/',
         'http://mng.kgd.gov.kz/',
         'http://pvl.kgd.gov.kz/',
         'http://sko.kgd.gov.kz/',
         'http://trk.kgd.gov.kz/']


def select_site():
    for i, site in enumerate(SITES):
        print(i + 1, '-', site)

    while True:
        try:
            site_index = int(input("Выберите номер сайта: "))
            if site_index not in range(1, len(SITES) + 1):
                print(f"Пожалуйста введите число от 1 до {len(SITES)}")
                continue
            return SITES[site_index - 1]
        except ValueError:
            print("Номер сайта должен быть цифрой")
            continue
