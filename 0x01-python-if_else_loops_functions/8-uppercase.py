#!/usr/bin/python3
def uppercase(str):
    string = str
    output_str = "" 
    for character in string:
        if 'a' <= character <= 'z':
            uppercase_ascii = ord(character) - 32
            output_str += chr(uppercase_ascii)
        else:
            output_str += character
    print(output_str)
