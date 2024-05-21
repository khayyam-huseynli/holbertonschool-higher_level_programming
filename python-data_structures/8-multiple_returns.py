#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first_ch = sentence[0]
    else:
        first_ch = None
    return (length, first_ch)
