#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

int n;

class State {
 public:
  vector<State> getAdjacent();
  bool operator== (const State &rhs) const { return towers == rhs.towers; }
  bool empty(int index) const { return (towers & windows[index]) == 0; }
  void push(int index, int disc) { 
    long long int value = disc;
    towers += (value << (12 * index));
  }
  void pop(int index) { 
    long long int tower_i = (towers & windows[index]);
    towers = towers - (tower_i & (~tower_i + 1));
  }
  int peek(int index) const {
    long long int tower_i = (towers & windows[index]);
    tower_i = tower_i >> (12 * index);
    return tower_i & (~tower_i + 1);
  }

  std::vector<long long int> decoding() const {
    long long int tower_0 = (towers & windows[0]);
    long long int tower_1 = (towers & windows[1]);
    long long int tower_2 = (towers & windows[2]);
    long long int tower_3 = (towers & windows[3]);

    tower_1 = tower_1 >> 12;
    tower_2 = tower_2 >> 24;
    tower_3 = tower_3 >> 36;
    return {tower_0, tower_1, tower_2, tower_3};
  }

  long long int towers = 0;

  const long long int windows[4] = {
    (long long int)0xFFF,
    (long long int)0xFFF << 12,
    (long long int)0xFFF << 24,
    (long long int)0xFFF << 36
  };
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

State init, target;

void initialize() {
  target.towers = 0;
  target.push(3, (1 << n) - 1);
}

int sgn(int x) { if (!x) return 0; return x > 0 ? 1 : -1; }
int incr(int x) { if (x < 0) return x - 1; return x + 1; }

int bidirectional(State start, State end) {
  unordered_map<long long int, int> c;
  queue<State> q;
  if (start == end) return 0;

  q.push(start); c[start.towers] = 1;
  q.push(end); c[end.towers] = -1;
  while (!q.empty()) {
    State here = q.front(); q.pop();
    auto adjacent = here.getAdjacent();
    for (int i = 0; i < adjacent.size(); ++i) {
      auto iter = c.find(adjacent[i].towers);
      if (iter == c.end()) {
        c[adjacent[i].towers] = incr(c[here.towers]);
        q.push(adjacent[i]);
      } else if (sgn(iter->second) != sgn(c[here.towers])) {
        return abs(iter->second) + abs(c[here.towers]) - 1;
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
    init.towers = 0;
    for (int i = 0; i < 4; ++i) {
      int num_d; cin >> num_d;
      for (int j = 0; j < num_d; ++j) {
        int disc; cin >> disc;
        init.push(i, 1 << (disc-1));
      }
    }
    solution();
  }
}