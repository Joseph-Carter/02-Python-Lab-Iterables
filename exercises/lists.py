# Exercise 1: Reverse a list in place.
def reverse_list(lst):
    return lst.reverse()
    pass

# Exercise 2: Find all unique elements in a list.
def find_unique_elements(lst):
    unique_elements = list(set(lst))
    return unique_elements
    pass

# Exercise 3: Rotate a list by n positions.
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
    pass

# Exercise 4: Flatten a list of lists.
def flatten_list(lst_of_lsts):
    flattened = [i for flatlist in lst_of_lsts for i in flatlist]
    return flattened
    pass

# Exercise 5: Remove duplicates from a list.
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    pass
