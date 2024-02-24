#  practise
class Node:
    def __init__(self):
        self.right = None  # right pointer
        self.left = None  # left pointer
        self.data = 0  # data to be added to list as an integer


size = 15
my_tree = []
free_pointer = None
root_pointer = None


def initialise_tree():
    global my_tree, free_pointer, root_pointer
    my_tree = [Node() for i in range(size)]
    indexing_length = range(size - 1)
    for x in indexing_length:
        my_tree[x].left = x + 1
    free_pointer = 0


def find_insertion_point(num: int):
    global my_tree, free_pointer, root_pointer
    pointer = root_pointer
    direction = None
    prev_pointer = None
    while pointer is not None:
        current = my_tree[pointer].data
        prev_pointer = pointer
        if num < current:
            direction = "Left"
            pointer = my_tree[pointer].left
        else:
            direction = "Right"
            pointer = my_tree[pointer].right
    return direction, prev_pointer


def add_num(num: int):
    global my_tree, free_pointer, root_pointer
    if free_pointer is None:
        print(f"Error cannot add {num}, tree is already full")
    else:
        new_pointer = free_pointer
        my_tree[new_pointer].data = num
        free_pointer = my_tree[new_pointer].left
        my_tree[new_pointer].left = None
        #  breaking the Node from the free list by removing the pointer value and the
        #  setting it to None so both right and left pointer are None, because they will be placed
        #  at the bottom of the binary tree
        if root_pointer is None:
            root_pointer = new_pointer
        # it means that it an empty tree would be first item to add to the tree
        else:
            direction, pointer = find_insertion_point(num=num)
            if direction == "Right":
                my_tree[pointer].right = new_pointer
            else:
                my_tree[pointer].left = new_pointer
        print(f"{num}, was successfully added to the tree")


def search_tree(num: int):
    global my_tree, free_pointer, root_pointer
    pointer = root_pointer
    while pointer is not None and my_tree[pointer].data != num:
        current = my_tree[pointer].data
        if current < num:
            direction = "Right"
            pointer = my_tree[pointer].right
        else:
            direction = "Left"
            pointer = my_tree[pointer].left
    if pointer is None:
        print(f"that {num}, does not exist in the tree ")
    else:
        print(f"that {num}, exists in the tree at the position {pointer + 1}")


def traverse_tree(pointer=None):
    global my_tree, free_pointer, root_pointer
    if root_pointer is None:
        print("cannot traverse the tree because it is empty")
    if pointer is None:
        pointer = root_pointer
    left_pointer = my_tree[pointer].left
    right_pointer = my_tree[pointer].right
    data = my_tree[pointer].data
    if left_pointer is not None:
        traverse_tree(pointer=left_pointer)
    print(data)
    if right_pointer is not None:
        traverse_tree(pointer=right_pointer)


# testing function's for adding and searching the tree
        
def test():
    initialise_tree()
    for nums in (27, 19, 36, 42, 16):
        add_num(num=nums)
    traverse_tree()
    search_tree(num=19)
    search_tree(num=16)
    search_tree(num=99)

test()
