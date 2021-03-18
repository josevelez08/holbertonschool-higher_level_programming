#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join(x for x in str if str.index(x) != n)
