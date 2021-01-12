#!/usr/bin/python3
"""Request with error."""


if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        url = argv[1]
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as err:
        print('Error code:', err.response.status_code)
