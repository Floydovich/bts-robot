from unittest import TestCase
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

    def get_column_names(self):
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


class DBManagerTest(TestCase):

    def setUp(self):
        self.db = Database(':memory:')

    def test_table_has_correct_columns(self):
        columns = self.db.get_column_names()

        self.assertEqual(13, len(columns))

    def test_can_add_company(self):
        companies = [EXAMPLE_COMPANY]

        self.db.add_rows(companies)

        all_rows = self.db.table.execute('select * from company').fetchall()
        self.assertEqual(1, len(all_rows))
        self.assertEqual(companies[0], all_rows[0])

    def test_can_add_many_companies(self):
        companies = [EXAMPLE_COMPANY for i in range(10)]

        self.db.add_rows(companies)

        all_rows = self.db.table.execute('select * from company').fetchall()
        self.assertEqual(len(companies), len(all_rows))
