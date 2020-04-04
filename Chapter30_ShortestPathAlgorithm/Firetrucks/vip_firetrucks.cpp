#include <iostream>
#include <vector>
#include <queue>
#include <limits>

#define MAX_V 1001
#define MAX_INT numeric_limits<int>::max()

using namespace std;

int v;
vector<int> fires;
vector<int> stations;
vector<vector<pair<int, int>>> adj;

void solution() {
  vector<int> dist(v, MAX_INT);
  priority_queue<pair<int, int>> q;
  for (int station : stations) {
    dist[station] = 0;
    q.push({0, station});
  }

  while (!q.empty()) {
    auto current = q.top(); q.pop();
    int cost1 = -current.first;
    int v1 = current.second;
    if (dist[v1] < cost1) continue;
    for (int i = 0; i < adj[v1].size(); ++i) {
      auto next = adj[v1][i];
      int cost2 = next.first + cost1;
      int v2 = next.second;
      if (dist[v2] > cost2) {
        dist[v2] = cost2;
        q.push({-cost2, v2});
      }
    }
  }

  int result = 0;
  for (int fire : fires) {
    result += dist[fire];
  }
  cout << result << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;

  while (c--) {
    int e, n, m;
    cin >> v >> e >> n >> m;
    fires.clear();
    stations.clear();
    adj.clear(); adj.resize(v, {});
    while (e--) {
      int a, b, t;
      cin >> a >> b >> t;
      adj[a-1].push_back({t, b-1});
      adj[b-1].push_back({t, a-1});
    }

    while (n--) {
      int a; cin >> a;
      fires.push_back(a-1);
    }

    while (m--) {
      int a; cin >> a;
      stations.push_back(a-1);
    }

    solution();
  }
}
