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
    for student in students:
        print(student)
    
    # Inserts onto array and prints
    students.append("Luna")
    print("After insertion: ")
    for student in students:
        print(student)

    # Removes a student
    students.remove("Draco")
    print("After deletion: ")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
