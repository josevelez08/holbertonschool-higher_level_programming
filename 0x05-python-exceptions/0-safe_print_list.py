#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        myString = ""
        while i < x:
            myString += str(my_list[i])
            i = i+1
        print(myString)
    except:
        print(myString)
    return(i)
