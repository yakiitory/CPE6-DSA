"""
    Author: Steven Ebreo
    Implementation of several abstract data types as a module
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"node.value = {self.value}; node.next = {self.next}\n"

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
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    # TODO: Implement operator overrides
    #def __add__(self, other_list):
    

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
    
    def append(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head
        else:
            self.tail.next = new
            self.tail = self.tail.next

    def insert_after(self, first_value, insert_value) -> bool:
        if self.head == None:
            return False
        specific_node = self.search(first_value)
        if specific_node:
            inserted_node = Node(insert_value)
            inserted_node.next = specific_node.next
            specific_node.next = inserted_node
            return True
        else:
            return False

    def delete(self, value) -> bool:
        if self.head == None:
            return False
        elif self.head == value:
            self.head = self.head.next
            return True

        curr = self.head
        prev = self.head
        while curr:
            if curr.value == value:
                prev.next = curr.next
                curr = None
                return True
            else:
                prev = curr
                curr = curr.next
        return False
    
    def push(self, value) -> bool:
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head
            return True
        else:
            new.next = self.head
            self.head = new
            return True

    def pop(self):
        if self.head == None:
            raise ValueError("List is empty!")
        else:
            tmp = self.head
            self.head = self.head.next
            return tmp.value
    
    def pop_node(self) -> Node:
        if self.head == None:
            raise ValueError("List is empty!")
        else:
            tmp = self.head
            self.head = self.head.next
            return tmp

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
