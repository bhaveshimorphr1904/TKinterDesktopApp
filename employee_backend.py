import sqlite3


def connect():
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, mobile TEXT, email TEXT)")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    conn.close()
    return employees


def search(name="", mobile="", email=""):
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM employee WHERE name=? OR mobile=? OR email=?", (name, mobile, email))
    employees = cur.fetchall()
    conn.close()
    return employees


def insert(name, mobile, email):
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL, ?, ?, ?)",
                (name, mobile, email))
    conn.commit()
    conn.close()


def update(id, name, mobile, email):
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute("UPDATE employee SET name=?, mobile=?, email=? WHERE id=?",
                (name, mobile, email, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("employee.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    conn.commit()
    conn.close()
