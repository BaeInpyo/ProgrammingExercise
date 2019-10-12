#include <iostream>
#include <set>

#define MAX 10000

using namespace std;

int num_tests;
int n;
int min_for_microwave[MAX];
int min_to_eat[MAX];

auto f = [](pair<int, int> const &a, pair<int, int> const &b) {
  return a.second > b.second;
};

void solution() {
  int total_time = 0;
  int remain_min_to_eat = 0;
  multiset<pair<int, int>, decltype(f)> total_min(f);
  for (int i = 0; i < n; ++i) {
    total_min.insert(make_pair(i, min_to_eat[i]));
  }

  for (auto candidate : total_min) {
    int candidate_index = candidate.first;
    int min_for_m = min_for_microwave[candidate_index];
    int min_to_e = min_to_eat[candidate_index];

    total_time += min_for_m;
    remain_min_to_eat -= min_for_m;
    if (remain_min_to_eat < min_to_e) {
      remain_min_to_eat = min_to_e;
    }
  }

  total_time += remain_min_to_eat;
  
  cout << total_time << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> min_for_microwave[i];
    }
    for (int i = 0; i < n; ++i) {
      cin >> min_to_eat[i];
    }

    solution();
  }
  
  return 0;
}
