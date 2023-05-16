#!/usr/bin/python3
"""A script that takes in arguments and displays all values in the `states`
table of `hbtn_0e_0_usa` where name matches the arguments. But this time it's
safe from MySQL Injections.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    val = argv[4].split()[0]
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name LIKE BINARY "{}"\
        ORDER BY states.id ASC'.format(val)
    )
    """
    --> The above syntax works the same as follows:
    SELECT * FROM states WHERE name LIKE
    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    """
    rows = cur.fetchall()

    for row in rows:
        print(row)
