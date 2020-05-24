#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int C, V/*places*/, E/*roads*/, N/*fires*/, M/*firestations*/;
const int INF = 987654321;

void solution() {
    cin >> V >> E >> N >> M;
    int input_a, input_b, input_m;
    auto adj = vector<vector<pair<int, int>>>(V+1, vector<pair<int, int>>());
    auto fires = vector<int>();
    auto fire_stations = vector<int>();
    for (int i=0; i<E; i++) {
        cin >> input_a >> input_b >> input_m;
        adj[input_a].push_back(make_pair(input_m, input_b));
        adj[input_b].push_back(make_pair(input_m, input_a));
    }
    for (int i=0; i<N; i++) {
        cin >> input_a;
        fires.push_back(input_a);
    }
    for (int i=0; i<M; i++) {
        cin >> input_a;
        fire_stations.push_back(input_a);
    }
    for (auto fs : fire_stations) adj[0].push_back(make_pair(0, fs));
    auto dist = vector<int>(V+1, INF);
    auto q = priority_queue<pair<int, int>>();
    dist[0] = 0;
    q.push(make_pair(0, 0));
    while (!q.empty()) {
        int here = q.top().second;
        int dist_here = q.top().first;
        q.pop();
        if (-dist_here > dist[here]) continue;
        for (auto& p : adj[here]) {
            int there = p.second;
            int dist_there = -dist_here + p.first;
            if (dist_there < dist[there]) {
                dist[there] = dist_there;
                q.push(make_pair(-dist_there, there));
            }
        }
    }
    int res = 0;
    for (auto f : fires) res += dist[f];
    cout << res << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}
