#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    oper = {'+': add, '-': sub, '*': mul, '/': div}

    try:
        check = len(sys.argv) == 4
        if check is not True:
            raise ValueError
    except ValueError:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    try:
        ch = sys.argv[2] in oper.keys()
        if ch is not True:
            raise ValueError
    except ValueError:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    result = oper[sys.argv[2]](int((sys.argv[1])), int(sys.argv[3]))
    print(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}')
