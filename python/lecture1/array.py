def main():
    list = [10,20,30,40,50]

    print("Array Elements: ")
    for i in list:
        print(f"{i}, ", end="")

    list.append(60)
    print(f"\nAfter inserting 60: {list}")

    list.remove(30)
    print(f"After removing 30: {list}")

    if 40 in list:
        print(f"40 found at index {list.index(40)}")

if __name__ == "__main__":
    main()
