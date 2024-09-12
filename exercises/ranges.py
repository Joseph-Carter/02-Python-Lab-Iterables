# Exercise 1: Create a list of numbers using range().
def create_range(start, end, step=1):
    return range(start, end, step)
    pass

# Exercise 2: Sum all elements in a range.
def sum_range(start, end):
    The_sum = sum(range(start, end))
    return The_sum
    pass

# Exercise 3: Check if a number is within a range.
def in_range(n, start, end):
    return start <= n <= end
    pass

# Exercise 4: Create a list of even numbers using range().
def even_numbers(start, end):
    if start % 2 != 0:
        start += 1

    return list(range(start, end + 1, 2))
    pass

# Exercise 5: Iterate over a range in reverse.
def reverse_range(start, end):
    return range( end - 1, start - 1, - 1)
    pass
