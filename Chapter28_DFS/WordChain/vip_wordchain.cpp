#include <iostream>
#include <vector>

#define MAX_N 100
#define NUM_CHAR 26

using namespace std;

int n;
string words[MAX_N];

const string wrong_string = "IMPOSSIBLE";
bool wrong;

bool visited[MAX_N];
vector<int> edges[NUM_CHAR][NUM_CHAR];
int start_char;
int end_char;

inline int char_to_int(char c) { return c - 'a'; }
inline char int_to_char(int c) { return c + 'a'; }

void initialize() {
  wrong = false;
  start_char = -1; end_char = -1;
  vector<int> outgoing_edge_count(NUM_CHAR, 0);
  vector<int> ingoing_edge_count(NUM_CHAR, 0);

  for (int i = 0; i < n; ++i) visited[i] = false;

  for (int i = 0; i < NUM_CHAR; ++i) {
    for (int j = 0; j < NUM_CHAR; ++j) {
      edges[i][j].clear();
    }
  }

  for (int i = 0; i < n; ++i) {
    int front_char = char_to_int(words[i].front());
    int back_char = char_to_int(words[i].back());

    edges[front_char][back_char].push_back(i);

    ++outgoing_edge_count[front_char];
    ++ingoing_edge_count[back_char];
  }

  for (int i = 0; i < NUM_CHAR; ++i) {
    if (outgoing_edge_count[i] == ingoing_edge_count[i] + 1) {
      if (start_char != -1) wrong = true;
      start_char = i;
    } else if (ingoing_edge_count[i] == outgoing_edge_count[i] + 1) {
      if (end_char != -1) wrong = true;
      end_char = i;
    }
  }

  if (start_char == -1 && end_char == -1) {
    start_char = char_to_int(words[0].front());
  } else if (start_char * end_char < 0) {
    wrong = true;
  }
}

string dfs(int start) {
  string result = "";
  for (int i = 0; i < NUM_CHAR; ++i) {
    auto &edges_i = edges[start][i];
    while (!edges_i.empty()) {
      int word_index = edges_i.back(); edges_i.pop_back();
      result = words[word_index] + ' ' + dfs(i) + result;
    }
  }
  return result;
}

void solution() {
  initialize();
  if (wrong) {
    cout << wrong_string << endl;
    return;
  }
  string result = dfs(start_char);
  cout << result << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> words[i];
    }
    solution();
  }
  return 0;
}