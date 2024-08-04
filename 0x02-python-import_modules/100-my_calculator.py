#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():

    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print(f'{a} + {b} = {add(a, b)}')
        elif sys.argv[2] == '-':
            print(f'{a} - {b} = {sub(a, b)}')
        elif sys.argv[2] == '*':
            print(f'{a} * {b} = {mul(a, b)}')
        elif sys.argv[2] == '/':
            print(f'{a} / {b} = {div(a, b)}')
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
