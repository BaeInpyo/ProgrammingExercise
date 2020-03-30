#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAX = 100000;

int parents[MAX][20];
vector<int> children[MAX];
int depth[MAX];

void preproc(int here) {
    for (int i = 0; i < children[here].size(); i++) {
        int curr = children[here][i];
        depth[curr] = depth[here] + 1;
        for (int j = 1; j < 20; j++) {
            int prnt = parents[curr][j-1];
            if (prnt == -1) break;
            parents[curr][j] = parents[prnt][j-1];
        }
        preproc(curr);
    }
}

int dist(int _a, int _b) {
    int a = _a, b = _b;

    if (depth[a] < depth[b]) {
        int tmp = a; a = b; b = tmp;
    } // a is deeper
    for (int i = 19; i >= 0; i--) {
        if (depth[parents[a][i]] >= depth[b])
            a = parents[a][i];
    }
    int cp = a;
    if (a != b) {
        for (int i = 19; i >= 0; i--) {
            if (parents[a][i] != parents[b][i]) {
                a = parents[a][i];
                b = parents[b][i];
            }
            cp = parents[a][i];
        }
    }
    return depth[_a] - depth[cp] + depth[_b] - depth[cp];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    #endif

    int C;
    cin >> C;
    while (C--) {
        int n, q;
        int i;
        cin >> n >> q;
        memset(parents, 0, sizeof(parents));
        memset(children, 0, sizeof(children));
        memset(depth, 0, sizeof(depth));
        for (i = 1; i < n; i++) {
            int t;
            cin >> t;
            parents[i][0] = t;
            children[t].push_back(i);
        }
        preproc(0);

        for (i = 0; i < q; i++) {
            int a, b;
            cin >> a >> b;
            cout << dist(a, b) << '\n';
        }


    }
    return 0;
}
