#include <iostream>
#include <vector>

using namespace std;

void dfs(int n, vector<vector<int>>& graph, vector<int>& visited, vector<int>& order) {
    visited[n] = 1;
    for (int i=0; i<26; i++)
        if (graph[n][i] && !visited[i]) dfs(i, graph, visited, order);
    order.push_back(n);
}

void solution() {
    int n;
    cin >> n;
    auto graph = vector<vector<int>>(26, vector<int>(26, 0));
    string prev = "";
    string curr = "";
    while (n--) {
        cin >> curr;
        for (int i=0; i < min(prev.size(), curr.size()); i++)
            if (prev[i] != curr[i]) {
                graph[prev[i] - 'a'][curr[i] - 'a'] = 1;
                break;
            }
        prev = curr;
    }

    vector<int> visited = vector<int>(26, 0);
    vector<int> order;
    for (int i=0; i<26; i++)
        if (!visited[i]) dfs(i, graph, visited, order);
    for (int i=0; i<25; i++)
        if (graph[order[25-(i+1)]][order[25-i]]) {
            cout << "INVALID HYPOTHESIS" << endl;
            return;
        }
    string s = "";
    for (int i=0; i<26; i++) s += static_cast<char>(order[25-i] + 'a');
    cout << s << endl;
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
