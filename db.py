import sqlite3

EXAMPLE_COMPANY = ('120840008444',
                   'ТОО "Valio Bisness Stroy"',
                   '2121',
                   'г.Астана пр.Республики д. 60, каб. 405',
                   'СМЭС г.Астана',
                   '12 / 26 / 2017',
                   '12 / 26 / 2017',
                   'Камалатова Гулшат Камалатовна',
                   '1 / 3 / 2018',
                   '2 / 3 / 2018',
                   'г.Астана, пр.Абая д. 135 кв. 101',
                   '87752565566 gkk.81 @ mail.ru',
                   '1 / 3 / 2018')
COLUMNS = ['iin',
           'company_name',
           'registration_number',
           'company_address',
           'court_name',
           'initiation_date',
           'appointment_date',
           'pm_name',
           'deadline_from',
           'deadline_to',
           'claims_address',
           'contact_details',
           'posting_date',
           ]


class Database:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.table = self.con.execute(
            f"create table company({', '.join(COLUMNS)})"
        )

    def column_names(self):
        cursor = self.con.execute('select * from company')
        return [description[0] for description in cursor.description]

    def add_rows(self, companies):
        self.con.executemany(
            f"""
            insert into company({', '.join(COLUMNS)})
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            companies
        )

    def all(self):
        return self.table.execute('select * from company').fetchall()
