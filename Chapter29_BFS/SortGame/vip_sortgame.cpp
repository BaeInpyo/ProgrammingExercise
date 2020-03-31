#include <iostream>
#include <vector>
#include <unordered_map>
#include <deque>
#include <algorithm>

#define MAX_N 8
#define MAX_COMB 8*7*6*5*4*3*2*1

using namespace std;

int n;
vector<int> nums;
unordered_map<int, int> index_map;
int parent[MAX_N+1][MAX_COMB];

void normalize() {
  vector<int> temp(n, 0);
  for (int i = 0; i < n; ++i) {
    temp[i] = nums[i];
  }
  sort(temp.begin(), temp.end());
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (nums[j] == temp[i]) {
        nums[j] = i+1;
        break;
      }
    }
  }
}

int vector_to_int(vector<int> &numbers) {
  int result = 0;
  for (int i = 0; i < numbers.size(); ++i) {
    result *= 10;
    result += numbers[i];
  }
  return result;
}

void build_graph(int nth) {
  int counter = 0;
  vector<int> init(nth, 0);
  for (int i = 0; i < nth; ++i) {
    init[i] = i+1;
  }

  deque<vector<int>> trace(1, init);
  parent[nth][0] = 0;
  index_map[vector_to_int(init)] = counter++;
  while (!trace.empty()) {
    vector<int> current = trace.front(); trace.pop_front();
    int current_enc = vector_to_int(current);
    for (int i = 0; i <= nth-2; ++i) {
      for (int j = i+2; j <= nth; ++j) {
        vector<int> temp = current;
        reverse(temp.begin()+i, temp.begin()+j);
        int next_enc = vector_to_int(temp);
        if (index_map.find(next_enc) == index_map.end()) {
          index_map[next_enc] = counter++;
          trace.push_back(temp);
          parent[nth][index_map[next_enc]] = index_map[current_enc];
        }
      }
    }
  }
}

void initialize() {
  normalize();
}

int find_shortest_path(int from) {
  int depth = 0;
  while (parent[n][from] != from) {
    ++depth;
    from = parent[n][from];
  }
  return depth;
}

void solution() {
  initialize();

  int enc = vector_to_int(nums);
  cout << find_shortest_path(index_map[enc]) << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  for (int i = 1; i <= MAX_N; ++i) {
    build_graph(i);
  }
  while (c--) {
    cin >> n;
    nums.clear(); nums.resize(n, 0);
    for (int i = 0; i < n; ++i) {
      cin >> nums[i];
    }
    solution();
  }
  return 0;
}
