"""
    Author: Steven Ebreo
    Problem Set 1 : Binary Tree
    Create a binary tree with at least 7 nodes.
    Implement inorder, preorder, and postorder traversals
"""

from adt import BinaryTree

def main():
    tree = BinaryTree(50)
    root = tree.root
    values = [30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(root, value)

    preorder_list = []
    tree.preorder(root, preorder_list)
    print(*preorder_list, sep=", ")

    inorder_list = []
    tree.inorder(root, inorder_list)
    print(*inorder_list, sep=", ")

    postorder_list = []
    tree.postorder(root, postorder_list)
    print(*postorder_list, sep=", ")

if __name__ == "__main__":
    main()
