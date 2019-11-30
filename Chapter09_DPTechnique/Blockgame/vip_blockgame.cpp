#include <iostream>

// For Cache
#define BOARD_IN_INT 1 << 25

// For Game Info
#define MAX   5
#define EMPTY '.'
#define FILL  '#'
#define WIN   2
#define LOSE  1
#define NAN   0

using namespace std;

int num_tests;
int blocks[6][3][2] = { {{0, 0}, {0, 1}, {-1, -1}},  // len: 2
                        {{0, 0}, {1, 0}, {-1, -1}},  // len: 2
                        {{0, 0}, {1, 0}, {1, 1}},    // len: 3
                        {{0, 0}, {0, 1}, {1, 1}},    // len: 3
                        {{0, 0}, {0, 1}, {1, 0}},    // len: 3
                        {{0, 0}, {1, 0}, {1, -1}} }; // len: 3
char cache[BOARD_IN_INT];

void init_cache() {
  for (int i = 0; i < BOARD_IN_INT; ++i) {
    cache[i] = 0;
  }
}

int encrypt_cell(int x, int y) {
  return 1 << x * MAX + y;
}

bool is_empty_cell(int board, int x, int y) {
  int encrypted_cell = encrypt_cell(x, y);

  return ((board & encrypted_cell) == 0);
}

bool can_insert_block(int board, int x, int y, int block_index) {
  for (int parts = 0; parts < 3; ++parts) {
    if (block_index < 2 && parts == 2) break;
    int loc_x = x+blocks[block_index][parts][0];
    int loc_y = y+blocks[block_index][parts][1];
    bool range = (0 <= loc_x && loc_x < MAX && 0 <= loc_y && loc_y < MAX);
    if (!range) return false;
    if (!is_empty_cell(board, loc_x, loc_y)) return false;
  }
  
  return true;
}

int insert_cell(int board, int x, int y, int block_index) {
  for (int parts = 0; parts < 3; ++parts) {
    if (block_index < 2 && parts == 2) break; 
    int loc_x = x+blocks[block_index][parts][0];
    int loc_y = y+blocks[block_index][parts][1];
    
    board |= encrypt_cell(loc_x, loc_y);
  }
  return board;
}

char can_win(int board) {
  char &res = cache[board];
  if (res != NAN) return res;

  // Main algorithm
  res = LOSE;
  for (int i = 0; i < MAX; ++i) {
    for (int j = 0; j < MAX; ++j) {
      if (!is_empty_cell(board, i, j)) continue;
      for (int block_index = 0; block_index < 6; ++block_index) {
        if (can_insert_block(board, i, j, block_index)) {
          int next_board = insert_cell(board, i, j, block_index);
          if (can_win(next_board) == LOSE) {
            res = WIN;
            return res;
          }
        }
      }
    }
  }
  
  return res;
}

void solution(int board) {
  if (can_win(board) == WIN) { cout << "WINNING" << endl; }
  else { cout << "LOSING" << endl; }
}

int main() {
  cin.sync_with_stdio(false);
  
  cin >> num_tests;

  while (--num_tests >= 0) {
    int board = 0;
    for (int r = 0; r < MAX; ++r) {
      for (int c = 0; c < MAX; ++c) {
        char cell; cin >> cell;
        if (cell == FILL) board += encrypt_cell(r, c);
      }
    }
    
    solution(board);
  }

  return 0;
}
