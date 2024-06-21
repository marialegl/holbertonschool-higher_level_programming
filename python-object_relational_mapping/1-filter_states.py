#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    db = MySQLdb.connect(host='localhost', user=mysql_username,
                         passwd=mysql_password, db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM `states` WHERE name LIKE BINARY 'N%' ORDER BY `id`")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
