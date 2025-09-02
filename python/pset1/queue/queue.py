"""
    Author: Steven Ebreo
    Problem Set 1 : Queue
    Simulate a line of people waiting:
    Add 3 names then remove the first one
"""

from adt import Queue

def main():
    queue = Queue()
    print("Queue is now open!")
    print("Current Queue: ", end="")

    queue.enqueue("Steven")
    queue.enqueue("Gea")
    queue.enqueue("Faye")

    for i in range(queue.get_len()):
        print(queue.queue[i], end=" ")
    print()

    print(f"{queue.dequeue()} has exited the queue!")

    print("New queue: ", end="")
    for i in range(queue.get_len()):
        print(queue.queue[i], end=" ")
    print()

if __name__ == "__main__":
    main()

