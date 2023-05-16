#!/usr/bin/python3
""" A python script that lists all states with a name starting with `N`
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'\
        ORDER BY states.id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
