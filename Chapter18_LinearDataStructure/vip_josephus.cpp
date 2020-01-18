#include <iostream>

using namespace std;

int num_tests;
int num_people;
int kth;

void solution() {}

int main() {
  cin.sync_with_stdio(false);
  
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> kth;
    solution();
  }
  return 0;
}
