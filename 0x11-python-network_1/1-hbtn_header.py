#!/usr/bin/python3
"""request of sysargv"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request

    url = argv[1]
    with request.urlopen(url) as response:
        # print(response.info()
        print(response.headers['X-Request-Id'])
