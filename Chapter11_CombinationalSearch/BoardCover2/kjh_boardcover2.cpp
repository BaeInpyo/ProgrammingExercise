
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int H, W, R, C;
int board[10][10];
vector<pair<int, int>> blockPair[4];
int blockSize;
int locMax;
bool dupMark[4];

bool placeable(int r, int c, int dir, vector<pair<int, int>> &placed) {
    for (auto p: blockPair[dir]) {
        if (board[r+p.first][c+p.second] > 0) return false;
        else {
            board[r+p.first][c+p.second] = 2;
            placed.push_back(p);
        }
    }
    return true;
}

void placeBlock(int r, int c, int placed, int spaceLeft) {
    if (placed > locMax) locMax = placed;
    for (int k = 0; k < 4; k++) {
        if (dupMark[k]) continue;
        if (placed + spaceLeft/blockSize <= locMax)
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
        if (r + _R > H) continue;

        vector<pair<int, int>> toRecover;
        if (placeable(r, c, k, toRecover)) {
            placeBlock(r, c+1, placed + 1, spaceLeft - blockSize);
        }

        for (auto p: toRecover) {
            board[r+p.first][c+p.second] = 0;
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
        blockPair[0] = vector<pair<int, int>>();
        blockPair[1] = vector<pair<int, int>>();
        blockPair[2] = vector<pair<int, int>>();
        blockPair[3] = vector<pair<int, int>>();
        dupMark[0] = dupMark[1] = dupMark[2] = dupMark[3] = 0;
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
                if (val < '.') {
                    blockPair[0].emplace_back(make_pair(i,j));
                    blockPair[1].emplace_back(make_pair(j,R-i-1));
                    blockPair[2].emplace_back(make_pair(R-i-1,C-j-1));
                    blockPair[3].emplace_back(make_pair(C-j-1,i));
                    blockSize++;
                }
            }

        sort(blockPair[0].begin(), blockPair[0].end());
        sort(blockPair[1].begin(), blockPair[1].end());
        sort(blockPair[2].begin(), blockPair[2].end());
        sort(blockPair[3].begin(), blockPair[3].end());
        
        for (int i = 0; i < 3; i++)
            for (int j = i+1; j < 4; j++) {        
                if (!dupMark[j] && blockPair[i] == blockPair[j]) {
                    dupMark[j] = 1;
                }
            }
    
        placeBlock(0, 0, 0, spaces);
        cout << locMax << '\n';
    }
    return 0;
}
