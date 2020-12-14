#!/usr/bin/python3
"""Filter by input"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    size = len(sys.argv) - 1
    db = None
    if size == 4:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY id"\
                " ASC".format(sys.argv[4])
        res = cur.execute(query)
        results = cur.fetchall()
        for result in results:
            print(result)
        cur.close()
        db.close()