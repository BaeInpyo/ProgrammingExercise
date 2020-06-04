#include <iostream>
#include <vector>

using namespace std;

const int UPPER_DEFAULT = 123456789;
const int CANNOT_REACH = 100000000;

int C, V, W, here_input, there_input, cost_input;

vector<vector<pair<int, int>>> adj;
vector<vector<pair<int, int>>> adj_minus;
vector<int> upper;

enum result { FOUND, UNREACHABLE, INFINITY };

result bellmanFord(int src, vector<vector<pair<int, int>>>& adj) {
    upper = vector<int>(V, UPPER_DEFAULT);
    upper[src] = 0;
    bool updated;
    for (int i=0; i<V; i++) {
        updated = false;
        for (int here=0; here < V; here++) {
            for (auto& p : adj[here]) {
                int there = p.first;
                int cost = p.second;
                if (upper[there] > upper[here] + cost) {
                    upper[there] = upper[here] + cost;
                    updated = true;
                }
            }
        }
        if (!updated) break;
    }
    bool andromeda_updated = false;
    if (updated) {
        for (int i=0; i<V; i++) {
            andromeda_updated = false;
            for (int here=0; here < V; here++) {
                for (auto& p : adj[here]) {
                    int there = p.first;
                    int cost = p.second;
                    if (upper[there] > upper[here] + cost) {
                        upper[there] = upper[here] + cost;
                        if (there == 1) {
                            andromeda_updated = true;
                        }
                    }
                }
            }
            if (andromeda_updated) break;
        }
    }

    if (upper[1] > CANNOT_REACH) return UNREACHABLE;
    else if (andromeda_updated) return INFINITY;
    else return FOUND;
}

void solution() {
    cin >> V >> W;
    adj = vector<vector<pair<int, int>>>(V, vector<pair<int, int>>()); // <there, cost>
    adj_minus = vector<vector<pair<int, int>>>(V, vector<pair<int, int>>()); // <there, cost>
    for (int i=0; i<W; i++) {
        cin >> here_input >> there_input >> cost_input;
        adj[here_input].push_back(make_pair(there_input, cost_input));
        adj_minus[here_input].push_back(make_pair(there_input, -cost_input));
    }
    auto res = bellmanFord(0, adj);
    if (res == INFINITY) cout << "INFINITY" << ' ';
    else if (res == FOUND) cout << upper[1] << ' ';
    else {
        cout << "UNREACHABLE" << endl;
        return;
    }

    res = bellmanFord(0, adj_minus);
    if (res == INFINITY) cout << "INFINITY" << endl;
    else cout << -upper[1] << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}
