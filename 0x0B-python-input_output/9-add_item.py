#!/usr/bin/python3
"""Script that adds item to json file."""
import sys


save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
load_from_json_f = __import__('8-load_from_json_file.py').load_from_json_file

file = "add_item.json"
try:
    pl = load_from_json_f(file)
except Exception:
    pl = []
finally:
    for i in sys.argv[1:]:
        pl.append(i)
    save_to_json_file(pl, file)
