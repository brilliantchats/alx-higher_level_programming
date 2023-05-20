#!/usr/bin/python3
"""
List all entries in a table whose name match a given name
"""
import sys
import MySQLdb


def main():
    if (len(sys.argv) == 5):
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id".format(
                sys.argv[4])
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)


if __name__ == '__main__':
    main()
