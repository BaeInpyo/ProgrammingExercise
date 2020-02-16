#include <iostream>
#include <vector>

#define MAX 50

using namespace std;

int num_tests;
int num_states;
string states[MAX+1];

bool is_clockwise(int i) {
  return (i % 2 == 1);
}


vector<int> get_partial_substring2(string &str) {
  int matched = 0;
  int n = str.size();
  vector<int> pi = vector<int>(n, 0);

  for (int i = 1; i < n; ++i) {
    while (matched > 0 && str[i] != str[matched]) {
      matched = pi[matched - 1];
    }

    if (str[i] == str[matched]) {
      ++matched;
      pi[i] = matched;
    }
  }

  return pi;
}

vector<int> get_partial_substring(string &str) {
  int begin = 1, matched = 0;
  int n = str.size();
  vector<int> pi = vector<int>(n, 0);

  while (begin + matched < n) {
    if (str[begin+matched] == str[matched]) {
      ++matched;
      pi[begin+matched-1] = matched;
    } else {
      if (matched == 0) {
        ++begin;
      } else {
        begin += matched - pi[matched - 1];
        matched = pi[matched - 1];
      }
    }
  }
  return pi;
}

int get_num_rotate(string &base, string &target) {
  string base_ = base + base;
  int base_size = base_.size();
  int target_size = target.size();

  vector<int> pi = get_partial_substring2(target);

  int matched = 0;
  for (int i = 1; i < base_size; ++i) {
    while (matched > 0 && base_[i] != target[matched]) {
      matched = pi[matched - 1];
    }

    if (base_[i] == target[matched]) {
      ++matched;
      if (matched == target_size) {
        return i - matched + 1;
      }
    }
  }
}

void solution() {
  int num_rotate = 0;

  string curr_state = states[0];
  for (int i = 1; i < num_states + 1; ++i) {
    string next_state = states[i];
    if (is_clockwise(i)) {
      num_rotate += get_num_rotate(next_state, curr_state);
    } else {
      num_rotate += get_num_rotate(curr_state, next_state);
    }
    curr_state = next_state;
  }

  cout << num_rotate << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_states;
    for (int i = 0; i < num_states + 1; ++i) {
      cin >> states[i];
    }

    solution();
  }
  return 0;
}