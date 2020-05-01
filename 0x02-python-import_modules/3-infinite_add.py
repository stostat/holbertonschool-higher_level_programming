#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    sum = 0
    if i == 1:
        print(i - 1)
    elif i == 2:
        print("{}".format(sys.argv[1]))
    else:
        for j in range(1, i):
            num = int(sys.argv[j])
            sum = sum + num
        print(sum)
