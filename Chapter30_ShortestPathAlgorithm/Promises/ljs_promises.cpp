#include <iostream>
#include <vector>

#define INF 987654321

using namespace std;

int C, V, M, N, a, b, c, res;
vector<vector<int>> adj;

void solution() {
    cin >> V >> M >> N;
    adj = vector<vector<int>>(V, vector<int>(V, INF));
    res = 0;
    for (int i=0; i<V; i++) adj[i][i] = 0;
    for (int i=0; i<M; i++) {
        cin >> a >> b >> c;
        adj[a][b] = adj[b][a] = c;
    }
    for (int k=0; k<V; k++)
        for (int i=0; i<V; i++)
            for (int j=0; j<V; j++)
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);

    for (int k=0; k<N; k++) {
        cin >> a >> b >> c;
        if (adj[a][b] <= c) {
            res++;
            continue;
        }
        adj[a][b] = adj[b][a] = c;
        for (int i=0; i<V; i++)
            for (int j=0; j<V; j++)
                adj[i][j] = adj[j][i] = min(adj[i][j], min(adj[i][a] + adj[a][b] + adj[b][j],
                                                           adj[i][b] + adj[b][a] + adj[a][j]));
    }
    cout << res << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}
