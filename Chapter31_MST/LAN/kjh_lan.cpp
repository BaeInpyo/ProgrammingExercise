#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <iomanip>

using namespace std;

vector<int> xs, ys;
int n, m;

inline double dist(int v, int u) {
    int x = xs[v] - xs[u];
    int y = ys[v] - ys[u];
    return sqrt(x*x+y*y);
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
        cin >> n >> m;
        xs = vector<int>(n);
        ys = vector<int>(n);
        auto dists = vector<vector<double>>(n, vector<double>(n));
        auto minDists = vector<double>(n, 1000005);
        for (int i = 0; i < n; i++) cin >> xs[i];
        for (int i = 0; i < n; i++) cin >> ys[i];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                dists[i][j] = dists[j][i] = dist(i, j);
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            dists[u][v] = dists[v][u] = 0;
        }
        double ret = 0;
        vector<int> visited = vector<int>(n, 0);
        minDists[0] = 0;
        for (int i = 0; i < n; i++) {
            int next = -1;
            double minDist = 1000005;
            for (int there = 0; there < n; there++)
                if (visited[there] == 0 && minDist > minDists[there]) {
                    next = there;
                    minDist = minDists[there];
                }
            visited[next] = 1;
            ret += minDist;
            for (int i = 0;i < n; i++) {
                minDists[i] = min(minDists[i], dists[next][i]);
            }
        }
        cout << setprecision(12) << ret << '\n';
    }
    return 0;
}
