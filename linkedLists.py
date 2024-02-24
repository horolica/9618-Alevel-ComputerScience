class Node:
    def __init__(self):
        self.data = None
        self.pointer = None


size = 9
linked_list = []
start_pointer = None
free_pointer = None


def initialise_list():
    global linked_list, start_pointer, free_pointer
    linked_list = [Node() for i in range(size)]
    indexing_length = range(size - 1)
    for x in indexing_length:
        linked_list[x].pointer = x + 1
    free_pointer = 0
    start_pointer = None


def append(new_data: int):
    global linked_list, free_pointer, start_pointer
    if free_pointer is None:
        print(f"The linked list is full, cannot add {new_data} to the list!")
    else:
        new_pointer = free_pointer
        free_pointer = linked_list[new_pointer].pointer
        linked_list[new_pointer].data = new_data
        linked_list[new_pointer].pointer = None
        if start_pointer is None:
            start_pointer = new_pointer
        else:
            last_pointer = None
            pointer = start_pointer
            while pointer is not None:
                last_pointer = pointer
                pointer = linked_list[pointer].pointer
            linked_list[last_pointer].pointer = new_pointer
        print(f"{new_data} was appended to the linked list")


def prepend(new_data: int):
    global linked_list, free_pointer, start_pointer
    if free_pointer is None:
        print(f"The linked list is full, cannot prepend {new_data} to the list!")
    else:
        new_pointer = free_pointer
        free_pointer = linked_list[new_pointer].pointer
        linked_list[new_pointer].data = new_data
        linked_list[new_pointer].pointer = None
        if start_pointer is None:
            start_pointer = new_pointer
        else:
            linked_list[new_pointer].pointer = start_pointer
            start_pointer = new_pointer


def delete_node(item__delete: int):
    global linked_list, free_pointer, start_pointer
    if start_pointer is None:
        print("the linked list is empty !!!!")
    else:
        found = False
        pointer = start_pointer
        prev_pointer = None
        flag = False
        while found is False:
            current = linked_list[pointer].data
            if current == item__delete:
                found = True
            else:
                prev_pointer = pointer
                pointer = linked_list[pointer].pointer
                if pointer is None:
                    flag = True
                    found = True

        if flag is True:
            print(f"we cannot delete {item__delete}, it doesn't exist !!!")
        else:
            delete_pointer = pointer
            next_pointer = linked_list[delete_pointer].pointer
            if prev_pointer is None:  # deleting the first item
                start_pointer = next_pointer
            else:
                linked_list[prev_pointer].pointer = next_pointer
            linked_list[delete_pointer].data = None
            linked_list[delete_pointer].pointer = free_pointer
            free_pointer = delete_pointer


initialise_list()
prepend(new_data=65)
append(new_data=66)
append(new_data=45)
append(new_data=34)
append(new_data=67)
append(new_data=99)
append(new_data=88)
append(new_data=77)
prepend(new_data=43)
append(new_data=23)
append(new_data=45)
prepend(new_data=11)
delete_node(item__delete=34)
delete_node(item__delete=65)
delete_node(item__delete=99)
for x in range(len(linked_list)):
    print(linked_list[x].data, end=",")
print(free_pointer)


