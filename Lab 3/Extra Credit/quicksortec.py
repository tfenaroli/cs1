# Author: Thomas Fenaroli
# Date: 02/25/2021
# Purpose: Define functions to allow for quicksort (EC)

from random import *


# partitions given list
def partition(the_list, p, r, compare_func):

    # random pivot
    rand_index = randint(p, r)
    temp = the_list[rand_index]
    the_list[rand_index] = the_list[r]
    the_list[r] = temp

    # assigns to pivot, i, and j
    pivot = the_list[r]
    i = p - 1
    j = p

    # swaps items as necessary
    while j < r:
        if compare_func(the_list[j], pivot):
            i += 1

            temp1 = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp1

            j += 1
        else:
            j += 1

    # moves pivot value
    temp2 = the_list[i + 1]
    the_list[i + 1] = pivot
    the_list[r] = temp2

    # returns index of pivot
    return i + 1

# recursively quicksorts
def quicksort(the_list, p, r, compare_func):
    # base case of recursion
    if r <= p:
        return None

    # calls partition
    q = partition(the_list, p, r, compare_func)

    # recursively calls quicksort
    quicksort(the_list, p, q - 1, compare_func)
    quicksort(the_list, q + 1, r, compare_func)

# calls quicksort
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
