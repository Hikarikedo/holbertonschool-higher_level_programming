#!/usr/bin/python3
"""
Return matching states
parameters given to script: username, password, database, state to match
"""

from sys import argv
import MySQLdb


if __name__ == '__main__':

    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
        '{}' ORDER BY states.id".format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
