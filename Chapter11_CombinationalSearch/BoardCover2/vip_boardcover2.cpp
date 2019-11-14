#include <iostream>
#include <vector>
#include <utility>

#define MAX 10

using namespace std;

int num_tests;
int board_height;
int board_width;

int block_row;
int block_column;

char board[MAX][MAX];
char block[MAX][MAX];
vector<vector<pair<int, int>>> opt_blocks;
bool zero_point[4]; 
int min_block_size;

int num_black_in_block;

int max_count;

bool is_same_blocks(vector<pair<int, int>> &block0, vector<pair<int, int>> &block1) {
  for (auto indices0 : block0) {
    auto iter = block1.begin();
    for (; iter != block1.end(); ++iter) {
      if (indices0.first == (*iter).first && indices0.second == (*iter).second) break;
    }
    if (iter == block1.end()) return false;
  }
  return true;
}

// Rotate
void preprocess() {
  opt_blocks.clear();
  for (int i = 0; i < 4; ++i) zero_point[i] = false;

  vector<pair<int, int>> block0;
  vector<pair<int, int>> block1;
  vector<pair<int, int>> block2;
  vector<pair<int, int>> block3;
  for (int r = 0; r < block_row; ++r) {
    for (int c = 0; c < block_column; ++c) {
      if (block[r][c] == '#') {
        block0.emplace_back(make_pair(r, c));
        block1.emplace_back(make_pair(c, block_row-1-r));
        block2.emplace_back(make_pair(block_row-1-r, block_column-1-c));
        block3.emplace_back(make_pair(block_column-1-c, r));
      }
    }
  }
  opt_blocks.push_back(block0);
  if (!is_same_blocks(block0, block1)) opt_blocks.push_back(block1);
  if (!is_same_blocks(block0, block2) && !is_same_blocks(block1, block2)) opt_blocks.push_back(block2);
  if (!is_same_blocks(block0, block3) && !is_same_blocks(block1, block3) && !is_same_blocks(block2, block3)) opt_blocks.push_back(block3);

  for (int i = 0; i < opt_blocks.size(); ++i) {
    for (auto indices : opt_blocks[i]) {
      if (indices.first == 0 && indices.second == 0) {
        zero_point[i] = true;
        break;
      }
    }
  }

  max_count = 0;
  num_black_in_block = opt_blocks[0].size();
  min_block_size = min(block_row, block_column);
}

int get_num_white_in_board(int start_h, int start_w) {
  int result = 0;

  for (int w = start_w; w < board_width; ++w) {
    if (board[start_h][w] == '.') ++result;
  } 

  for (int h = start_h+1; h < board_height; ++h) {
    for (int w = 0; w < board_width; ++w) {
      if (board[h][w] == '.') ++result;
    }
  }

  return result;
}

bool out_of_board_range(int h, int w) {
  if (h >= board_height || w >= board_width) return true;
  return false;
}

bool can_place(int h, int w, int n, vector<pair<int,int>> &revert_block) {
  for (auto indices : opt_blocks[n]) {
    int r = indices.first;
    int c = indices.second;
    
    if (out_of_board_range(h+r, w+c)) return false;
    if (board[h+r][w+c] == '#') return false;
    
    board[h+r][w+c] = '#';
    revert_block.emplace_back(make_pair(h+r, w+c));
  }

  return true;
}

void reset(vector<pair<int, int>> &revert_block) {
  for (auto indices : revert_block) {
    int h = indices.first;
    int w = indices.second;
    
    board[h][w] = '.';
  }
}

void find_max(int start_h, int start_w, int count, int num_white_in_board) {
  int h = start_h;
  int w = start_w;
  while (!out_of_board_range(h+min_block_size-1, w)) {
    int theoritical_count = count + num_white_in_board / num_black_in_block;
    if (max_count >= theoritical_count) { return; }
    for (int n = 0; n < opt_blocks.size(); ++n) {
      vector<pair<int,int>> placed;
      if (can_place(h, w, n, placed)) {
        int next_count = count + 1;
        int next_w = w + 1;
        int next_h = h;
        if (next_w == board_width) {
          next_h += 1; next_w = 0;
        } 

        int next_num_white_in_board = num_white_in_board - num_black_in_block;
        if (!zero_point[n]) next_num_white_in_board -= 1;
        
        if (next_count > max_count) { max_count = next_count; }

        find_max(next_h, next_w, next_count, next_num_white_in_board);
      }
      reset(placed);
    }
    if (board[h][w++] == '.') --num_white_in_board;
    if (w == board_width) { ++h; w = 0; } 
  }
  return;
}

void solution() {
  preprocess();
  find_max(0, 0, 0, get_num_white_in_board(0,0));
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
        cin >> block[r][c];
      }
    }

    solution();
  }
  return 0;
}
