#include <iostream>

using namespace std;

int num_tests;
long long int n, m;

const int limit = 2000000000;

void solution() {
  int curr_ratio = m * 100 / n;
  long long int next_n = n;
  long long int next_m = m;
  bool found = false;

  if (curr_ratio >= 99) {
    cout << -1 << endl;
    return;
  }

  for (int i = 0; i < limit; ++i) {
    next_n += 1;
    next_m += 1;
    int next_ratio = next_m * 100 / next_n;
    if (curr_ratio + 1 == next_ratio) {
      found = true;
      break;
    }
  }
  if (found) { 
    cout << next_n - n << endl;
  } else {
    cout << -1 << endl;
  }
}

int main() {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> n; cin >> m;
    solution();
  }

  return 0;
}
