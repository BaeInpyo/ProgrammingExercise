#include <iostream>
#include <cmath>

#define MAX 1000

using namespace std;

int num_tests;
int num_ingredients;
int ingredients[MAX];
int current_states[MAX];
int todo[MAX];

int gcd;
int num_cups;

int calculate_gcd_of_two_numbers(int p, int q) {
  if (q == 0) return p;
  return calculate_gcd_of_two_numbers(q, p % q);
}

void calculate_gcd() {
  if (num_ingredients == 1) {
    gcd = 1;
    return;
  }
  gcd = calculate_gcd_of_two_numbers(ingredients[0], ingredients[1]);
  for (int i = 2; i < num_ingredients; ++i) {
    if (gcd == 1) return;
    gcd = calculate_gcd_of_two_numbers(gcd, ingredients[i]);
  }
}

void get_num_cups() {
  double biggest_portion = 0;
  for (int i = 0; i < num_ingredients; ++i) {
    double portion = current_states[i]/(double)ingredients[i];
    if (biggest_portion < portion) {
      biggest_portion = portion;
    }
  }

  num_cups = ceil(biggest_portion*gcd);
}

void print_answer() {
  for (int i = 0; i < num_ingredients; ++i) {
    cout << ingredients[i] * num_cups / gcd - current_states[i] << " ";
  }
  cout << endl;
}

void solution() {
  calculate_gcd();
  get_num_cups();

  print_answer();
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_ingredients;
    for (int i = 0; i < num_ingredients; ++i) {
      cin >> ingredients[i];
    }
    for (int i = 0; i < num_ingredients; ++i) {
      cin >> current_states[i];
    }
    solution();
  }
}
