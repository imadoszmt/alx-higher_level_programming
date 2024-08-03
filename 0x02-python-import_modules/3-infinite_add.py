#!/usr/bin/python3
import sys


def main():
    adder = 0
    for arg in sys.argv[1:]:
        adder = adder + int(arg)

    print(adder)


if __name__ == "__main__":
    main()
