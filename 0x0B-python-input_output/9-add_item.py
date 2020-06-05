#!/usr/bin/python3
"""Script that adds item to json file."""

import sys
import json
import os.path as check

save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
load_from_json_f = __import__('8-load_from_json_file.py').load_from_json_file

file = "add_item.json"
if check.exists(file):
    list_args = load_from_json_f(file)
else:
    list_args = []

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        list_args.append(i)

save_to_json_file(list_args, file)
