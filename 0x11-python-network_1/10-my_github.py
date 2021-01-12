#!/usr/bin/python3
""" github api"""


import sys
import requests

if __name__ == "__main__":
    try:
        usr = sys.argv[1]
        psw = sys.argv[2]
        url = "https://api.github.com/user"
        res = requests.get(url, auth=(usr, psw))
        print(res.json()['id'])
    except:
        print("None")
