#include <iostream>

#define MAX 10

using namespace std;

int num_tests;
int board_height;
int board_width;

int block_row;
int block_column;

char board[MAX][MAX];
char block[4][MAX][MAX];

int max_count;
int theoritical_max;

// Rotate
void preprocess() {
  /* case 1 */
  for (int r = 0; r < block_row; ++r) {
    for (int c = 0; c < block_column; ++c) {
      block[1][c][block_row-1-r] = block[0][r][c];
    }
  }

  for (int r = 0; r < block_row; ++r) {
    for (int c = 0; c < block_column; ++c) {
      block[2][block_row-1-r][block_column-1-c] = block[0][r][c];
    }
  }

  for (int r = 0; r < block_row; ++r) {
    for (int c = 0; c < block_column; ++c) {
      block[3][block_column-1-c][r] = block[0][r][c];
    }
  }

  max_count = 0;
}

void calculate_theoritical_max() {
  int num_white_in_board = 0;
  int num_black_in_block = 0;

  for (int h = 0; h < board_height; ++h) {
    for (int w = 0; w < board_width; ++w) {
      if (board[h][w] == '.') ++num_white_in_board;
    }
  }

  for (int r = 0; r < block_row; ++r) {
    for (int c = 0; c < block_column; ++c) {
      if (block[0][r][c] == '#') ++num_black_in_block;
    }
  }

  theoritical_max = num_white_in_board / num_black_in_block;
}

bool out_of_board_range(int h, int w) {
  if (h >= board_height || w >= board_width) return true;
  return false;
}

bool can_place(int h, int w, int n) {
  if (n % 2 == 0) {
    for (int r = 0; r < block_row; ++r) {
      for (int c = 0; c < block_column; ++c) {
        if (out_of_board_range(h+r, w+c)) return false;
        if (board[h+r][w+c] == '#' && block[n][r][c] == '#') return false;
      }
    }
  } else {
    for (int r = 0; r < block_column; ++r) {
      for (int c = 0; c < block_row; ++c) {
        if (out_of_board_range(h+r, w+c)) return false;
        if (board[h+r][w+c] == '#' && block[n][r][c] == '#') return false;
      }
    }
  }
  return true;
}

void place(int h, int w, int n, bool clear) {
  char element = clear ? '.' : '#';
  if (n % 2 == 0) {
    for (int r = 0; r < block_row; ++r) {
      for (int c = 0; c < block_column; ++c) {
        if (block[n][r][c] == '#')
          board[h+r][w+c] = element;
      }
    }
  } else {
    for (int c = 0; c < block_column; ++c) {
      for (int r = 0; r < block_row; ++r) {
        if (block[n][c][r] == '#')
          board[h+c][w+r] = element;
      }
    }
  }
}

bool find_max(int start_h, int start_w, int count) {
  if (max_count >= theoritical_max) return true;
  int h = start_h;
  int w = start_w;
  while (!out_of_board_range(h,w)) {
    for (int n = 0; n < 4; ++n) {
      if (can_place(h, w, n)) {
        place(h, w, n, false);
        int temp_count = count + 1;
        if (temp_count > max_count) {
          max_count = temp_count;
          if (max_count >= theoritical_max) return true;
        }
        int next_w = w + 1;
        int next_h = h;
        if (next_w == board_width) {
          next_h += 1; next_w = 0;
          if (next_h == board_height) return false;
        } 
        if (find_max(next_h, next_w, temp_count)) return true;
        place(h, w, n, true);
      }
    }
    ++w;
    if (w == board_width) { ++h; w = 0; } 
  }
  return false;
}

void solution() {
  preprocess();
  calculate_theoritical_max();
  find_max(0, 0, 0);
  cout << max_count << endl;
}

int main() {
  cin.sync_with_stdio(false); 

  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> board_height; cin >> board_width;
    cin >> block_row; cin >> block_column; 

    for (int h = 0; h < board_height; ++h) {
      for (int w = 0; w < board_width; ++w) {
        cin >> board[h][w];
      }
    }

    for (int r = 0; r < block_row; ++r) {
      for (int c = 0; c < block_column; ++c) {
        cin >> block[0][r][c];
      }
    }

    solution();
  }
  return 0;
}
