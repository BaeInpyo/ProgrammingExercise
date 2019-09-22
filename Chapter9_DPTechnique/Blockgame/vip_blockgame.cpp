#include <iostream>

// For Cache
#define BOARD_IN_INT 1 << 25

// For Game Info
#define MAX   5
#define EMPTY '.'
#define FILL  '#'

using namespace std;

int num_tests;
char board[MAX][MAX];
int encrypted_board = 0;
int blocks[6][3][2] = { {{0, 0}, {0, 1}, {-1, -1}},  // len: 2
                        {{0, 0}, {1, 0}, {-1, -1}},  // len: 2
                        {{0, 0}, {1, 0}, {1, 1}},    // len: 3
                        {{0, 0}, {0, 1}, {1, 1}},    // len: 3
                        {{0, 0}, {0, 1}, {1, 0}},    // len: 3
                        {{0, 0}, {1, 0}, {1, -1}} }; // len: 3
int cache_test_num[BOARD_IN_INT];
bool cache[BOARD_IN_INT];

void init_cache() {
  for (int i = 0; i < BOARD_IN_INT; ++i) {
    cache_test_num[i] = -1;
  }
}

int encrypt_cell(int x, int y) {
  int cell = 1 << y;
  cell = cell << x * MAX;
  return cell;
}

bool is_empty_cell(int x, int y) {
  int encrypted_cell = encrypt_cell(x, y);

  return ((encrypted_board & encrypted_cell) == 0);
}

void encrypt_board() {
  for (int i = 0; i < MAX; ++i) {
    for (int j = 0; j < MAX; ++j) {
      if (board[i][j] == FILL) {
        encrypted_board += encrypt_cell(i, j);
      }
    }
  }
}

bool can_insert_block(int x, int y, int block_index) {
  bool result = true;
  for (int parts = 0; parts < 3; ++parts) {
    if (block_index < 2 && parts == 2) break;
    int loc_x = x+blocks[block_index][parts][0];
    int loc_y = y+blocks[block_index][parts][1];
    if (0 <= loc_x && loc_x < MAX && 0 <= loc_y && loc_y < MAX) {
      result = result && is_empty_cell(loc_x, loc_y);
    } else {
      result = false;
    }
  }
  
  return result;
}

void modify_block(int x, int y, int block_index, bool insert) {
  for (int parts = 0; parts < 3; ++parts) {
    if (block_index < 2 && parts == 2) break; 
    int loc_x = x+blocks[block_index][parts][0];
    int loc_y = y+blocks[block_index][parts][1];
    
    if (insert) encrypted_board += encrypt_cell(loc_x, loc_y);
    else encrypted_board -= encrypt_cell(loc_x, loc_y);
  }
}

bool can_win() {
  int &test_num = cache_test_num[encrypted_board];
  bool &res = cache[encrypted_board];

  if (test_num == num_tests) return res;

  // Main algorithm
  test_num = num_tests;
  res = false;
  for (int i = 0; i < MAX; ++i) {
    for (int j = 0; j < MAX; ++j) {
      for (int block_index = 0; block_index < 6; ++block_index) {
        if (can_insert_block(i, j, block_index)) {
          modify_block(i, j, block_index, true);
          if (!can_win()) res = true;
          modify_block(i, j, block_index, false);
        }
      }
    }
  }

  return res;
}

void solution() {
  encrypt_board();
  if (can_win()) { cout << "WINNING" << endl; }
  else { cout << "LOSING" << endl; }
}

int main() {
  cin.sync_with_stdio(false);
  
  cin >> num_tests;

  init_cache();

  while (--num_tests >= 0) {
    for (int r = 0; r < MAX; ++r) {
      for (int c = 0; c < MAX; ++c) {
        cin >> board[r][c];
      }
    }
    
    solution();
  }

  return 0;
}
