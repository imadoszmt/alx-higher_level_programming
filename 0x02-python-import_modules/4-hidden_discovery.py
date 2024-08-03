#!/usr/bin/python3
import imp


def main():
    with open('hidden_4.pyc', 'rb') as f:
        content = imp.load_compiled('hidden_4', 'hidden_4.pyc', f)
    for name in dir(content):
        if not name.startswith('__'):
            print(name)


if __name__ == '__main__':
     main()
