#include <iostream>
#include <cstring>

#define MAX_TIME 50001
#define MAX_V 500

using namespace std;

int v;
int delay[MAX_V];
int adj[MAX_V][MAX_V];
int max_delay[MAX_V][MAX_V];
int s, d;

void initialize() {
  for (int i = 0; i < v; ++i) {
    for (int j = 0; j < v; ++j) {
      if (i == j) adj[i][j] = 0;
      else adj[i][j] = MAX_TIME;
      max_delay[i][j] = 0;
    }
  }
}

void build() {
  for (int k = 0; k < v; ++k) {
    for (int i = 0; i < v; ++i) {
      if (i == k || adj[i][k] == MAX_TIME) continue;
      for (int j = 0; j < v; ++j) {
        if (j == i || j == k || adj[k][j] == MAX_TIME) continue;
        int temp_max_delay = max(max_delay[i][k], max_delay[k][j]);
        temp_max_delay = max(temp_max_delay, delay[k]);
        int adjust_delay = temp_max_delay - max_delay[i][k] - max_delay[k][j];
        if (adj[i][j] > adj[i][k] + adj[k][j] + adjust_delay) {
          adj[i][j] = adj[i][k] + adj[k][j] + adjust_delay;
          max_delay[i][j] = temp_max_delay;
        }
      }
    }
  }
}

void solution() {
  cout << adj[s][d] << endl; 
}

int main() {
  cin.sync_with_stdio(false);
  int e;
  cin >> v >> e;
  initialize();
  for (int i = 0; i < v; ++i) {
    cin >> delay[i];
  }
  while (e--) {
    int a, b, c;
    cin >> a >> b >> c;
    adj[a-1][b-1] = c;
    adj[b-1][a-1] = c;
  }
  build();

  int c; cin >> c;
  while (c--) {
    cin >> s >> d;
    s -= 1; d -= 1;
    solution();
  }
  return 0;
}
