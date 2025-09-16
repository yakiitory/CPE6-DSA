#include <iostream>
#include <stack>
#include <vector>
class Stack {
private:
  std::vector<int> v;

public:
  Stack() : v() {}
  void push(int data) { v.push_back(data); }

  int pop() {
    if (isEmpty()) {
      std::cout << "Stack is empty" << "\n";
    }
    int top = v.back();
    v.pop_back();
    return top;
  }

  int peek() {
    if (isEmpty()) {
      std::cout << "Stack is empty" << "\n";
    }
    return v.back();
  }

  bool isEmpty() { return v.empty(); }

  std::vector<int> get_stack() { return v; }
};

int main(void) {
  Stack stack;
  stack.push(10);
  stack.push(20);
  stack.push(30);

  std::cout << "Vector Stack: ";
  for (int n : stack.get_stack()) {
    std::cout << n << " ";
  }
  std::cout << std::endl;

  std::cout << "Popped element: " << stack.pop() << std::endl;
  std::cout << "After popping: ";
  for (int n : stack.get_stack()) {
    std::cout << n << " ";
  }
  std::cout << std::endl;

  std::cout << "Top element: " << stack.peek() << std::endl;

  // Alternatively
  std::stack<int> i_stack;
  i_stack.push(10);
  i_stack.push(20);
  i_stack.push(30);

  std::cout << "Stack: ";
  while (!i_stack.empty()) {
    std::cout << i_stack.top() << " ";
    i_stack.pop();
  }
  std::cout << std::endl;
}
