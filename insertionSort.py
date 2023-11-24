# ascending order
# implementation 1
def insertion_sort1(array_to_sort: list):
    indexing_length = range(1, len(array_to_sort))
    for x in indexing_length:
        value_to_sort = array_to_sort[x]
        while array_to_sort[x - 1] > value_to_sort and x > 0:
            array_to_sort[x], array_to_sort[x - 1] = array_to_sort[x - 1], array_to_sort[x]
            x = x - 1
    return array_to_sort


array = [4, 2, 8, 17, 9, 3, 7, 12, 34, 21, 5, 6, 3, 5, 2, 4, 1, 0, 444]
print(insertion_sort1(array_to_sort=array))

print("Shanice")
# implementation 2
def insertion_sort2(sort_array: list):
    for x in range(1, len(sort_array)):
        value_to_sort = sort_array[x]
        inner_loop = x
        if sort_array[x - 1] > value_to_sort:
            while sort_array[x - 1] > value_to_sort and inner_loop > 0:
                sort_array[x], sort_array[x - 1] = sort_array[x - 1], sort_array[x]
                inner_loop = inner_loop - 1
        sort_array[x] = value_to_sort
    return sort_array


#print(insertion_sort2(sort_array=array))


#  sorting in descending order
# implementation 1
def insertion_sort_descending_order1(sort_array: list):
    for x in range(1, len(sort_array)):
        value_to_sort = sort_array[x]
        if sort_array[x - 1] < value_to_sort:
            while sort_array[x - 1] < value_to_sort and x > 0:
                sort_array[x], sort_array[x - 1] = sort_array[x - 1], sort_array[x]
                x = x - 1
        sort_array[x] = value_to_sort
    return sort_array


print(insertion_sort_descending_order1(sort_array=array))


# implementation 2
def insertion_sort_descending_order2(array_to_sort: list):
    indexing_length = range(1, len(array_to_sort))
    for x in indexing_length:
        value_to_sort = array_to_sort[x]
        while array_to_sort[x - 1] < value_to_sort and x > 0:
            array_to_sort[x], array_to_sort[x - 1] = array_to_sort[x - 1], array_to_sort[x]
            x = x - 1
    return array_to_sort


Sorted = insertion_sort_descending_order2(array_to_sort=array)
#print(Sorted)
#  the difference is the change in the less than sign because with this code,
#  instead of (appending large values or sorting them based on whether the value before was larger)
#  we instead( look at the value before and check if the value is smaller than the current value and swap),
#  and only append values that are smaller than the current value onto the list.
