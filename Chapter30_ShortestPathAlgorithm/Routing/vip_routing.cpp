#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <cmath>
#include <limits>

#define MAX_N 10000
#define INF_DIST numeric_limits<double>::max()

using namespace std;

int n;
vector<vector<pair<double, int>>> adj;
void solution() {
  double result;

  vector<double> dist(n, INF_DIST);
  priority_queue<pair<double, int>> q;
  q.push({0, 0});
  while (!q.empty()) {
    auto element = q.top(); q.pop();
    double cost1 = -element.first;
    int v1 = element.second;
    if (dist[v1] < cost1) continue;
    for (int i = 0; i < adj[v1].size(); ++i) {
      auto next = adj[v1][i];
      double cost2 = next.first + cost1;
      int v2 = next.second;
      if (dist[v2] > cost2) {
        dist[v2] = cost2;
        q.push({-cost2, v2});
      }
    }
  }

  cout << setprecision(10) << exp(dist[n-1]) << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    int m;
    cin >> n >> m;
    adj.clear(); adj.resize(n, {});
    while (m--) {
      int a, b;
      double c;
      cin >> a >> b >> c;
      adj[a].push_back({log(c), b});
      adj[b].push_back({log(c), a});
    }
    solution();
  }
  return 0;
}
