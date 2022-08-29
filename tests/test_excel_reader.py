from unittest import TestCase

from examples import EXAMPLE_COMPANY
from excel_reader import Reader


class ExcelReaderTest(TestCase):

    def setUp(self) -> None:
        path = "list.xlsx"
        self.reader = Reader(path)

    def test_can_get_all_rows(self):
        rows = self.reader.all()

        self.assertEqual(712, len(rows))
        self.assertEqual(14, len(rows[0]))
        self.assertEqual(14, len(rows[-1]))

    def test_row_has_text_values(self):
        rows = self.reader.all()

        first_row = rows[0]
        last_row = rows[-1]

        self.assertEqual('ТОО "Valio Bisness Stroy"', first_row[2])
        self.assertEqual('ТОО "TEMIR ZHOL  ELECTRIFICATION" (ТЕМИР ЖОЛ ЭЛЕКТРИФИКЕЙШН)',
                         last_row[2])
