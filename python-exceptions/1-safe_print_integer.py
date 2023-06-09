#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if count < x:
                print("{:d}".format(item), end="")
                count += 1
        print()
        return count
    except TypeError:
        print("An error occurred while printing the list.")
        return count
