#!/usr/bin/python3
import importlib.util


def main():
    spec = importlib.util.spec_from_file_location('hidden_4', 'hidden_4.pyc')
    content = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(content)
    for name in dir(content):
        if not name.startswith('__'):
            print(name)


if __name__ == '__main__':
    main()
