# Queue(circular)
size = 10


def enqueue(data: str):
    global queue, end_pointer, start_pointer, size
    if end_pointer == start_pointer and queue[end_pointer] is not None:
        print(f"The queue is full cannot enqueue {data}")
    else:
        queue[end_pointer] = data
        end_pointer += 1
        if end_pointer == size:
            end_pointer = 0
        print(f"{data} was added to the queue")


def dequeue():
    global queue, end_pointer, start_pointer, size
    if end_pointer == start_pointer and queue[end_pointer] is None:
        print("cannot dequeue, the queue is empty!!!!")
    else:
        data_removed = queue[start_pointer]
        queue[start_pointer] = None
        start_pointer += 1
        if start_pointer == size:
            start_pointer = 0

        print(f"{data_removed} has been removed from the queue")


if __name__ == "__main__":
    queue = [None for i in range(size)]
    end_pointer = 0
    start_pointer = 0


def test():
    for colours in """"Red
    White
    Black
    Indigo
    Green
    Violent
    Yellow
    Blue
    Purple
    Gold
    Silver""".split("\n"):
        enqueue(data=colours.strip())
    print(queue)
    for i in range(7):
        dequeue()
    print(queue)


test()
