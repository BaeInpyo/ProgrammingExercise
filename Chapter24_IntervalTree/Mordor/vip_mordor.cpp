#include <iostream>
#include <vector>

#define MAX_N 100000
#define MAX_Q 10000

using namespace std;

int num_tests;
int num_signs;
int num_trails;
int heights[MAX_N];
int trails_first[MAX_Q];
int trails_last[MAX_Q];

class RMQ {
 public:
  RMQ() {
    n = num_signs;
    min_in_range.resize(4 * n);
    max_in_range.resize(4 * n);
    init(0, n-1, 0);
  }
  int get_difficulty(int left, int right);
 private:
  pair<int, int> get_difficulty(int left, int right, int rmq_left, int rmq_right, int index);
  pair<int, int> init(int left, int right, int index);
  int n = 0;
  vector<int> min_in_range;
  vector<int> max_in_range;
};

pair<int, int> RMQ::init(int left, int right, int index) {
  if (left == right) {
    min_in_range[index] = heights[left];
    max_in_range[index] = heights[left];
  } else {
    int mid = (left + right) / 2;
    auto left_info = init(left, mid, 2*index+1);
    auto right_info = init(mid+1, right, 2*index+2);
    min_in_range[index] = min(left_info.first, right_info.first);
    max_in_range[index] = max(left_info.second, right_info.second);
  }
  return { min_in_range[index], max_in_range[index] };
}

int RMQ::get_difficulty(int left, int right) {
  auto info = get_difficulty(left, right, 0, n-1, 0);
  return info.second - info.first;
}

pair<int, int> RMQ::get_difficulty(int left, int right, int rmq_left, int rmq_right, int index) {
  if (left == rmq_left && right == rmq_right) {
    return { min_in_range[index], max_in_range[index] };
  }

  int rmq_mid = (rmq_left + rmq_right) / 2;
  if (right <= rmq_mid) {
    return get_difficulty(left, right, rmq_left, rmq_mid, 2*index+1);
  } else if (left > rmq_mid) {
    return get_difficulty(left, right, rmq_mid+1, rmq_right, 2*index+2);
  }

  auto left_info = get_difficulty(left, rmq_mid, rmq_left, rmq_mid, 2*index+1);
  auto right_info = get_difficulty(rmq_mid+1, right, rmq_mid+1, rmq_right, 2*index+2);
  return { min(left_info.first, right_info.first), max(left_info.second, right_info.second) };
}

void solution() {
  auto rmq = RMQ();
  for (int i = 0; i < num_trails; ++i) {
    cout << rmq.get_difficulty(trails_first[i], trails_last[i]) << endl;
  }
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_signs; cin >> num_trails;
    for (int i = 0; i < num_signs; ++i) {
      cin >> heights[i];
    }
    for (int i = 0; i < num_trails; ++i) {
      cin >> trails_first[i];
      cin >> trails_last[i];
    }

    solution();
  }
  return 0;
}