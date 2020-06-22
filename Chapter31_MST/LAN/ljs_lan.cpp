#include <iostream>
#include <vector>
#include <math.h>

#define INF 987654321.0

using namespace std;

int C, N, M, a, b;

double distance(const pair<int, int>& b1, const pair<int, int>& b2) {
    return sqrt(pow((double)(b1.first - b2.first), 2) + pow((double)(b1.second - b2.second), 2));
}

void solution() {
    cin >> N >> M;
    auto coords = vector<pair<int, int>>(N);
    auto minDist = vector<double>(N, INF);
    auto parent = vector<int>(N, -1);
    auto added = vector<bool>(N, false);
    auto adj = vector<vector<double>>(N, vector<double>(N, INF));

    for (int i=0; i<N; i++) cin >> coords[i].first;
    for (int i=0; i<N; i++) cin >> coords[i].second;

    for (int i=0; i<N-1; i++)
        for (int j=i; j<N; j++)
            adj[i][j] = adj[j][i] = min(adj[i][j], distance(coords[i], coords[j]));

    for (int i=0; i<M; i++) {
        cin >> a >> b;
        adj[a][b] = adj[b][a] = 0;
    }

    parent[0] = minDist[0] = 0;
    double res = 0.0;

    for (int itr=0; itr<N; itr++) {
        int here = -1;
        for (int i=0; i<N; i++)
            if (!added[i] && (here == -1 || minDist[here] > minDist[i]))
                here = i;

        added[here] = true;
        res += minDist[here];

        for (int i=0; i<N; i++)
            if (!added[i] && minDist[i] > adj[here][i])
                minDist[i] = adj[here][i];
    }
    cout.precision(10);
    cout << res << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}
