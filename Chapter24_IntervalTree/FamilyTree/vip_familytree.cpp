#include <iostream>

#define MAX_N 100000
#define MAX_Q 10000

using namespace std;

int num_tests;
int num_people;
int num_pairs;
int family[MAX_N];
int pairs_first[MAX_Q];
int pairs_second[MAX_Q];

void solution() {

}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> num_pairs;
    for (int i = 0; i < num_people; ++i) {
      cin >> family[i];
    }
    for (int i = 0; i < num_pairs; ++i) {
      cin >> pairs_first[i];
      cin >> pairs_second[i];
    }
    solution();
  }
  return 0;
}