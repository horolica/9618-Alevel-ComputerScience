# Each element in the array is compared with the element next to it and the swapped if the elements are in the wrong
# order, note; the element in the upperbound is now in the correct position, this is repeated with once less item in the
# list until theirs only one element remaining in the list, or no more swaps to be made.
# is implemented using both a condition loop (while) and a count controlled loop (for).

# Sorting in ascending order
def bubble_sort1(sort_list):
    swap = True
    top = len(sort_list) - 1
    while swap is True or top > 0:
        swap = False
        indexing_length = range(top)
        for x in indexing_length:
            if sort_list[x] > sort_list[x + 1]:
                sort_list[x], sort_list[x + 1] = sort_list[x + 1], sort_list[x]
                # easier way to swap without having to use a temp variable
                swap = True
        top = top - 1


List = [9092, 8500, 8203, 7980, 7246, 7001, 6490, 6003, 2000, 9999, 10000]
bubble_sort1(sort_list=List)
print(List)


# Sorting in descending order
def bubble_sort2(sort_list):
    swap = False
    top = len(sort_list) - 1
    while swap is False or top > 0:
        swap = True
        indexing_length = range(top)
        for x in indexing_length:
            if sort_list[x] < sort_list[x + 1]:
                # exactly the same logic as sorting in ascending order just change the sign, to move the largest value
                # the lower bound.
                sort_list[x], sort_list[x + 1] = sort_list[x + 1], sort_list[x]
                swap = False
        top = top - 1
    return sort_list


list_sorted = bubble_sort2(sort_list=List)
print(list_sorted)
