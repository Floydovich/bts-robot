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
        self.create_table()

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
        self.con.commit()

    def all(self):
        cursor = self.con.cursor()
        rows = cursor.execute('select * from company').fetchall()
        return rows

    def close(self):
        self.con.close()

    def create_table(self):
        cursor = self.con.cursor()
        cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='company' ''')
        if cursor.fetchone()[0] == 1:
            pass
        else:
            self.con.execute(
                f"create table company({', '.join(COLUMNS)})"
            )
