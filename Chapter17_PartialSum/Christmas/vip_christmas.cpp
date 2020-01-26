#include <iostream>
#include <fstream>

#define MAX 100000
#define MOD 20091101

using namespace std;

int num_tests;
int num_boxes;
int num_children;
int num_dolls[MAX];

int psum[MAX+1];
long long int remains[MAX+1];
int prev_idx[MAX+1];
int cache[MAX+1];

void initialize() {
  for (int i = 0; i < MAX+1; ++i) {
    remains[i] = 0;
    prev_idx[i] = -1;
  }

  psum[0] = 0;
  ++remains[psum[0]];
  for (int i = 1; i < num_boxes+1; ++i) {
    psum[i] = (psum[i-1] + num_dolls[i-1]) % num_children;
    ++remains[psum[i]];
  }
}

int calculate_num_ways() {
  long long int result = 0;

  for (int i = 0; i < num_children; ++i) {
    long long int count = remains[i];
    if (count >= 2) {
      result = (result + ((count * (count-1)) / 2)) % MOD;
    }
  }
  return result;
}

int calculate_num_orders() {
  for (int i = 0; i < num_boxes+1; ++i) {
    if (i > 0)
      cache[i] = cache[i-1];
    else
      cache[i] = 0;
    int prev = prev_idx[psum[i]];
    if (prev != -1) {
      cache[i] = max(cache[i], cache[prev] + 1);
    }
    prev_idx[psum[i]] = i;
  }

  return cache[num_boxes];
}

void solution() {
  initialize();
  cout << calculate_num_ways() << " ";
  cout << calculate_num_orders() << endl;
}

int main() {
#ifdef FILE_INPUT
  ifstream input_file;
  input_file.open("./input.txt");
  input_file >> num_tests;
  while (--num_tests >= 0) {
    input_file >> num_boxes; input_file >> num_children;
    //cout << num_boxes << " " << num_children << endl;
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
