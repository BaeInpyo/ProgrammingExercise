#include <iostream>
#include <string>

using namespace std;

int num_tests;
int k;
string words[15];
bool distinct_words[15];

void init_array() {
  for (int i = 0; i < 15; ++i) {
    distinct_words[i] = true;
  }
}

// Check whether i word is subset of j word.
bool check_subset(int i, int j) {
  bool result = false;
  string i_words = words[i];
  string j_words = words[j];

  if (i_words.length() <= j_words.length()) {
    size_t found = j_words.find(i_words);
    if (found != string::npos) {
      result = true;
      distinct_words[i] = false;
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
}

void solution() {
  init_array();
  // Check whether a word is subset of other words and remove it
  preprocess();
}

int main() {
    cin.sync_with_stdio(false);
    cin >> num_tests;
    while (--num_tests >= 0) {
        cin >> k;
        for (int i = 0; i < k; i++) {
            cin >> words[i];
        }

        solution();
    }
}
