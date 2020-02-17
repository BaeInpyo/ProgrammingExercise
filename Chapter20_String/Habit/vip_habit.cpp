#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;

int num_tests;
int cnt;
string words;


struct SuffixComparator {
  const string &s;
  SuffixComparator(const string &s) : s(s) {}
  bool operator () (int i, int j) {
    return strcmp(s.c_str() + i, s.c_str() + j) < 0;
  }
};

vector<int> get_suffix_array(const string &s) {
  vector<int> perm;
  for (int i = 0; i < s.size(); ++i) perm.push_back(i);

  sort(perm.begin(), perm.end(), SuffixComparator(s));
  return perm;
}

int common_prefix(int i, int j) {
  int k = 0;
  while (i < words.size() && j < words.size() && words[i] == words[j]) {
    ++i; ++j; ++k;
  }
  return k;
}

void solution() {
  int n = words.size();
  vector<int> suffix = get_suffix_array(words);

  int max_length = 0;
  for (int i = 0; i < suffix.size(); ++i) {
    int length = n - suffix[i];
    int k = cnt - 1;
    for (int j = i+1; j < suffix.size() && k > 0; ++j, --k) {
      length = common_prefix(suffix[i], suffix[j]);
      if (length == 0) {
        break;
      }
    }

    if (k == 0) {
      max_length = max(max_length, length);
    }
  }

  cout << max_length << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> cnt;
    cin >> words;

    solution();
  }
  return 0;
}