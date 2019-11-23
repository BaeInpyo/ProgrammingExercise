#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

#define MAX 50

using namespace std;

int num_tests;
int num_friends;
int num_dishes;
int min_count;
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

void sort_dishes() {
  vector<long long int> temp(num_dishes);

  for (int i = 0; i < num_dishes; ++i) {
    temp.push_back(favorites[i]);
  }
  sort(temp.begin(), temp.end(),
        [](long long int first, long long int second) {
          int num_first = 0, num_second = 0;
          while (first > 0) {
            if (first & 0x1) ++num_first;
            first = (first >> 1);
          }
          while (second > 0) {
            if (second & 0x1) ++num_second;
            second = (second >> 1);
          }
          return num_first > num_second;
        }
      );
  
  for (int i = 0; i < num_dishes; ++i) {
    favorites[i] = temp[i];
  }
}

void preprocess() {
  remove_duplicates();
  sort_dishes();
  min_count = 51;
}

void get_min_dishes(int start, int count) {
  if (everyone == 0) {
    if (count < min_count) {
      min_count = count;
    }
    return;
  }
  if (count >= min_count) return;

  for (int i = start; i < num_dishes; ++i) {
    long long int satisfied = favorites[i] & everyone;
    if (!satisfied) continue;
    int next_count = count + 1;
    everyone ^= satisfied;
    get_min_dishes(i+1, next_count);
    everyone |= satisfied;
  }

  return;
}

void solution() {
  preprocess();
  get_min_dishes(0, 0);
  cout << min_count << endl;
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
