#include <iostream>
#include <iomanip>
#include <utility>

#define MAX 1000

using namespace std;

int num_tests;
int num_taken;
int num_limit;
int ranks[MAX];
int counts[MAX];

bool withdrawal[MAX];

void init() {
  for (int i = 0; i < MAX; ++i) {
    withdrawal[i] = false;
  }
}

pair<double, double> get_total_r_c() {
  double sum_r = 0.0;
  double sum_c = 0.0;
  for (int i = 0; i < num_taken; ++i) {
    sum_r += ranks[i];
    sum_c += counts[i];
  }
  return make_pair(sum_r, sum_c);
}

pair<double, double> get_minimum_rank(double prev_sum_r, double prev_sum_c) {
  int min_index = -1;
  double min_rank = 1.0;
  double sum_r = 0;
  double sum_c = 0;
  for (int i = 0; i < num_taken; ++i) {
    if (withdrawal[i]) continue;

    double temp_rank = (prev_sum_r - ranks[i])/(prev_sum_c - counts[i]);
    if (temp_rank < min_rank) {
      min_rank = temp_rank;
      min_index = i;
      sum_r = prev_sum_r - ranks[i];
      sum_c = prev_sum_c - counts[i];
    }
  }

  withdrawal[min_index] = true;
  return make_pair(sum_r, sum_c);
}

void solution() {
  init();
  auto r_and_c = get_total_r_c();
  for (int i = 1; i < num_taken-num_limit+1; ++i) {
    r_and_c = get_minimum_rank(r_and_c.first, r_and_c.second);
  }
  double result = r_and_c.first / r_and_c.second;
  cout << setprecision(8) << result << endl;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_taken; cin >> num_limit;
    for (int i = 0; i < num_taken; ++i) {
      cin >> ranks[i]; cin >> counts[i];
    }

    solution();
  }
}
