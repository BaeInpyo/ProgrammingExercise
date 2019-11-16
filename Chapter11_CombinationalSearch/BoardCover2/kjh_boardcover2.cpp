#define DEBUG
#include <iostream>

using namespace std;

int H, W, R, C;
int board[10][10];
int block[4][10][10];
int blockSize;
int locMax;

bool placeable(int r, int c, int dir) {
    int _R, _C;
    if (dir & 1) {
        _R = C;
        _C = R;
    }
    else {
        _R = R;
        _C = C;
    }
    for (int i = 0; i < _R; i++)
        for (int j = 0; j < _C; j++) {
            int _r = r + i;
            int _c = c + j;
            if (_r >= H || _c >= W) return false;
            if (block[dir][i][j] > 0 && board[_r][_c] > 0) return false;
        }
    return true;
}

void placeBlock(int r, int c, int placed, int spaceLeft) {
    for (int k = 0; k < 4; k++) {
        if (placed + spaceLeft/blockSize < locMax)
            return;
        int _R, _C;
        if (k & 1) {
            _R = C;
            _C = R;
        }
        else {
            _R = R;
            _C = C;
        }       

        if (c + _C > W) return placeBlock(r+1, 0, placed, spaceLeft);
        if (r + _R > H) {
            if (placed > locMax) locMax = placed;
            return;
        }

        if (placeable(r, c, k)) {

            for (int i = 0; i < _R; i++)
                for (int j = 0; j < _C; j++) {
                    int _r = r + i;
                    int _c = c + j;
                    if (block[k][i][j] > 0) board[_r][_c] = 2;
                }
            placeBlock(r, c+1, placed + 1, spaceLeft - blockSize);
            for (int i = 0; i < _R; i++)
                for (int j = 0; j < _C; j++) {
                    int _r = r + i;
                    int _c = c + j;
                    if (block[k][i][j] > 0) board[_r][_c] = 0;
                }

        }
    }
    if (placed + spaceLeft/blockSize < locMax)
        return;
    if (board[r][c] > 0)
        placeBlock(r, c+1, placed, spaceLeft);
    else placeBlock(r, c+1, placed, spaceLeft-1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifdef DEBUG
        freopen("input.txt", "r", stdin);       
    #endif
    int T;
    cin >> T;
    while (T--) {

        cin >> H >> W >> R >> C;
        locMax = 0;
        blockSize = 0;
        int spaces = 0;
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++) {
                char val;
                cin >> val;
                if (val > '#') spaces++;
                board[i][j] = (val > '#')? 0:1;
            }
        for (int i = 0; i < R; i++) 
            for (int j = 0 ; j < C; j++) {
                char val;
                cin >> val;
                block[0][i][j] = block[1][j][R-i-1] = block[2][R-i-1][C-j-1]
                    = block[3][C-j-1][i] = (val > '#')? 0:1;
                if (val < '.') blockSize++;
            }
    
        placeBlock(0, 0, 0, spaces);
        cout << locMax << '\n';
    }
    return 0;
}
