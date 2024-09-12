# Exercise 1: Create a dictionary from two lists (keys and values).
def create_dict(keys, values):
    return dict(zip(keys, values))
    pass


# Exercise 2: Merge two dictionaries.
def merge_dicts(dict1, dict2):
    merge = dict1.copy()
    merge.update(dict2)
    return merge
    pass

# Exercise 3: Find the key of the maximum value in a dictionary.
def max_value_key(d):
    return max(d, key = d.get)
    pass

# Exercise 4: Sort a dictionary by values.
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key = lambda item: item[1]))
    pass

# Exercise 5: Count the occurrences of elements in a list using a dictionary.
def count_elements(lst):
    return {i: lst.count(i) for i in set(lst)}
    pass
