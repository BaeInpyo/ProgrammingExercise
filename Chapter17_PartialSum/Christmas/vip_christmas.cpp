#include <iostream>

#define MAX 100000
#define MOD 20091101

using namespace std;

int num_tests;
int num_boxes;
int num_children;
int num_dolls[MAX];

void solution() {}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_boxes; cin >> num_children;
    for (int i = 0; i < num_boxes; ++i) {
      cin >> num_dolls[i];
    }

    solution();
  }
}
