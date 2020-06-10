#include <iostream>
#include <vector>
#include <algorithm>
#define INF 987654321

using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    #endif

    int v, e, a,b,c, t;
    cin >> v >> e;
    vector<int> delay(v, 0);
    vector<vector<int>> dist(v+1, vector<int>(v+1, INF));
    vector<vector<int>> bn(v+1, vector<int>(v+1, INF));
    auto idx = vector<int>(v+1, 0);
    for (int i = 1 ; i <= v; i++) {
        idx[i] = i;
        cin >> delay[i];
        bn[i][i] = dist[i][i] = 0;
    }
    for (int i = 0; i < e; i++) {
        cin >> a >> b >> c;
        dist[b][a] = dist[a][b] = c;
        bn[b][a] = bn[a][b] = c;
    }

    stable_sort(idx.begin(), idx.end(), [&delay](int a, int b){ return delay[a] < delay[b]; });

    for (int k_ = 1; k_ <= v; k_++) {
        int k = idx[k_];
        for (int i = 1; i <= v; i++) {
            for (int j = 1; j <= v; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                bn[i][j] = min(bn[i][j], dist[i][k] + dist[k][j] + delay[k]);
            }
        }
    }
    cin >> t;
    while (t--) {
        cin >> a >> b;
        cout << bn[a][b] << '\n';
    }
    return 0;
}
