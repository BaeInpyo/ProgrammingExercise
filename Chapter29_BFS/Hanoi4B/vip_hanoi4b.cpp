#include <iostream>
#include <vector>

using namespace std;

int n;

struct State {
  vector<int> towers[4];
};

State curr;

void solution() {

}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while(c--) {
    cin >> n;
    for (int i = 0; i < 4; ++i) {
      int d; cin >> d;
      curr.towers[i].clear();
      curr.towers[i].resize(d, 0);
      for (int j = 0; j < d; ++j) {
        cin >> curr.towers[i][j];
      }
    }
    solution();
  }
}