#include <iostream>
#include <cstring>

using namespace std;

#define INVALID 123

int n, k, m, l;
unsigned int prereq[12];
unsigned int course[10];

int getAns(unsigned int took, int sem, int cnt) {
    if (__builtin_popcount(took) >= k) return cnt;
    if (sem >= m) return INVALID;

    unsigned int &courses = course[sem];
    unsigned int canTake = courses & ~took;

    for (int i = 0; i < n; i++) {
        if (canTake & (1 << i)) {
            if ((took & prereq[i]) < prereq[i])
                canTake ^= 1 << i;
        }
    }

    // iterate all subset
    unsigned int _itr = canTake;
    int ret = INVALID;
    while (_itr) {
        if (__builtin_popcount(_itr) <= l) {
            int res = getAns(took | _itr, sem+1, cnt+1);
            if (res < ret) ret = res;
        }
        _itr = (_itr-1) & canTake;
    }
    // skip semester
    int res = getAns(took, sem+1, cnt);
    if (res < ret) ret = res;
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int C;
    cin >> C;
    while (C--) {
        memset(prereq, 0, sizeof(prereq));
        memset(course, 0, sizeof(course));

        int i, j;
        cin >> n >> k >> m >> l;
        for (i = 0; i < n; i++) {
            int r;
            cin >> r;
            for (j = 0; j < r; j++) {
                int pre;
                cin >> pre;
                prereq[i] |= 1 << pre;
            }
        }
        for (i = 0; i < m; i++) {
            int c;
            cin >> c;
            for (j = 0; j < c; j++) {
                int open;
                cin >> open;
                course[i] |= 1 << open;
            }
        }

        int ans = getAns(0, 0, 0);
        if (ans == INVALID) cout << "IMPOSSIBLE\n";
        else cout << ans << '\n';
    }
    return 0;
}
