def main():
    stack = []

    stack.append(10)
    stack.append(20)
    stack.append(30)

    print(f"Stack: {stack}")
    print(f"Popped element: {stack.pop()}")
    print(f"After popping: {stack}")
    print(f"Top element: {stack[-1]}")

if __name__ == "__main__":
    main()
