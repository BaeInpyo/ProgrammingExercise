#include <iostream>

#define MAX_N 50000

using namespace std;

int num_tests;
int n;
int arr[MAX_N];

void solution() {
  
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> arr[i];
    }
    solution();
  }

  return 0;
}