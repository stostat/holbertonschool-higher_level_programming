#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print(i - 1, "arguments.")
    elif i == 2:
        print(i - 1, "argument:")
    else:
        print(i - 1, "arguments:")
    for j in range(1, i):
        print("{}: {}".format(j, sys.argv[j]))
