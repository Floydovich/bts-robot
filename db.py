import sqlite3

COLUMNS = ['number',
           'iin',
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

    def add_rows(self, rows):
        self.con.executemany(
            f"""
            insert into company({', '.join(COLUMNS)})
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows
        )

    def all(self):
        return self.table.execute('select * from company').fetchall()

    def close(self):
        self.con.close()
