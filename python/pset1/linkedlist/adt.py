"""
    Author: Steven Ebreo
    Singly linked list module for Problem Set 1
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def to_list(self) -> list:
        l = []
        current_node = self.head
        while current_node:    
            l.append(current_node.value)
            current_node = current_node.next
        return l

    def search(self, value) -> Node:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        raise ValueError("Value not found in list")

    def insert_after(self, first_value, insert_value) -> bool:
        specific_node = self.search(first_value)
        if specific_node:
            inserted_node = Node(insert_value)
            inserted_node.next = specific_node.next
            specific_node.next = inserted_node
            return True
        else:
            return False
