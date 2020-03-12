#include <iostream>

#define MAX_N 100000
#define MAX_Q 10000

using namespace std;

int num_tests;
int num_signs;
int num_trails;
int heights[MAX_N];
int trails_first[MAX_Q];
int trails_last[MAX_Q];

void solution() {
  
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_signs; cin >> num_trails;
    for (int i = 0; i < num_signs; ++i) {
      cin >> heights[i];
    }
    for (int i = 0; i < num_trails; ++i) {
      cin >> trails_first[i];
      cin >> trails_last[i];
    }

    solution();
  }
  return 0;
}