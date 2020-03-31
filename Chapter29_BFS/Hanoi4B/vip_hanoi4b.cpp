#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int n;

class State {
 public:
  vector<State> getAdjacent();
  bool operator< (const State &rhs) const;
  bool operator== (const State &rhs) const;
  bool empty(int index) const { return towers[index] == 0; }
  void push(int index, int disc) { towers[index] += disc; }
  void pop(int index) { towers[index] -= peek(index); }
  int peek(int index) const { return (towers[index] & (~towers[index] + 1)); }

  int towers[4];
};

vector<State> State::getAdjacent() {
  vector<State> result;

  for (int i = 0; i < 4; ++i) {
    for (int j = 0; j < 4; ++j) {
      if (i == j) continue;
      if (!empty(i) && (peek(i) < peek(j) || peek(j) == 0)) {
        State new_state = *this;
        new_state.push(j, new_state.peek(i));
        new_state.pop(i);
        result.push_back(new_state);
      }
    }
  }

  return result;
}

bool State::operator<(const State &rhs) const {
  if (towers[3] < rhs.towers[3]) return true;
  if (towers[3] == rhs.towers[3] && towers[2] < rhs.towers[2]) return true;
  if (towers[3] == rhs.towers[3] && towers[2] == rhs.towers[2] && towers[1] < rhs.towers[1]) return true;
  if (towers[3] == rhs.towers[3] && towers[2] == rhs.towers[2] && towers[1] == rhs.towers[1] &&
      towers[0] < rhs.towers[0]) return true;
  return false;
}

bool State::operator==(const State &rhs) const {
  if (towers[3] == rhs.towers[3] && towers[2] == rhs.towers[2] &&
      towers[1] == rhs.towers[1] && towers[0] == rhs.towers[0]) return true;
  return false;
}

State init, target;

void initialize() {
  for (int i = 0; i < 3; ++i) {
    target.towers[i] = 0;
  }
  target.towers[3] = (1 << n) - 1;
}

int sgn(int x) { if (!x) return 0; return x > 0 ? 1 : -1; }
int incr(int x) { if (x < 0) return x - 1; return x + 1; }

int bidirectional(State start, State end) {
  map<State, int> c;
  queue<State> q;
  if (start == end) return 0;

  q.push(start); c[start] = 1;
  q.push(end); c[end] = -1;
  while (!q.empty()) {
    State here = q.front(); q.pop();
    auto adjacent = here.getAdjacent();
    for (int i = 0; i < adjacent.size(); ++i) {
      auto iter = c.find(adjacent[i]);
      if (iter == c.end()) {
        c[adjacent[i]] = incr(c[here]);
        q.push(adjacent[i]);
      } else if (sgn(iter->second) != sgn(c[here])) {
        return abs(iter->second) + abs(c[here]) - 1;
      }
    }
  }
  return -1;
}

void solution() {
  initialize();
  cout << bidirectional(init, target) << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> n;
    for (int i = 0; i < 4; ++i) {
      int num_d; cin >> num_d;
      init.towers[i] = 0;
      for (int j = 0; j < num_d; ++j) {
        int disc; cin >> disc;
        init.push(i, 1 << (disc-1));
      }
    }
    solution();
  }
}