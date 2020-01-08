#include <iostream>
#include <cmath>
#include <unordered_map>

#define MAX 10000000

using namespace std;

int num_tests;
int num_divisor;
int lo;
int hi;
int min_factor[MAX + 1];
int num_divisors[MAX + 1];

void initialize() {
  for (int i = 0; i <= MAX; ++i) {
    num_divisors[i] = 0;
  }
}

void calculate_min_factor() {
  int n = MAX;
  int n_square = sqrt(MAX);

  for (int i = 1; i <= MAX; ++i) {
    min_factor[i] = i;
  }
  for (int i = 2; i <= n_square; ++i) {
    if (min_factor[i] == i) {
      for (int j = i*i; j <= MAX; j += i) {
        if (min_factor[j] == j) {
          min_factor[j] = i;
        }
      }
    }
  }
}

void solution() {
  int count = 0;
  for (int number = lo; number <= hi; ++number) {
    int n = number;
    int &num_divisor_in_number = num_divisors[number];

    if (num_divisor_in_number == 0) {
      unordered_map<int, int> primes;
      while (n > 1) {
        int factor = min_factor[n];
        auto it = primes.find(factor);
        if (it != primes.end()) {
          primes[factor] += 1;
        } else {
          primes.insert(make_pair(factor, 1));
        }
        n /= min_factor[n];
      }
      
      num_divisor_in_number = 1;
      for (auto prime : primes) {
        num_divisor_in_number *= (prime.second + 1);
      }
    }

    if (num_divisor_in_number == num_divisor) {
      count++;
    }
  }
  
  cout << count << endl;
  return;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;

  initialize();
  calculate_min_factor();
  while (--num_tests >= 0) {
    cin >> num_divisor;
    cin >> lo;
    cin >> hi;

    solution();
  }

  return 0;
}
