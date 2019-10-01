#include <iostream>
#include <string>

using namespace std;

int num_tests;
int k;
int num_distinct_words;
string input_words[15];
string distinct_words[15];
bool subset[15];
int substring_len[15][15];
int next_index[15];
int cache[15][1 << 14];

void init() {
  num_distinct_words = 0;
  for (int i = 0; i < 15; ++i) {
    for (int j = 0; j < (1<<14); ++j) {
      cache[i][j] = -1;
    }
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

int calc_substr_len(int left, int right) {
  int sub_len = 0;
  string left_word = distinct_words[left];
  string right_word = distinct_words[right];
  int len_left = left_word.size();
  int len_right = right_word.size();

  for (int temp_len = 1; temp_len < len_right; ++temp_len) {
    bool match = true;
    int right_index = 0;
    for (int left_index = len_left - temp_len; left_index < len_left; ++left_index) {
      if (left_index < 0) {
        return sub_len;
      }
      
      if (left_word[left_index] != right_word[right_index]) {
        match = false;
        break;
      }
      ++right_index;
    }
    if (match) sub_len = temp_len;
  }

  return sub_len;
}

void preprocess() {
  for (int i = 0; i < k; ++i) {
    for (int j = 0; j < k; ++j) {
      if (i == j) continue;
      if (!subset[j] && check_subset(i, j)) {
        break;
      }
    }
  }

  for (int i = 0; i < k; ++i) {
    if (!subset[i]) distinct_words[num_distinct_words++] = input_words[i];
  }
  
  for (int i = 0; i < num_distinct_words; ++i) {
    for (int j = 0; j < num_distinct_words; ++j) {
      if (i != j) {
        substring_len[i][j] = calc_substr_len(i, j);
      }
    }
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

  res = 100000;
  for (int i = 0; i < num_distinct_words; ++i) {
    if (exists(i, remains)) {
      int common_len = substring_len[start][i];
      int len = distinct_words[start].size() + find_shortest(i, calc_remains(i, remains)) - common_len;
      if (len < res) {
        res = len;
        next_index[start] = i;
      }
    }
  }

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

  // TODO: reconstruct
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
