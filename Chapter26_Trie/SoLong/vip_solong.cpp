#include <iostream>

#define MAX_N 10000
#define MAX_M 20000
#define ALPHABET 26

using namespace std;

int num_tests;
int n;
int m;
std::string words[MAX_N];
int freq[MAX_N];
std::string input[MAX_M];

class Trie {
 public:
  void Insert(int index, int pos = 0) {
    if (pos >= words[index].size()) {
      terminate_ = true;
      return;
    }

    int code = CharToInt(words[index][pos]);
    Trie *child;
    if (children_[code] == nullptr) {
      child = new Trie();
      child->most_freq_index_ = index;
      children_[code] = child;
    } else {
      child = children_[code];
      if (freq[child->most_freq_index_] < freq[index] ||
         (freq[child->most_freq_index_] == freq[index] && words[child->most_freq_index_].compare(words[index]) > 0)) {
        child->most_freq_index_ = index;
      }
    }
    child->Insert(index, pos+1);
  }

  int CalcNumPress(int index, int pos = 0) {
    if (pos >= input[index].size()) return 0;

    int code = CharToInt(input[index][pos]);
    if (children_[code] == nullptr) return input[index].size() - pos;
    Trie *child = children_[code];
    if (words[child->most_freq_index_].compare(input[index]) == 0) return 1;
    return 1 + child->CalcNumPress(index, pos+1);
  }
 private:
  int CharToInt(char c) { return c - 'A'; }
  Trie *children_[ALPHABET] = { nullptr };
  int most_freq_index_ = -1;
  bool terminate_ = false;
};

void solution() {
  Trie root;
  for (int i = 0; i < n; ++i) {
    root.Insert(i);
  }

  int result = 0;
  for (int i = 0; i < m; ++i) {
    int num_press = root.CalcNumPress(i);
    result += num_press;
    if (num_press < input[i].size()) result += 1;
    result += 1;
  }
  cout << result - 1 << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >>n; cin >>m;
    for (int i = 0; i < n; ++i) {
      cin >> words[i]; cin >> freq[i];
    }

    for (int i = 0; i < m; ++i) {
      cin >> input[i];
    }

    solution();
  }
  return 0;
}