#!/usr/bin/env python3
def no_c(my_string):
    result_str = "" 
    for i in my_string:
        if i != "c" and i != "C":
            result_str = result_str + i 
    return result_str