#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> status;
int G, H;
constexpr int NOT_VISITED = 0;
constexpr int VISITED = 1;
constexpr int WATCHED = 2;
constexpr int NOT_WATCHED = 3;
constexpr int INSTALLED = 4;

void dfs(int here) {
    status[here] = VISITED;
    int there;
    bool leaf = true;
    for (int there=0; there < G; there++) {
        if (graph[here][there]) {
            if (status[there] == NOT_VISITED) {
                dfs(there);
                leaf = false;
            }
        }
    }
    if (leaf) {
        status[here] = NOT_WATCHED;
    } else {
        for (int there=0; there < G; there++) {
            if (graph[here][there]) {
                switch (status[there]) {
                    case NOT_WATCHED:
                        status[here] = INSTALLED;
                        status[there] = WATCHED;
                        break;
                    case INSTALLED:
                        if (status[here] != INSTALLED) status[here] = WATCHED;
                        break;
                    default:
                        break;
                }
            }
        }
        if (status[here] == VISITED) status[here] = NOT_WATCHED;
    }
}

void init() {
    cin >> G >> H;
    graph = vector<vector<int>>(G, vector<int>(G, 0));
    status = vector<int>(G, NOT_VISITED);
}

void solution() {
    init();
    int here, there;
    for (int i=0; i<H; i++) {
        cin >> here >> there;
        graph[here][there]++;
        graph[there][here]++;
    }

    for (int i=0; i<G; i++)
        if (status[i] == NOT_VISITED)
            dfs(i);

    int installed = 0;
    for (int i=0; i<G; i++)
        if (status[i] == NOT_WATCHED || status[i] == INSTALLED)
            installed++;

    cout << installed << endl;
}

int main() {
    int C;
    cin >> C;
    while (C--) solution();
    return 0;
}

