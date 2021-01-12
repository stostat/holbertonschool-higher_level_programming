#!/usr/bin/python3
"""Error code posts"""


if __name__ == "__main__":
    from sys import argv
    from urllib import error
    from urllib import request

    try:
        url = argv[1]
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
