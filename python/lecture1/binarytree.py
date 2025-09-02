class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder(root):
    if root:
        if root.left != None:
            inorder(root.left)
        print(root.value, end=" ")
        if root.right != None:
            inorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Inorder Traversal: ")
inorder(root)
