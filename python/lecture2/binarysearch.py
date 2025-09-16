def main():
    arr = []
    for i in range(6):
        arr.append((i+1) * 10)
    print("Index of 40:", binary_search(arr,40))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    main()
