#include <iostream>

#define MAX_N 100

using namespace std;

int num_teams;
pair<int, int> week[MAX_N];
pair<int, int> month[MAX_N];

const string success_string = "POSSIBLE";
const string fail_string = "IMPOSSIBLE";

void solution() {}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> num_teams;
    for (int i = 0; i < num_teams; ++i) {
      cin >> week[i].first >> week[i].second
          >> month[i].first >> month[i].second;
    }
    solution();
  }
  return 0;
}