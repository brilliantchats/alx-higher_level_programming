#!/usr/bin/python3
"""
Connects to a database using the MySQLdb api
"""
import sys
import MySQLdb


def main():
    """Prints the rows from a database"""
    if len(sys.argv) == 4:
        db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
