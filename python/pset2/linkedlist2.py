from adt import LinkedList

def main():
    sllist = LinkedList()
    for i in range(10):
        sllist.append(i)

    for i in range(10):
        sllist.push(i)

    sllist.insert_after(0, "Gyatt")

    print(*sllist, sep=", ")

    for i in range(10):
        print(sllist.pop())

if __name__ == "__main__":
    main()
