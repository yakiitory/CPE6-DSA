"""
    Author: Steven Ebreo
    Problem Set 1 : Stack
    Simulate an "Undo" feature, pushing 3 actions then popping 1
"""

def main():
    stack = []
    
    # Simulation of searching using a keyboard
    search = "Search: "
    skibidi = "Skibidi"
    stack.append(skibidi)

    print(join_strlist(search, stack))

    toilet = "Toilet"
    stack.append(toilet)

    print(join_strlist(search, stack))

    ohio = "Ohio"
    stack.append(ohio)

    print(join_strlist(search, stack))

    print(f"CTRL + Z: {stack.pop()}")

    print(join_strlist(search, stack))

def join_strlist(header:str, prompt:list) -> str:
    return header + " ".join(prompt)


if __name__ == "__main__":
    main()
