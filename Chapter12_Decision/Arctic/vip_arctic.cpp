#include <iostream>

using namespace std;

#define MAX 100

struct Point {
  int x;
  int y;
};

int num_tests;
int num_camps;
Point camps[100];

void solution() {
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_camps;
    for (int i = 0; i < num_camps; ++i) {
      cin >> camps[i].x; cin >> camps[i].y;
    }

    solution();
  }
}
