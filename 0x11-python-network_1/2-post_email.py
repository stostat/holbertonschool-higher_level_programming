#!/usr/bin/python3
"""Request including email address"""


if __name__ == "__main__":
    from sys import argv
    from urllib import parse
    from urllib import request

    url = argv[1]
    email = argv[2]
    values = {'email': email, }
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
