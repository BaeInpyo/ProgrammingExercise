#include <iostream>
#include <vector>
#include <deque>
#include <limits>

#define MIN_INT numeric_limits<int>::min()
#define MAX_INT numeric_limits<int>::max()

using namespace std;

int v;
vector<vector<pair<int, int>>> adj;

bool dfs(int s, vector<bool> &visited) {
  visited[s] = true;
  if (s == 1) return true;
  for (int i = 0; i < adj[s].size(); ++i) {
    int next = adj[s][i].first;
    if (!visited[next]) {
      bool result = dfs(next, visited);
      if (result) return result;
    }
  }
  return false;
}

bool is_reachable() {
  vector<bool> visited(v, false);
  return dfs(0, visited);
}

pair<bool, int> find_past() {
  bool updated = false;
  vector<int> dist(v, MAX_INT);
  dist[0] = 0;
  for (int iter = 0; iter < v; ++iter) {
    updated = false;    
    for (int v1 = 0; v1 < v; ++v1) {
      if (dist[v1] != MAX_INT) {
        for (int i = 0; i < adj[v1].size(); ++i) {
          auto next = adj[v1][i];
          int v2 = next.first;
          int cost = next.second + dist[v1];
          if (dist[v2] > cost) {
            dist[v2] = cost;
            updated = true;
          }
        }
      }
    }
    if (!updated) break;
  }
  return {updated, dist[1]};
}

pair<bool, int> find_future() {
  bool updated = false;
  vector<int> dist(v, MIN_INT);
  dist[0] = 0;
  for (int iter = 0; iter < v; ++iter) {
    updated = false;    
    for (int v1 = 0; v1 < v; ++v1) {
      if (dist[v1] != MIN_INT) {
        for (int i = 0; i < adj[v1].size(); ++i) {
          auto next = adj[v1][i];
          int v2 = next.first;
          int cost = next.second + dist[v1];
          if (dist[v2] < cost) {
            dist[v2] = cost;
            updated = true;
          }
        }
      }
    }
    if (!updated) break;
  }
  return {updated, dist[1]};
}

void solution() {
  bool reachable = is_reachable();
  if (!reachable) {
    cout << "UNREACHABLE" << endl;
    return;
  }

  auto result1 = find_past();
  auto result2 = find_future();

  if (result1.first) {
    cout << "INFINITY" << " ";
  } else {
    cout << result1.second << " ";
  }

  if (result2.first) {
    cout << "INFINITY" << endl;
  } else {
    cout << result2.second << endl;
  }
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;

  while (c--) {
    int w; cin >> v >> w;
    adj.clear(); adj.resize(v, {});
    while (w--) {
      int a, b, d;
      cin >> a >> b >> d;
      adj[a].push_back({b, d});
    }

    solution();
  }

  return 0;
}
