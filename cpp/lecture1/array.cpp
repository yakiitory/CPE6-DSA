#include <iostream>

void append(int *&original, int &current_size, int value);
void remove(int *&original, int &current_size, int value);

int main(void) {
  int *arr = new int[5]{10, 20, 30, 40, 50};
  int arr_size{5};

  std::cout << "Array Elements: ";
  for (int i = 0; i < arr_size; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  append(arr, arr_size, 60);
  std::cout << "After appending 60: ";
  for (int i = 0; i < arr_size; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  remove(arr, arr_size, 30);
  std::cout << "After removing 30: ";
  for (int i = 0; i < arr_size; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}

void append(int *&original, int &current_size, int value) {
  int new_size{current_size + 1};
  int *new_arr = new int[new_size];

  if (!new_arr) {
    std::cout << "Error appending value!" << std::endl;
  }
  std::copy(original, original + current_size, new_arr);
  new_arr[current_size] = value;

  delete[] original;
  original = new_arr;
  current_size = new_size;
}

void remove(int *&original, int &current_size, int value) {
  int new_size{current_size - 1};
  int *new_arr = new int[new_size];

  if (!new_arr) {
    std::cout << "Error creating an array!" << std::endl;
  }
  for (int i = 0, j = 0; i < current_size; i++) {
    if (original[i] == value) {
      continue;
    }
    new_arr[j] = original[i];
    j++;
  }

  delete[] original;
  original = new_arr;
  current_size = new_size;
}
