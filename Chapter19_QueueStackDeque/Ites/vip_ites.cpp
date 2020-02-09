#include <iostream>
#include <deque>

#define a 214013
#define b 2531011
#define MOD 10000
#define FIRST 1983

using uint = unsigned int;
using llint = long long int;
using namespace std;

int num_tests;
int length;
int sum;

int preprocess(uint curr) {
  return (curr % 10000 + 1);
}

uint get_next_number(uint prev) {
  llint mod = 4294967296; 
  return (prev * (llint)a % mod + b) % mod;
}

void solution() {
  int count = 0;
  deque<int> status;
  llint partial_sum = 0;
  uint curr = FIRST;
  int p_curr = preprocess(curr);
  for (int i = 0; i < length; ++i) {
    partial_sum += p_curr;
    status.push_back(p_curr);
    while (partial_sum > sum) {
      partial_sum -= status.front();
      status.pop_front();
    }

    if (partial_sum == sum) {
      ++count;
      partial_sum -= status.front();
      status.pop_front();
    }

    curr = get_next_number(curr);
    p_curr = preprocess(curr);
  }

  cout << count << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> sum; cin >> length;
    solution();
  }

  return 0;
}
