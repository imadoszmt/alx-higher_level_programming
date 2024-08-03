#!/usr/bin/python3
import sys


def main():

    if len(sys.argv) == 1:
        print('0 arguments.')
    elif len(sys.argv) == 2:
        print('1 argument:')
        print(f'1: {sys.argv[1]}')
    else:
        print(f'{len(sys.argv) - 1} arguments:')
        for arg in sys.argv[1:]:
            print(f'{sys.argv.index(arg)}: {arg}')


if __name__ == "__main__":
    main()
