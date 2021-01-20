#!/usr/bin/python3
def lookup(obj):
    myList = []
    for i in dir(obj):
        myList.append(i)
    return myList
