#include <iostream>

#define MAX 50000

using namespace std;

int num_tests;
int n;
int moved[MAX];

class Node {
 public:
  Node(int key) : key_(key), priority_(rand()) {}

  int get_key() { return key_; }
  int get_priority() { return priority_; }
  int get_size() { return size_; }
  Node *get_left() { return left_; }
  Node *get_right() { return right_; }

  void set_left(Node *left) { left_ = left; calculate_size(); }
  void set_right(Node *right) { right_ = right; calculate_size(); }
  
  void calculate_size() {
    size_ = 1;
    if (left_) size_ += left_->get_size();
    if (right_) size_ += right_->get_size();
  }

  int get_depth() {
    int left_depth = (left_) ? left_->get_depth() : 0;
    int right_depth = (right_) ? right_->get_depth() : 0;
    return max(left_depth, right_depth) + 1;
  }

 private:
  int key_ = 0;
  int priority_ = 0;
  int size_ = 1;
  Node *left_ = nullptr;
  Node *right_ = nullptr;
};

pair<Node *, Node *> split(Node *root, int key) {
  if (root == nullptr) return {nullptr, nullptr};

  if (root->get_key() < key) {
    auto rs = split(root->get_right(), key);
    root->set_right(rs.first);
    return {root, rs.second};
  }
  auto ls = split(root->get_left(), key);
  root->set_left(ls.second);
  return {ls.first, root};
}

Node *insert(Node *root, Node *node) {
  if (root == nullptr) return node;
  if (root->get_priority() < node->get_priority()) {
    auto splitted = split(root, node->get_key());
    node->set_left(splitted.first);
    node->set_right(splitted.second);
    return node;
  }

  if (node->get_key() < root->get_key()) root->set_left(insert(root->get_left(), node));
  else root->set_right(insert(root->get_right(), node));
  return root;
}

Node *merge(Node *a, Node *b) {
  if (a == nullptr) return b;
  if (b == nullptr) return a;
  if (a->get_priority() < b->get_priority()) {
    b->set_left(merge(a, b->get_left()));
    return b;
  }
  a->set_right(merge(a->get_right(), b));
  return a;
}

Node *erase(Node *root, int key) {
  if (root == nullptr) return root;
  
  if (root->get_key() == key) {
    Node *ret = merge(root->get_left(), root->get_right());
    delete root;
    return ret;
  }
  if (root->get_key() < key) {
    root->set_right(erase(root->get_right(), key));
  } else {
    root->set_left(erase(root->get_left(), key));
  }
  return root;
}

void solution() {
  Node *root = nullptr;
  for (int i = 1; i <= n; ++i) {
    root = insert(root, new Node(i));
  }
  cout << root->get_depth() << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> n;
    //for (int i = 0; i < n; ++i) {
    //  cin >> moved[i];
    //}

    solution();
  }
}