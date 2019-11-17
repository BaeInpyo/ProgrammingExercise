#include <iostream>
#include <unordered_map>

#define MAX 50

using namespace std;

int num_tests;
int num_friends;
int num_dishes;
unordered_map<string, int> friend_index_map;
long long int favorites[MAX];
long long int everyone;

void remove_duplicates() {
  bool deleted[MAX] = { false };
  for (int i = 0; i < num_dishes; ++i) {
    if (deleted[i]) continue;
    for (int j = 0; j < num_dishes; ++j) {
      if (i == j) continue;
      if (deleted[j]) continue;

      if ((favorites[i] | favorites[j]) == favorites[i])
        deleted[j] = true;
    }
  }
  
  int temp_index = 0;
  for (int i = 0; i < num_dishes; ++i) {
    if (deleted[i]) continue;
    favorites[temp_index++] = favorites[i];
  }

  num_dishes = temp_index;
}

void preprocess() {
  remove_duplicates();
}

int get_min_dishes(int start) {
  if (everyone == 0) return 0;

  int count = 0;
  int min_count = 51;
  for (int i = start; i < num_dishes; ++i) {
    long long int satisfied = favorites[i] & everyone;
    if (!satisfied) continue;
    everyone ^= satisfied;
    count = 1 + get_min_dishes(i+1);
    if (count < min_count) {
      min_count = count;
    }
    everyone |= satisfied;
  }

  return min_count;
}

void solution() {
  preprocess();
  int count = get_min_dishes(0);
  cout << count << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_friends; cin >> num_dishes;
    everyone = ((long long int)1 << num_friends) - 1;
    friend_index_map.clear();
    for (int i = 0; i < num_friends; ++i) {
      string temp; cin >> temp;
      friend_index_map[temp] = i;
    }
  
    for (int i = 0; i < num_dishes; ++i) {
      int num_favorite; cin >> num_favorite;
      favorites[i] = 0;
      for (int j = 0; j < num_favorite; ++j) {
        string temp; cin >> temp;
        favorites[i] |= ((long long int)1 << friend_index_map[temp]);
      }
    }

    solution();
  }  
}
