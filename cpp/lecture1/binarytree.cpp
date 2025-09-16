#include <iostream>
#include <vector>
class BinaryNode {
public:
  int value;
  BinaryNode *left;
  BinaryNode *right;

  BinaryNode(int val) : value(val), left(nullptr), right(nullptr) {};
};

class BinaryTree {
public:
  explicit BinaryTree(int val) { root = new BinaryNode(val); }
  ~BinaryTree() { free_nodes(root); }

  BinaryTree(const BinaryTree &) = delete;
  BinaryTree &operator=(const BinaryTree &) = delete;

  void insert(int value) { root = insert(root, value); }
  void inorder(std::vector<int> &v) { inorder(root, v); }
  void preorder(std::vector<int> &v) { preorder(root, v); }
  void postorder(std::vector<int> &v) { postorder(root, v); }

private:
  BinaryNode *root;

  BinaryNode *insert(BinaryNode *node, int value) {
    if (node == nullptr) {
      return new BinaryNode(value);
    } else if (value > node->value) {
      node->right = insert(node->right, value);
    } else if (value < node->value) {
      node->left = insert(node->left, value);
    }
    return node;
  }

  void inorder(BinaryNode *node, std::vector<int> &v) {
    if (node != nullptr) {
      inorder(node->left, v);
      v.push_back(node->value);
      inorder(node->right, v);
    }
  }

  void preorder(BinaryNode *node, std::vector<int> &v) {
    if (node != nullptr) {
      v.push_back(node->value);
      preorder(node->left, v);
      preorder(node->right, v);
    }
  }

  void postorder(BinaryNode *node, std::vector<int> &v) {
    if (node != nullptr) {
      postorder(node->left, v);
      postorder(node->right, v);
      v.push_back(node->value);
    }
  }

  void free_nodes(BinaryNode *node) {
    if (node != nullptr) {
      free_nodes(node->left);
      free_nodes(node->right);
      delete node;
    }
  }
};

int main() {
  BinaryTree tree(50);
  int values[6]{30, 70, 20, 40, 60, 80};

  for (int value : values) {
    tree.insert(value);
  }

  std::vector<int> inorder;
  tree.inorder(inorder);
  for (int n : inorder) {
    std::cout << n << " ";
  }
  std::cout << std::endl;

  std::vector<int> preorder;
  tree.preorder(preorder);
  for (int n : preorder) {
    std::cout << n << " ";
  }
  std::cout << std::endl;

  std::vector<int> postorder;
  tree.postorder(postorder);
  for (int n : postorder) {
    std::cout << n << " ";
  }
  std::cout << std::endl;

  return 0;
}
