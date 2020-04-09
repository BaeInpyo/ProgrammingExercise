#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>

#define MAX_N 500

using namespace std;

int n;
pair<double, double> building[MAX_N];
double adj[MAX_N][MAX_N];
bool used[MAX_N][MAX_N];
int parent[MAX_N];

double get_dist(int i, int j) {
  auto b_i = building[i];
  auto b_j = building[j];
  return sqrt(pow(b_i.first - b_j.first, 2) + pow(b_i.second - b_j.second, 2));
}

int find_parent(int i) {
  if (parent[i] == i) return i;
  return parent[i] = find_parent(parent[i]);
}

void merge(int i, int j) {
  i = find_parent(i);
  j = find_parent(j);

  parent[i] = j;
}

void solution() {
  double result = 0;

  vector<pair<double, pair<int, int>>> order;
  for (int i = 0; i < n; ++i) {
    for (int j = i+1; j < n; ++j) {
      if (!used[i][j]) order.push_back({adj[i][j], {i, j}});
    }
  }
  sort(order.begin(), order.end());
  for (auto candidate : order) {
    auto i = candidate.second.first;
    auto j = candidate.second.second;
    if (find_parent(i) == find_parent(j)) continue;
    merge(i, j);
    result += candidate.first;
  }
  cout << setprecision(10) << result << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    int m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      cin >> building[i].first;
    }
    for (int i = 0; i < n; ++i) {
      cin >> building[i].second;
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        adj[i][j] = get_dist(i, j);
        used[i][j] = false;
      }
      parent[i] = i;
    }
    while (m--) {
      int a, b; cin >> a >> b;
      if (!used[a][b] && !used[b][a]) {
        used[a][b] = true;
        used[b][a] = true;
        merge(a, b);
      }
    }

    solution();
  }
  return 0;
}
