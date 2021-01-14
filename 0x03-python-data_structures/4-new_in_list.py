#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Newlist = list.copy(my_list)
    if idx < 0 or idx > len(my_list):
        return Newlist
    else:
        for i in my_list:
            if idx == i - 1:
                Newlist[i - 1] = element
    return Newlist
