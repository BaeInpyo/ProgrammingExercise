#include <iostream>
#include <vector>

using namespace std;

// #    #  ##  ##
// ##  ##   #  #

// N * Y * X
int shapes[4][3][2] = { { {0, 0}, {1, 0}, {1, 1} },
                        { {0, 0}, {1, 0}, {1, -1} },
                        { {0, 0}, {0, 1}, {1, 1} },
                        { {0, 0}, {0, 1}, {1, 0} } };

int height, width;
vector<vector<bool>> board;

int countWhiteInBoard() {
    int count = 0;
    for (int h_idx = 0; h_idx < height; h_idx++) {
        for (int w_idx = 0; w_idx < width; w_idx++) {
            if (!board[h_idx][w_idx]) count++;
        }
    }

    return count;
}

pair<int, int> getAnyWhitePos() {
    for (int h_idx = 0; h_idx < height; h_idx++) {
        for (int w_idx = 0; w_idx < width; w_idx++) {
            if (!board[h_idx][w_idx]) {
                return make_pair(h_idx, w_idx);
            }
        }
    }
}

bool checkPosition(int y, int x) {
    return (y >= 0 && y < height && x >= 0 && x < width && !board[y][x]);
}

int findNumberOfWay(int empty_count) {
    int count = 0;
    pair<int, int> white_pos;

    // Success
    if (empty_count == 0) return 1;

    white_pos = getAnyWhitePos();

    for (int i = 0; i < 4; i++) {
        int is_coloring_possible = true;
        int (*shape_L)[2] = shapes[i];
        for (int pos = 0; pos < 3; pos++) {
            int y = shape_L[pos][0] + white_pos.first;
            int x = shape_L[pos][1] + white_pos.second;
            if (!checkPosition(y,x)) {
                is_coloring_possible = false;
                break;
            }
        }

        if (is_coloring_possible) {
            // Coloring
            for (int pos = 0; pos < 3; pos++) {
                int y = shape_L[pos][0] + white_pos.first;
                int x = shape_L[pos][1] + white_pos.second;
                board[y][x] = true;
            }

            count += findNumberOfWay(empty_count - 3);

            // Revert
            for (int pos = 0; pos < 3; pos++) {
                int y = shape_L[pos][0] + white_pos.first;
                int x = shape_L[pos][1] + white_pos.second;
                board[y][x] = false;
            }
        }
    }

    return count;
}

int main() {

    cin >> height; cin >> width;
    board.resize(height, vector<bool>(width, false));

    for (int h_idx = 0; h_idx < height; h_idx++) {
        for (int w_idx = 0; w_idx < width; w_idx++) {
            char board_element;
            cin >> board_element;
            if (board_element == '#') {
                board[h_idx][w_idx] = true;
            }
        }
    }

    cout << findNumberOfWay(countWhiteInBoard()) << endl;

    return 0;
}
