#include <iostream>

using namespace std;

int num_tests;
int n, m;

const int limit = 2000000000;

void solution() {
  int curr_ratio = m * 100 / n;
  int next_n = n;
  int next_m = m;
  bool found = false;
  for (int i = 0; i < limit; ++i) {
    next_n += 1;
    next_m += 1;
    int next_ratio = next_m * 100 / next_n;
    if (curr_ratio == next_ratio + 1) {
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
