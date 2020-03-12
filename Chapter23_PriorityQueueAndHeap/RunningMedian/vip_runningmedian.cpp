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
  int result = 0;
  std::vector<int> runtime_numbers;
  for (int i = 0; i < n; ++i) {
    runtime_numbers.push_back(numbers[i]);
  }
  cout << result << endl;
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