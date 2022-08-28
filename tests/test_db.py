from unittest import TestCase
import sqlite3


COLUMNS = [
    'id',
    'iin',
    'company_name',
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

    def get_table_columns(self):
        cursor = self.con.execute('select * from company')
        return [description[0] for description in cursor.description]


class DBManagerTest(TestCase):

    def setUp(self):
        self.db = Database(':memory:')

    def test_table_has_correct_columns(self):
        columns = self.db.get_table_columns()

        self.assertEqual(13, len(columns))
