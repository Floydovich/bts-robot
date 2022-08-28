from unittest import TestCase
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date


class DBManager:

    def __init__(self):
        self.engine = create_engine('sqlite:///../sqlite3.db')
        self.engine.connect()
        self.meta = MetaData()
        self.table = None

    def create_table(self, table_name):
        self.table = Table(
            table_name, self.meta,
            Column('id', Integer, primary_key=True),
            Column('iin', Integer),
            Column('company_name', String),
            Column('compnay_address', String),
            Column('court_name', String),
            Column('initiation_date', Date),
            Column('appointment_date', Date),
            Column('pm_name', String),
            Column('deadline_from', Date),
            Column('deadline_to', String),
            Column('claims_address', String),
            Column('contact_details', String),
            Column('posting_date', Date),
        )
        self.meta.create_all(self.engine)


class DBManagerTest(TestCase):

    def setUp(self):
        self.db = DBManager()

    def test_db_can_create_table(self):
        self.assertIsNone(self.db.table)
        table_name = 'companies'

        self.db.create_table(table_name)

        self.assertTrue(self.db.engine.has_table('companies'))

    def test_table_has_right_amount_of_columns(self):
        table_name = 'companies'

        self.db.create_table(table_name)

        self.assertEqual(13, len(self.db.table.columns.keys()))
        self.assertIn('id', self.db.table.columns.keys())
        self.assertIn('iin', self.db.table.columns.keys())

    def tearDown(self):
        self.db.meta.drop_all(self.db.engine)
