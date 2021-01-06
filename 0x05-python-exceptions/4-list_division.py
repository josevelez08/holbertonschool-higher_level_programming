#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    my_string = "["
    while i < list_length:
        try:
            c = my_list_1[i] / my_list_2[i]
            i = i + 1
            my_string += str(c)
            if i != list_length:
                my_string += str(", ")
        except ZeroDivisionError:
            print("division by {}".format(0))
            my_string += str(0)
            my_string += str(", ")
            i = i + 1
        except TypeError:
            my_string += str(0)
            my_string += str(", ")
            print("wrong type")
            i = i + 1
        except IndexError:
            my_string += str(0)
            print("out of range")
            i = i + 1
    my_string += str("]")
    return(my_string)
