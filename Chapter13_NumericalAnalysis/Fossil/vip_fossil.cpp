#include <iostream>

#define MAX 100

using namespace std;

struct _Point {
  double x;
  double y;
};

using Point = struct _Point;

int num_tests;
int num_a_points;
int num_b_points;
Point A[MAX];
Point B[MAX];

void solution() {

}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_a_points; cin >> num_b_points;
    for (int i = 0; i < num_a_points; ++i) {
      cin >> A[i].x; cin >> A[i].y;
    }

    for (int i = 0; i < num_b_points; ++i) {
      cin >> B[i].x; cin >> B[i].y;
    }

    solution();
  }

  return 0;
}
