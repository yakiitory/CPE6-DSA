from collections import deque

def main():
    queue = deque()

    queue.append(10)
    queue.append(20)
    queue.append(30)

    print(f"Queue: {queue}")
    print(f"Dequeued element: {queue.popleft()}")
    print(f"After dequeuing: {queue}")

if __name__ == "__main__":
    main()
