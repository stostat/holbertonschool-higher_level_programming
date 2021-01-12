#!/usr/bin/python3
"""Email posts from argv"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    values = {'email': email, }
    response = requests.post(url, data=values)
    print(response.text)
