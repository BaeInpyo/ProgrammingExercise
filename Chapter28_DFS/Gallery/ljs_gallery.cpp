#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> status;
int installed;
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
    bool alone = true;
    for (int there=0; there<graph[here].size(); there++) {
        if (graph[here][there]) {
            alone = false;
            if (status[there] == NOT_VISITED) {
                dfs(there);
                leaf = false;
            }
        }
    }
    if (alone) {
        status[here] = INSTALLED;
        installed++;
    } else if (leaf) {
        status[here] = NOT_WATCHED;
    } else {
        for (int there=0; there<graph[here].size(); there++) {
            if (graph[here][there]) {
                switch (status[there]) {
                    case NOT_WATCHED:
                        status[here] = INSTALLED;
                        installed++;
                        return;
                    case INSTALLED:
                        status[here] = WATCHED;
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
    installed = 0;
}

void solution() {
    init();
    int here, there;
    for (int i=0; i<H; i++) {
        cin >> here >> there;
        graph[here][there]++;
        graph[there][here]++;
    }

    for (int i=0; i<G; i++) {
        if (status[i] == NOT_VISITED) dfs(i);
    }

    cout << installed << endl;
}


int main() {
    int C;
    cin >> C;
    while (C--) solution();
    return 0;
}

