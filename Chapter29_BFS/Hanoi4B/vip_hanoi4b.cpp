#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstring>

using namespace std;

int n;
int init, target;
int c[1 << 24];

void push(int towers, int index, int disc) {
  towers += (index << (2 * (disc-1)));
}

void initialize() {
  target = (1 << (2*n)) - 1;
}

int sgn(int x) { if (!x) return 0; return x > 0 ? 1 : -1; }
int incr(int x) { if (x < 0) return x - 1; return x + 1; }

int bidirectional(int start, int end) {
  //unordered_map<int, int> c;
  memset(c, 0, sizeof(c));
  queue<int> q;
  if (start == end) return 0;

  q.push(start); c[start] = 1;
  q.push(end); c[end] = -1;
  while (!q.empty()) {
    int here = q.front(); q.pop();
    int towers[4]{0, 0, 0, 0};
    for (int i = n; i > 0; --i) {
      towers[(here >> (2*(i-1))) & 3] = i;
    }
    for (int i = 0; i < 4; ++i) {
      if (towers[i] != 0) {
        for (int j = 0; j < 4; ++j) {
          if (i != j) {
            if (towers[i] < towers[j] || towers[j] == 0) {
              int next = (here & ~(3 << 2*(towers[i]-1))) | (j << 2*(towers[i]-1));
              if (c[next] == 0) {
                c[next] = incr(c[here]);
                q.push(next);
              } else if (sgn(c[next]) != sgn(c[here])) {
                return abs(c[next]) + abs(c[here]) - 1;
              }
            }
          }
        }
      }
    }
  }
  return -1;
}

void solution() {
  initialize();

  cout << bidirectional(init, target) << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> n;
    init = 0;
    for (int i = 0; i < 4; ++i) {
      int num_d; cin >> num_d;
      for (int j = 0; j < num_d; ++j) {
        int disc; cin >> disc;
        init += (i << (2 * (disc-1)));
      }
    }
    solution();
  }
}