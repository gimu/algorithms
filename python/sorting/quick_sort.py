#!/usr/bin/env python3

"""
Quicksort
Desc: Recursively split the list in half.
"""

def sort(list):
    if list:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return sort(less) + [pivot] + sort(more)
    else:
        return [] # Prevent IndexError if an empty list is passed

#print(sort([1, 2, 3, 4, 5, 6, 7]))
print(sort([5, 3, -1, 13, 6, 2, 8]))
print(sort(1))
