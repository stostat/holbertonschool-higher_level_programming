#!/usr/bin/python3
"""Takes requests returns header"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
