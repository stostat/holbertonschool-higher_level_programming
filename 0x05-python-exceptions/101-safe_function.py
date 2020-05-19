#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as te:
        sys.stderr.write('Exception: ' + str(te) + '\n')
        return None
