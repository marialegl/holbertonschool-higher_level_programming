#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections.
"""


from sys import argv
import MySQLdb

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(host='localhost', user=mysql_username,
                         passwd=mysql_password, db=database_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE name = %s",
                (state_name_searched,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
