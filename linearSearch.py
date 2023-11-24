#  Linear Search code
# Can be used for a list for which items can be stores in any order, but as the size increases the amount of
# time taken to search increases correspondingly

#  Using a while loop implementation
def linear_search1(search_item: int, search_list: list):
    # because python always start indexing from 0, hence we have to subtract from the upperbound
    upper_bound = len(search_list) - 1
    lower_bound = 0
    index = lower_bound
    found = False
    while index <= upper_bound and found is False:
        if search_list[index] == search_item:
            found = True
            break  # we can use break to make the code more efficient
        else:
            index = index + 1
    if found is True:
        print(f"{search_item} found at position {index + 1}")
    else:
        print(f"{search_item} doesn't exist in list")
# every item is checked in order, from the lower bound to the upperbound until is upperbound is reached or until the
# item being searched is found


# testing the for loop implementation
array = [4, 2, 8, 17, 9, 3, 7, 12, 34, 21]
linear_search1(search_item=12, search_list=array)


#  Using a for loop implementation
def linear_search2(search_item: int, search_list: list):
    # getting the upper bound of the array/list and storing it in the "upper_bound" variable
    upper_bound = len(search_list)
    # initialising found as false
    found = False
    # looping through the list until the end which the upperbound
    for index in range(upper_bound):
        # checking for the item at each index until it's found or until the end of the loop is reached
        if search_list[index] == search_item:
            found = True
            print(f"{search_item} found at position {index + 1}")
            # help's us exit the procedure
            break
    #  otherwise the value was not found, and we output q message to reflect that condition
    if found is False:
        print(f"{search_item} doesn't exist in list")


# testing the while loop implementation
linear_search1(search_item=8, search_list=array)
