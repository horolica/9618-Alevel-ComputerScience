#  Initialising the stack
size = 5
top_pointer = -1
stack = []


def create_stack():
    global top_pointer, stack
    stack = ["" for i in range(size)]
    top_pointer = -1

#  Push operation for an item into the stack


def push(push_item: str):
    global top_pointer, size, stack
    if top_pointer == size - 1:
        print(f"stack is full cannot push {push_item}, the stack is full")
    else:
        top_pointer = top_pointer + 1
        stack[top_pointer] = push_item
        print(stack, end=",")


def pop():
    global top_pointer, size, stack
    if top_pointer == -1:
        print("cannot pop the stack is empty")
    else:
        popped = stack[top_pointer]
        stack[top_pointer] = ""
        print(f"{popped} has been popped from the stack !!!!")
        top_pointer = top_pointer - 1


def test():
    create_stack()
    for food in """pizza,
    hotdog  
    salad
    sushi
    chips  
    pasta
    chocolate 
    cheese, """.split("\n"):
        push(push_item=food.strip())
    pop()
    pop()
    pop()
    pop()
    print(stack)


test()
