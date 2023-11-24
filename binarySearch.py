# Binary code implementation can only work with a conditional loop and also can only work if a list is sorted
# the value of the middle is first tested to see if it matches the required item, if it doesn't the half that does not
# contain the required item is discarded and the lower bound or upper bound is adjusted accordingly, depending on which
# half contains the data item. This is repeated until the item is found or until theirs nothing left to test. And
# because of this a binary search usually takes fewer comparisons to find an item compared to the linear search
def binary_search(search_item: int, search_list: list):  # function definition
    found = False
    upper_bound = len(search_list) - 1
    lower_bound = 0
    while found is False and lower_bound <= upper_bound:  # conditional loop
        mid_point = (upper_bound + lower_bound) // 2  # double slash means integer division
        if search_list[mid_point] == search_item:
            found = True
            break  # to break from the loop and make the code more efficient
        else:
            if search_item < search_list[mid_point]:
                # if the item we are searching is less than the middle item, we discard the right side completely and
                # adjust the upper bound to be the midpoint minus 1
                upper_bound = mid_point - 1
            else:
                # basically the opposite of what described above
                lower_bound = mid_point + 1
    if found is False:
        print(f"{search_item} doesn't exist in the array")
        # if found is false it means the item was not found, and we hence output that the item was not found
    else:
        # also prints the position of where you can find the item
        print(f"{search_item}, exists in the position {mid_point + 1}")
        # else it was found, and we output that the item was found


array = [1, 2, 4, 5, 6, 7, 8, 9, 10, 42, 69]
# testing the search
binary_search(search_item=69, search_list=array)
binary_search(search_item=6, search_list=array)
