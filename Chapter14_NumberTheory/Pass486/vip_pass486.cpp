#include <iostream>
#include <cmath>

using namespace std;

int num_tests;
int num_divisor;
int lo;
int hi;
int num_divisor_in_number[1000000];
//int min_factor[10000000];

void initialize() {
  for (int i = 0; i < 1000000; ++i) {
    num_divisor_in_number[i] = 0;
  }
}

void calculate_divisors() {
  for (int number = lo; number <= hi; ++number) {
    int n_sqrt = sqrt(number);
    for (int i = 1; i <= n_sqrt; ++i) {
      if (number % i == 0) {
        num_divisor_in_number[number - lo] += 2;
      }
    }
    if (n_sqrt * n_sqrt == number) {
      --num_divisor_in_number[number - lo];
    }
  }
}

void solution() {
  initialize();
  calculate_divisors();

  int count = 0;
  for (int number = 0; number < hi - lo + 1; ++number) {
    if (num_divisor_in_number[number] == num_divisor) {
      ++count;
    }
  }
  
  cout << count << endl;
  return;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_divisor;
    cin >> lo;
    cin >> hi;

    solution();
  }

  return 0;
}
