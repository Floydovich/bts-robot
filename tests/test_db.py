from unittest import TestCase
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from pathlib import Path


class DBManager:

    def __init__(self):
        self.engine = create_engine('sqlite:///../sqlite3.db')
        self.engine.connect()

    def create_table(self, param):
        meta = MetaData()
        Table(
            'companies', meta,
            Column('id', Integer, primary_key=True),
            Column('iin', Integer),
            Column('name', String),
            Column('registration_number', String),
        )
        meta.create_all(self.engine)


class DBManagerTest(TestCase):

    def test_db_can_create_table(self):
        db = DBManager()
        db.create_table('companies')

        self.assertTrue(db.engine.has_table('companies'))
