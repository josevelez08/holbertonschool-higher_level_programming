#!/usr/bin/python3
"""
Module select the name that match with a argument
"""

import MySQLdb
import sys
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3],
                                charset="utf8")
    searchstring = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='%s'" % (searchstring,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
