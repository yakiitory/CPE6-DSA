"""
    Author: Steven Ebreo
    Problem Set 1 : Linked List
    Build a linked list of 3 integers, and display
    Insert a new number, and then display
"""
from adt import LinkedList

def main():
    sllist = LinkedList(1871)
    sllist.insert_after(1871, 1917)
    sllist.insert_after(1917, 1945)

    list = sllist.to_list()
    str_list = [str(x) for x in list]
    print(f"Initial list: {", ".join(str_list)}")

    # Insert a new number in between
    sllist.insert_after(1917, 1941)
    new_list = sllist.to_list()
    new_str_list = [str(x) for x in new_list]
    print(f"Mutated list: {", ".join(new_str_list)}")

if __name__ == "__main__":
    main()

