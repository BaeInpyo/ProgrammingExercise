#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 200000
#define MOD 20090711

using namespace std;

int num_tests;
int n;
int a, b;
int numbers[MAX];

struct greaters {
  bool operator()(const int& a, const int& b) const {
    return a > b;
  }
};

void initialize() {
  numbers[0] = 1983;
  for (int i = 1; i < n; ++i) {
    long long int numbers_prev_i = numbers[i-1];
    long long int temp = (numbers_prev_i * a) % MOD;
    numbers[i] = (temp + b) % MOD;
  }
}

void push(std::vector<int> &my_heap, int number, bool is_min = false) {
  my_heap.push_back(number);
  if (is_min) {
    push_heap(my_heap.begin(), my_heap.end(), greaters());
  } else {
    push_heap(my_heap.begin(), my_heap.end());
  }
}

void pop(std::vector<int> &my_heap, bool is_min = false) {
  if (is_min) {
    pop_heap(my_heap.begin(), my_heap.end(), greaters());
  } else {
    pop_heap(my_heap.begin(), my_heap.end());
  }
  my_heap.pop_back();
}

void solution() {
  initialize();
  int result = numbers[0];
  if (n == 1) cout << result << endl;
  else {
    std::vector<int> max_heap;
    std::vector<int> min_heap;
    max_heap.push_back(numbers[0]);
    for (int i = 1; i < n; ++i) {
      int number = numbers[i];
      if (max_heap[0] > number) {
        push(max_heap, number);
        if (max_heap.size() - min_heap.size() > 1) {
          push(min_heap, max_heap[0], true);
          pop(max_heap);
        }
      } else if (min_heap.size() > 0 && min_heap[0] < number) {
        push(min_heap, number, true);
        if (max_heap.size() < min_heap.size()) {
          push(max_heap, min_heap[0]);
          pop(min_heap, true);
        }
      } else {
        if (max_heap.size() == min_heap.size()) {
          push(max_heap, number);
        } else {
          push(min_heap, number, true);
        }
      }
      result = (result + max_heap[0]) % MOD;
    }
    cout << result << endl;
  }
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> n; cin >> a; cin >> b;
    solution();
  }
  return 0;
}