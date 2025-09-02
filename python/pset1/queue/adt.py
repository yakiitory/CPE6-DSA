"""
    Author: Steven Ebreo
    Implementation of the 'Queue' data structure as a module
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self) -> bool:
        return self.get_len() == 0
    
    def get_len(self) -> int:
        return len(self.queue)

