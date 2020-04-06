#include <iostream>
#include <vector>

#define MAX_V 200
#define MAX_TIME 20000001

using namespace std;

int v, n;
int adj[MAX_V][MAX_V];
vector<vector<pair<int, int>>> future;

void solution() {
  for (int k = 0; k < v; ++k) {
    for (int i = 0; i < v; ++i) {
      if (i == k || adj[i][k] == MAX_TIME) continue;
      for (int j = 0; j < v; ++j) {
        if (j == i || j == k || adj[k][j] == MAX_TIME) continue;
        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
      }
    }
  }

  int cnt = 0;
  while (n--) {
    int a, b, c;
    cin >> a >> b >> c;
    if (adj[a][b] <= c) {
      ++cnt;
      continue;
    }

    adj[a][b] = c;
    adj[b][a] = c;
    for (int i = 0; i < v; ++i) {
      for (int j = 0; j < v; ++j) {
        adj[i][j] = min(adj[i][j], adj[i][a] + c + adj[b][j]);
        adj[i][j] = min(adj[i][j], adj[i][b] + c + adj[a][j]);
      }
    }
  }
  cout << cnt << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    int m;
    cin >> v >> m >> n;

    for (int i = 0; i < MAX_V; ++i)
      for (int j = 0; j < MAX_V; ++j) {
        if (i == j) adj[i][j] = 0;
        else adj[i][j] = MAX_TIME;
      }

    while (m--) {
      int a, b, c;
      cin >> a >> b >> c;
      adj[a][b] = min(adj[a][b], c);
      adj[b][a] = min(adj[b][a], c);
    }

    solution();
  }
  return 0;
}
