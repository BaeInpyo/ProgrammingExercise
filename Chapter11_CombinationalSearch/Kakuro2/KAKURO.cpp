#define DEBUG

#include <iostream>
#include <vector>

#include <cstring>
using namespace std;

int n, q;
int board[20][20];
int infoIdx[20][20][2];

struct INFO {
    int y, x, dir, sum, len, used = 0;
    INFO() {}
    INFO(int y, int x, int dir, int sum, int len, int used): 
        y(y), x(x), dir(dir), sum(sum), len(len), used(used) {}
};
vector<INFO> infos;

// length, sum, used
int candidates[10][46][1<<9];

void initCandidates() {
    for (int _set = 0; _set < 1<<9; _set++) {
        int _len = 0, _sum = 0;
        int i = 0;
        for (int t = _set; t; t >>= 1) {
            i++;
            if (t & 1) {
                _len++;
                _sum += i;
            }
        }
        
        int _subset = _set;
        candidates[_len][_sum][0] |= _set;
        while (_subset) {
            candidates[_len][_sum][_subset] |= (_set & ~_subset);
            _subset = (_subset-1) & _set;
        }
    }
}

bool search() {
    int cand = -1;
    int minLen = 10;
    int y, x;
    
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 0) {
                INFO &info1 = infos[infoIdx[i][j][0]];
                INFO &info2 = infos[infoIdx[i][j][1]];
                int _cand = candidates[info1.len][info1.sum][info1.used] &
                    candidates[info2.len][info2.sum][info2.used];
                int _len = 0;
                for (int t = _cand; t; t &= t-1) _len++;
                if (_len < minLen) {
                    minLen = _len;
                    cand = _cand;
                    y = i; x = j;
                }
            }
        }

    if (cand < 0) return 1;
    if (cand <= 0) return 0;

    int i = 0;
    INFO &hInfo = infos[infoIdx[y][x][0]];
    INFO &vInfo = infos[infoIdx[y][x][1]];

    for (int t = 1; t <= cand; t <<= 1) {
        i++;
        if (t & cand) {
            board[y][x] = i;
            hInfo.used |= t;
            vInfo.used |= t;
            if (search()) return 1;
            board[y][x] = 0;
            hInfo.used &= ~t;
            vInfo.used &= ~t;
        }
    }
    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifdef DEBUG
        freopen("input.txt", "r", stdin);
    #endif

    int T;
    cin>>T;
    memset(candidates, 0, sizeof(candidates));
    initCandidates();
    while(T--) {

        cin >> n;
        for (int i = 0; i < n; i++) 
            for (int j = 0; j < n; j++) {
                int b; 
                cin >> b;
                board[i][j] = (b > 0)? 0: -1;
                infoIdx[i][j][0] = infoIdx[i][j][1] = 0;
            }
        
        cin >> q;
        infos = vector<INFO>();
        for (int i = 0; i < q; i++) {
            int y, x, dir, _sum;
            cin >> y >> x >> dir >> _sum;

            infos.emplace_back(INFO(y, x, dir, _sum, 0, 0));
            int &len = infos.back().len;
            if (dir ^ 1) { 
                // horizontal
                y--;
                while (board[y][x] >= 0 && x < n) {
                    infoIdx[y][x][0] = i;
                    x++;
                    len++;
                }
            }
            else {
                // vertical
                x--;
                while (board[y][x] >= 0 && y < n) {
                    infoIdx[y][x][1] = i;
                    y++;
                    len++;
                }
            }
        }

        if (search()) 
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++)
                    if (board[i][j] > 0)
                        cout << board[i][j] << ' ';
                    else cout << 0 << ' ';
                cout << '\n';
            }
        else cout << "NO\n";
    }
    return 0;
}