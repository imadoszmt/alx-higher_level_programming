#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != "":
        length = len(sentence)
        first_chr = sentence[0]
        return (length, first_chr)
    else:
        return (0, None)
