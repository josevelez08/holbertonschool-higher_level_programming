#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return 0
    elif idx > len(my_list):
        return 0
    else:
        for i in my_list:
            if i == idx:
                return my_list[i]
