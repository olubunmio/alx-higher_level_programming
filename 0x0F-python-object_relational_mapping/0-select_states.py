#!/usr/bin/python3
""" A python script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to database
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")

    cur = conn.cursor()

    # query database
    cur.execute("SELECT * from states ORDER BY states.id ASC")

    # fetch stored data
    rows = cur.fetchall()

    # Print data row by row
    for row in rows:
        print(row)
