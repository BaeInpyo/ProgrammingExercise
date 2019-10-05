#include <iostream>

#define MAX 20

using namespace std;

int num_tests;
int num_sushi;
int budget;
int price[MAX];
int prefer[MAX];

void solution() {
}

int main () {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_sushi; cin >> budget;

    for (int i = 0; i < num_sushi; ++i) {
      cin >> price[i]; cin >> budget[i];
    }

    solution();
  }
  return 0;
}
