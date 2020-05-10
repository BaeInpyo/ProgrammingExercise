#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

#define MAX_DISCS 12
#define INF 1234567890

// there are 4^MAX_DISCS of states
// for each 12 discs, each of them can be at 1~4th pillar
int cost[1 << (MAX_DISCS*2)];
int N;

// state look like below
// 0b....00011100
// each Nth two bits from right represents where the Nth disc is at
// e.g. if the rightmost two bits are 00, it means 1th disc is now at 1th pillar
int get(int state, int idx) { return (state >> (idx*2)) & 0b11; }
int set(int state, int idx, int value) { return (state & ~(0b11 << (idx*2))) | (value << (idx*2)); }

void bfs(int begin, int end) {
    auto q = queue<int>{ { begin } };
    cost[begin] = 0;
    while (!q.empty()) {
        auto& here = q.front();
        q.pop();
        int top[4] = { INF, INF, INF, INF };
        for (int i = N-1; i >= 0; --i)
            top[get(here, i)] = i;
        for (int i=0; i<4; ++i) {
            for (int j=0; j<4; ++j) {
                if (i != j && top[i] < top[j]) {
                    auto there = set(here, top[i], j);
                    if (cost[there] == -1) {
                        cost[there] = cost[here] + 1;
                        if (there == end) {
                            cout << cost[there] << endl;
                            return;
                        }
                        q.push(there);
                    }
                }
            }
        }
    }
    // cout << "FAILED" << endl;
}

int getState() {
    int ret = 0;
    int n, disc;
    for (int i=0; i<4; ++i) {
        cin >> n;
        while (n--) {
            cin >> disc;
            ret = set(ret, disc-1, i);
        }
    }
    return ret;
}

void solution() {
    memset(cost, -1, sizeof(cost));
    cin >> N;
    int begin = getState();
    int end = getState();
    bfs(begin, end);
}

int main() {
    int C;
    cin >> C;
    while (C--) solution();
    return 0;
}
