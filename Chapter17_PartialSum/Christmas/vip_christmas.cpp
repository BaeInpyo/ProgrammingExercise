#include <iostream>
#include <fstream>

#define MAX 100000
#define MOD 20091101

using namespace std;

int num_tests;
int num_boxes;
int num_children;
int num_dolls[MAX];
long long int psum[MAX];
int cache[MAX];

void initialize() {
  psum[0] = num_dolls[0];
  cache[0] = -1;
  for (int i = 1; i < num_boxes; ++i) {
    psum[i] += psum[i-1] + num_dolls[i];
    cache[i] = -1;
  }
}

bool can_divide(int start, int end) {
  long long int num_dolls_ij = (start == 0) ? psum[end] : psum[end] - psum[start - 1];
  return (num_dolls_ij >= num_children && num_dolls_ij % num_children == 0);
}

int calculate_num_ways() {
  int result = 0;

  for (int i = 0; i < num_boxes; ++i) {
    for (int j = i; j < num_boxes; ++j) {
      if (can_divide(i, j)) {
        result = (result + 1) % MOD;
      }
    }
  }

  return result;
}

int calculate_num_orders(int start) {
  int &max_result = cache[start];
  if (max_result >= 0) {
    return max_result;
  }
  for (int length = 1; start + length - 1 < num_boxes; ++length) {
    int end = start + length - 1;
    int partial_max = calculate_num_orders(end + 1);

    if (can_divide(start, end)) {
      ++partial_max;
    }
    
    if (partial_max > max_result) {
      max_result = partial_max;
    }
  }

  return max_result;
}

void solution() {
  initialize();
  cout << calculate_num_ways() << " ";
  cout << calculate_num_orders(0) << endl;
}

int main() {
#ifdef FILE_INPUT
  ifstream input_file;
  input_file.open("./input.txt");
  input_file >> num_tests;
  while (--num_tests >= 0) {
    input_file >> num_boxes; input_file >> num_children;
    cout << num_boxes << " " << num_children << endl;
    for (int i = 0; i < num_boxes; ++i) {
      input_file >> num_dolls[i];
    }

    solution();
  }
#else
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_boxes; cin >> num_children;
    for (int i = 0; i < num_boxes; ++i) {
      cin >> num_dolls[i];
    }

    solution();
  }
#endif
}
