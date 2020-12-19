#!/usr/bin/python3
"""Select states module"""


def esc_chars(string):
    """ function to escape characers use in sql"""
    esc_array = ['\\x00', '\\n', '\\r', '\\', '\'', '"', '\\x1a', '%', '_']
    if type(string) is str:
        for element in esc_array:
            if element in string:
                string = string.replace(element, "\\" + element)
    return stringcode


if __name__ == "__main__":
    import MySQLdb
    import sys
    size = len(sys.argv) - 1
    db = None
    if size == 4:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        var_input = esc_chars(sys.argv[4])
        query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id "\
                "ASC".format(var_input)
        res = cur.execute(query)
        results = cur.fetchall()
        for result in results:
            print(result)
        cur.close()
        db.close()
