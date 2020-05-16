#include <iostream>
#include <queue>
#include <vector>
#include <math.h>

#define INF 9876543210

using namespace std;

int C, N, M, input_here, input_there;
long double input_noise; 

void solution() {
    cin >> N >> M;
    auto adj = vector<vector<pair<long double, int>>>(N, vector<pair<long double, int>>());
    for (int i=0; i<M; i++) {
        cin >> input_here >> input_there >> input_noise;
        adj[input_here].push_back(make_pair(log(input_noise), input_there));
    }
    auto dist = vector<long double>(N, INF);
    auto q = priority_queue<pair<long double, int>>();
    q.push(make_pair(0.0f, 0));
    dist[0] = 0.0f;
    while (!q.empty()) {
        auto [dist_here, here] = q.top();
        q.pop();
        if (-dist_here > dist[here]) continue;
        for (auto& [noise_there, there] : adj[here]) {
            auto dist_there = -dist_here + noise_there;
            if (dist_there < dist[there]) {
                dist[there] = dist_there;
                q.push(make_pair(-dist_there, there));
            }
        }
    }
    printf("%.10Lf\n", exp(dist[N-1]));
}

int main() {
    cin >> C;
    while (C--) solution();
    return 0;
}
