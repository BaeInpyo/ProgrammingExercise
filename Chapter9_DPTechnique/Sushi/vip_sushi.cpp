#include <iostream>

#define MAX 20
#define MAX_BUDGET 21474836

using namespace std;

int num_tests;
int num_sushi;
int budget;
int min_price = 200;
int price[MAX];
int prefer[MAX];
int cache[MAX_BUDGET];
int max_prefer;

void init_cache() {
  for (int i = 0; i < MAX_BUDGET; ++i) {
    cache[i] = 0;
  }
}

int choose_best(int remain_budget) {
  if (remain_budget < min_price) return 0;

  int &preference = cache[remain_budget];
  if (preference > 0) return preference;

  preference = 0;
  for (int i = 0; i < num_sushi; ++i) {
    int temp_preference;
    int next_budget = remain_budget - price[i];
    if (next_budget >= 0) {
      temp_preference = choose_best(next_budget) + prefer[i];
    }
    if (preference < temp_preference) {
      preference = temp_preference;
    }
  }
  return preference;
}

void solution() {
  init_cache();
  cout << choose_best(budget) << endl;
}

int main () {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_sushi; cin >> budget;
    budget /= 100;
    
    for (int i = 0; i < num_sushi; ++i) {
      int temp_price;
      cin >> temp_price; cin >> prefer[i];
      temp_price /= 100;
      price[i] = temp_price;
      if (min_price > temp_price) {
        min_price = temp_price;
      }
    }

    solution();
  }
  return 0;
}
