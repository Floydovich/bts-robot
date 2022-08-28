from unittest import TestCase
from sqlalchemy import create_engine
from pathlib import Path


class DBManagerTest(TestCase):

    def test_create_db(self):
        my_file = Path("../sqlite3.db")
        engine = create_engine('sqlite:///../sqlite3.db')
        engine.connect()

        self.assertTrue(my_file.is_file())
