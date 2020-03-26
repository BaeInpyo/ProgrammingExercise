#include <iostream>
#include <set>
#include <deque>

#define MAX_N 1000
#define NUM_CHAR 26

using namespace std;

int n;
string words[MAX_N];
set<int> edges[NUM_CHAR];
bool visited[NUM_CHAR];

string answer = "";
const string wrong_string = "INVALID HYPOTHESIS";
bool wrong = false;

int char_to_int(char c) { return c - 'a'; }
char int_to_char(int c) { return c + 'a'; }

void initialize() {
  answer = "";
  wrong = false; 

  for (int i = 0; i < NUM_CHAR; ++i)
    edges[i].clear();

  for (int i = 1; i < n; ++i) {
    string prev = words[i-1];
    string curr = words[i];
    int end = min(prev.size(), curr.size());
    int index = -1;

    while (++index < end) {
      if (prev[index] != curr[index]) {
        edges[char_to_int(prev[index])].insert(char_to_int(curr[index]));
        break;
      }
    }
  }

  for (int i = 0; i < NUM_CHAR; ++i)
    visited[i] = false;
}

string dfs(int v, string path = "") {
  string result = "";
  visited[v] = true;
  auto &edge = edges[v];
  path += int_to_char(v);
  for (auto iter = edge.begin(); iter != edge.end(); ++iter) {
    if (!visited[*iter])
      result = dfs(*iter, path) + result;
    else
      if (path.find(int_to_char(*iter)) != string::npos) wrong = true;
  }
  return int_to_char(v) + result;
}

void solution() {
  initialize();

  for (int i = 0; i < NUM_CHAR; ++i) {
    if (!visited[i]) {
      answer = dfs(i) + answer;
    }
  }
  
  if (wrong) cout << wrong_string << endl;
  else cout << answer << endl;
}

int main() {
  int C;
  cin.sync_with_stdio(false);
  cin >> C;
  while (C--) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> words[i];
    }
    solution();
  }
  return 0;
}