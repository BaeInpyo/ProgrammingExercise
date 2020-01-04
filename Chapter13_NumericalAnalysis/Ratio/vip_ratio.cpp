#include <iostream>

#define LIMIT 2000000000

using namespace std;

int num_tests;
long long int n, m;


void solution() {
  int target_ratio = m * 100 / n + 1;

  int hi = LIMIT;
  int lo = 0;
  int ratio = (m + hi) * 100 / (n + hi);
  if (ratio < target_ratio) {
    cout << -1 << endl;
    return;
  }

  while (hi - lo > 1) {
    int mid = (lo + hi) / 2;  
    ratio = (m + mid) * 100 / (n + mid);
    if (ratio >= target_ratio) {
      hi = mid;
    } else {
      lo = mid;
    }
  }

  cout << hi << endl;
}

int main() {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> n; cin >> m;
    solution();
  }

  return 0;
}
