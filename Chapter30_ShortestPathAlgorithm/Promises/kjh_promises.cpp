#include <iostream>
#include <vector>
#include <algorithm>
#define INF (100000 * 201)

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    #endif

    int t;
    cin >> t;
    while (t--) {
        int v, n, m;
        cin >> v >> m >> n;
        auto dist = vector<vector<int>>(v, vector<int>(v, INF));
        for (int i = 0; i < v; i++) dist[i][i] = 0;
        for (int i = 0; i < m; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            if (dist[a][b] > c)
                dist[a][b] = dist[b][a] = c;
        }
        for (int k = 0; k < v; k++)
            for (int i = 0; i < v; i++)
                for (int j = 0; j < v; j++)
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j]);

        int ret = 0;
        for (int k = 0; k < n; k++) {
            int a, b, c;
            cin >> a >> b >> c;
            if (dist[a][b] <= c) {
                ret += 1;
                continue;
            }

            for (int i = 0; i < v; i++)
                for (int j = 0; j < v; j++)
                    dist[i][j] = min(dist[i][b] + dist[a][j] + c, min(dist[i][a] + dist[b][j] + c, dist[i][j]));
        }
        cout << ret << '\n';
    }

    return 0;
}
