#include <iostream>
#include <string>

using namespace std;

int num_tests;
int k;
int num_distinct_words;
string input_words[15];
string distinct_words[15];
bool subset[15];
int cache[15][1 << 14];

void init() {
  num_distinct_words = 0;
  for (int i = 0; i < 15; ++i) {
    subset[i] = false;
  }
}

// Check whether i word is subset of j word.
bool check_subset(int i, int j) {
  bool result = false;
  string i_words = input_words[i];
  string j_words = input_words[j];

  if (i_words.length() <= j_words.length()) {
    size_t found = j_words.find(i_words);
    if (found != string::npos) {
      result = true;
      subset[i] = true;
    }
  }

  return result;
}

void preprocess() {
  for (int i = 0; i < k; ++i) {
    for (int j = 0; j < k; ++j) {
      if (i == j) continue;
      if (check_subset(i, j)) break;
    }
  }

  for (int i = 0; i < k; ++i) {
    if (!subset[i]) distinct_words[num_distinct_words++] = input_words[i];
  }
}

int calc_remains(int index, int total) {
  return total - (1 << index);
}

bool exists(int index, int remains) {
  return ((remains & (1 << index)) > 0);
}

int find_shortest(int start, int remains) {
  if (remains == 0) {
    return distinct_words[start].size();
  }

  int &res = cache[start][remains];

  if (res != -1) return res;

  return res;
}

void solution() {
  init();
  // Check whether a word is subset of other words and remove it
  preprocess();

  int index = -1;
  int min_len = 100000;
  int total = (1<<num_distinct_words) - 1;
  for (int i = 0; i < num_distinct_words; ++i) {
    int remains = calc_remains(i, total);
    int len = find_shortest(i, remains);
    if (len < min_len) {
      index = i;
      min_len = len;
    }
  }

  cout << index << endl;
  cout << min_len << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> k;
    for (int i = 0; i < k; i++) {
      cin >> input_words[i];
    }

    solution();
  }
}
