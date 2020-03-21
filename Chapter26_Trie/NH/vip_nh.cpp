#include <iostream>

#define MAX_M 100

using namespace std;

int num_tests;
int len;
int num_pattern;
std::string patterns[MAX_M];

void solution() {

}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> len; cin >> num_pattern;
    for (int i = 0; i < num_pattern; ++i) {
      cin >> patterns[i];
    }
    solution();
  }
  return 0;
}