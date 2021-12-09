import sqlite3


class EmployeeDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, mobile TEXT, email TEXT)")
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM employee")
        employees = self.cur.fetchall()
        return employees

    def search(self, name="", mobile="", email=""):
        self.cur.execute(
            "SELECT * FROM employee WHERE name=? OR mobile=? OR email=?", (name, mobile, email))
        employees = self.cur.fetchall()
        return employees

    def insert(self, name, mobile, email):
        self.cur.execute("INSERT INTO employee VALUES (NULL, ?, ?, ?)",
                         (name, mobile, email))
        self.conn.commit()

    def update(self, id, name, mobile, email):
        self.cur.execute("UPDATE employee SET name=?, mobile=?, email=? WHERE id=?",
                         (name, mobile, email, id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM employee WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()