#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    # Iterate over element in the list
    for element in my_list:
        # Check the element matches the search element
        if element == search:
            # Replace element with the new element
            new_list.append(replace)
        else:
            new_list.append(element)

    return new_list
