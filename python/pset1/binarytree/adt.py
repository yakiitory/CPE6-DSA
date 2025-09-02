"""
    Author: Steven Ebreo
    Implementation of the 'Binary Tree' structure as a module
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

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
            return Node(value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        return root


