#include <iostream>
#include <queue>

using namespace std;

int main() {
  queue<int> queue;
  queue.push(10);
  queue.push(20);
  queue.push(30);

  size_t size = queue.size();

  cout << "Queue: ";
  for (size_t i = 0; i < size; i++) {
    cout << queue.front() << " ";
    queue.pop();
  }
  cout << endl;
  return 0;
}
