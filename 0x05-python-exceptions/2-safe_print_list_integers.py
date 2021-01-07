#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    while i < x:
        try:
            "{:d}".format(my_list[i])
            print(my_list[i], end="")
            j = j + 1
        except(TypeError, ValueError):
            pass
        i = i + 1
    print("")
    return(j)
