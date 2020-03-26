#include <iostream>
#include <vector>

#define MAX_N 100
#define NUM_CHAR 26

using namespace std;

int n;
string words[MAX_N];

const string wrong_string = "IMPOSSIBLE";

string result;
vector<int> starts_with[NUM_CHAR];

void solution() {

}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> words[i];
    }
    solution();
  }
  return 0;
}