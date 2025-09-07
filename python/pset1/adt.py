"""
    Author: Steven Ebreo
    Implementation of several abstract data types as a module
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = BinaryNode(value)

    def inorder(self, node, l:list):
        if node:
            self.inorder(node.left, l)
            l.append(node.value)
            self.inorder(node.right, l)

    def preorder(self, node, l:list):
        if node:
            l.append(node.value)
            self.preorder(node.left, l)
            self.preorder(node.right, l)

    def postorder(self, node, l:list):
        if node:
            self.postorder(node.left, l)
            self.postorder(node.right,l)
            l.append(node.value)


    def insert(self, root, value):
        if root == None:
            return BinaryNode(value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        return root

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def to_list(self) -> list:
        l = []
        current_node = self.head
        while current_node:
            l.append(str(current_node.value))
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
