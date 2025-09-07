"""
    Author: Steven Ebreo
    Problem Set 1 : Array
    Create an array of 5 student names
    Add one new student
    Remove one student
    Print updated list
"""

def main():
    students = ["Harry", "Hermione", "Ron", "Neville", "Draco"]
    print("Before update:")
    print(*students, sep=", ")

    # Inserts onto array and prints
    students.append("Luna")
    print("After insertion: ")
    print(*students, sep=", ")

    # Removes a student
    students.remove("Draco")
    print("After deletion: ")
    print(*students, sep=", ")

if __name__ == "__main__":
    main()
