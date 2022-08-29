from unittest import TestCase

from db import Database
from tests.examples import EXAMPLE_COMPANY


class DBManagerTest(TestCase):

    def setUp(self):
        self.db = Database(':memory:')

    def test_table_has_correct_columns(self):
        columns = self.db.column_names()

        self.assertEqual(14, len(columns))

    def test_can_add_company(self):
        companies = [EXAMPLE_COMPANY]

        self.db.add_rows(companies)

        all_rows = self.db.all()
        self.assertEqual(1, len(all_rows))
        self.assertEqual(tuple(companies[0]), all_rows[0])

    def test_can_add_many_companies(self):
        companies = [EXAMPLE_COMPANY for _ in range(10)]

        self.db.add_rows(companies)

        all_rows = self.db.all()
        self.assertEqual(len(companies), len(all_rows))
