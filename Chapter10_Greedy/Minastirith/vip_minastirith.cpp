#include <iostream>

#define MAX 100

using namespace std;

enum Loc {
  Y = 0,
  X = 1,
  R = 2,
};

int num_tests;
int num_checkpoints;
double location[MAX][3]; // 0: y, 1: x, 2: r

void solution() {
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_checkpoints;
    for (int i = 0; i < num_checkpoints; ++i) {
      cin >> location[i][Y];
      cin >> location[i][X];
      cin >> location[i][R];
    }

    solution();
  }
}
