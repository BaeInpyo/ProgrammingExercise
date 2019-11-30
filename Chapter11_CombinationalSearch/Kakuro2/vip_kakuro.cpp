#include <iostream>
#include <vector>

using namespace std;

#define N 20

int num_tests;
int board_size;
int board[N][N];
int hints[2][N][N] = { 0 };
int num_hints;

struct Hint {
  int sum;
  int count;
  bool used[9] = { false };
  Hint(int s, int c) {
    sum = s;
    count = c;
  }
};

vector<pair<int, int>> pos_vec;
Hint *hhint_of_pos[N][N];
Hint *vhint_of_pos[N][N];

int get_minimum_sum(int count) { return count * (count+1) / 2; }

int get_maximum_sum(int count) { return (9-count) * count + get_minimum_sum(count); }

int get_min_number(int sum, int count) {
  if (count == 1) {
    if (sum >= 10) return 0;
    return sum;
  }
  int maximum_sum = get_maximum_sum(count-1);
  int remain = sum - maximum_sum;

  if (remain <= 0) return 1;
  if (remain > 10-count) return 0;
  return remain;
}

int get_max_number(int sum, int count) {
  if (count == 1) {
    if (sum >= 10) return 0;
    return sum;
  }
  int minimum_sum = get_minimum_sum(count-1);
  int remain = sum - minimum_sum;

  if (remain <= count - 1) return 0;
  if (remain > 9) return 9;
  return remain;
}

void initialize() {
  for (int y = 0; y < board_size; ++y) {
    for (int x = 0; x < board_size; ++x) {
      if (board[y][x]) {
        pos_vec.emplace_back(y,x);
        vhint_of_pos[y][x] = nullptr;
        hhint_of_pos[y][x] = nullptr;
      }
    }
  }

  for (int y = 0; y < board_size; ++y) {
    int x_hint = 0;
    int count = 0;
    for (int x = 1; x < board_size; ++x) {
      if (!board[y][x]) {
        if (count) {
          Hint *cur_hint = new Hint(hints[0][y][x_hint], count);
          for (int x_pos = x_hint + 1; x_pos < x; ++x_pos) {
            hhint_of_pos[y][x_pos] = cur_hint;
          }
          count = 0;
        }
        x_hint = x;
      } else {
        ++count;
      }
    }
    if (count) {
      Hint *cur_hint = new Hint(hints[0][y][x_hint], count);
      for (int x_pos = x_hint + 1; x_pos < board_size; ++x_pos) {
        hhint_of_pos[y][x_pos] = cur_hint;
      }
    }
  }

  for (int x = 0; x < board_size; ++x) {
    int y_hint = 0;
    int count = 0;
    for (int y = 0; y < board_size; ++y) {
      if (!board[y][x]) {
        if (count) {
          Hint *cur_hint = new Hint(hints[1][y_hint][x], count);
          for (int y_pos = y_hint + 1; y_pos < y; ++y_pos) {
            vhint_of_pos[y_pos][x] = cur_hint;
          }
          count = 0;
        }
        y_hint = y;
      } else {
        ++count;
      }
    }
    if (count) {
      Hint *cur_hint = new Hint(hints[1][y_hint][x], count);
      for (int y_pos = y_hint + 1; y_pos < board_size; ++y_pos) {
        vhint_of_pos[y_pos][x] = cur_hint;
      }
    }
  }
}

void preprocess() {
  pos_vec.clear();
  initialize();
}

bool placable(int number, Hint *h_hint, Hint *v_hint) {
  return (!h_hint->used[number-1] && !v_hint->used[number-1]);
}

void place(int number, int y, int x) {
  Hint *h_hint = hhint_of_pos[y][x];
  Hint *v_hint = vhint_of_pos[y][x];

  board[y][x] = number;
  h_hint->sum -= number;
  v_hint->sum -= number;
  h_hint->count -= 1;
  v_hint->count -= 1;
  h_hint->used[number-1] = true;
  v_hint->used[number-1] = true;
}

void revert(int number, int y, int x) {
  Hint *h_hint = hhint_of_pos[y][x];
  Hint *v_hint = vhint_of_pos[y][x];
  board[y][x] = 1;
  h_hint->sum += number;
  v_hint->sum += number;
  h_hint->count += 1;
  v_hint->count += 1;
  h_hint->used[number-1] = false;
  v_hint->used[number-1] = false;
}

bool kakuro(int index) {
  if (index >= pos_vec.size()) return true;

  auto pos = pos_vec[index];
  int y = pos.first;
  int x = pos.second;

  Hint *h_hint = hhint_of_pos[y][x];
  Hint *v_hint = vhint_of_pos[y][x];

  int h_sum = h_hint->sum;
  int h_count = h_hint->count;

  int v_sum = v_hint->sum;
  int v_count = v_hint->count;

  int min_num_for_h = get_min_number(h_sum, h_count);
  if (!min_num_for_h) return false;
  int min_num_for_v = get_min_number(v_sum, v_count);
  if (!min_num_for_v) return false;
  int max_num_for_h = get_max_number(h_sum, h_count);
  if (!max_num_for_h) return false;
  int max_num_for_v = get_max_number(v_sum, v_count);
  if (!max_num_for_v) return false;

  int candidate = max(min_num_for_h, min_num_for_v);
  while (candidate <= min(max_num_for_h, max_num_for_v)) {
    if (placable(candidate, h_hint, v_hint)) {
      place(candidate, y, x);
      if (kakuro(index+1)) return true;
      revert(candidate, y, x);
    }
    ++candidate;
  }

  return false;
}

void print_board() {
  for (int y = 0; y < board_size; ++y) {
    for (int x = 0; x < board_size; ++x) {
      cout << board[y][x];
      cout << " ";
    }
    cout << endl;
  }
}

void solution() {
  preprocess();
  kakuro(0);
  print_board();
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> board_size;

    for (int y = 0; y < board_size; ++y) {
      for (int x = 0; x < board_size; ++x) {
        cin >> board[y][x];
      }
    }

    cin >> num_hints;
    for (int y = 0; y < board_size; ++y) {
      for (int x = 0; x < board_size; ++x) {
        hints[0][y][x] = 0;
        hints[1][y][x] = 0;
      }
    }
    for (int i = 0; i < num_hints; ++i) {
      int y, x, d, sum;
      cin >> y; cin >> x; cin >> d; cin >> sum;
      hints[d][y-1][x-1] = sum;
    }
    
    solution();
  }
}
