#include <iostream>

#define MAX 100

using namespace std;

int num_tests;
int num_nodes;
int preorder[MAX];
int inorder[MAX];

void print_postorder(int preorder_index, int start, int end) {
  int root = preorder[preorder_index];
  int left_count = 0;
  for (int i = start; i < end && inorder[i] != root; ++i, ++left_count);

  int next_index = preorder_index + 1;
  // print left
  if (left_count != 0) {
    print_postorder(next_index, start, start + left_count);
  }

  // print right
  if (left_count != end - start - 1) {
    print_postorder(next_index+left_count, start + left_count + 1, end);
  }

  // print root
  cout << root << " ";
}

void solution() {
  print_postorder(0, 0, num_nodes);
  cout << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_nodes;

    for (int i = 0; i < num_nodes; ++i) {
      cin >> preorder[i];
    }

    for (int i = 0; i < num_nodes; ++i) {
      cin >> inorder[i];
    }

    solution();
  }
  return 0;
}
