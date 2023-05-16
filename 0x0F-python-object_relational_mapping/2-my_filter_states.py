#!/usr/bin/python3
""" A python script that takes an argument and displays all values in the
`states` table of `hbtn_0e_0_usa` where name matches the argument.
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
        'SELECT * FROM states WHERE name = BINARY "{}";'.format(sys.argv[4])
    )

    # fetch all rows
    rows = cur.fetchall()

    # print records
    for row in rows:
        print(row)
