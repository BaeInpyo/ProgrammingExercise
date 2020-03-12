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
        max_heap.push_back(number);
        push_heap(max_heap.begin(), max_heap.end());
        if (max_heap.size() - min_heap.size() > 1) {
          min_heap.push_back(max_heap[0]);
          push_heap(min_heap.begin(), min_heap.end(), greaters());
          pop_heap(max_heap.begin(), max_heap.end());
          max_heap.pop_back();
        }
      } else if (min_heap.size() > 0 && min_heap[0] < number) {
        min_heap.push_back(number);
        push_heap(min_heap.begin(), min_heap.end(), greaters());
        if (max_heap.size() < min_heap.size()) {
          max_heap.push_back(min_heap[0]);
          push_heap(max_heap.begin(), max_heap.end());
          pop_heap(min_heap.begin(), min_heap.end(), greaters());
          min_heap.pop_back();
        }
      } else {
        if (max_heap.size() == min_heap.size()) {
          max_heap.push_back(number);
          push_heap(max_heap.begin(), max_heap.end());
        } else {
          min_heap.push_back(number);
          push_heap(min_heap.begin(), min_heap.end(), greaters());
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