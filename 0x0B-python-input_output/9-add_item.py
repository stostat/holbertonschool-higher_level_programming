#!/usr/bin/python3
"""Script to adds args to Python list."""
import sys

load = __import__('8-load_from_json_file').load_from_json_file
save = __import__('7-save_to_json_file').save_to_json_file

filename = 'add_item.json'
try:
    py_list = load(filename)
except Exception:
    py_l = []
finally:
    for i in sys.argv[1:]:
        py_l.append(i)
    save(py_list, filename)
