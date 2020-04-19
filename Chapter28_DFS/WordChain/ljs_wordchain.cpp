#include <iostream>
#include <vector>

using namespace std;

#define ALP 26

void getEulerCircuit(int here, vector<vector<int>>& graph, vector<int>& circuit) {
    for (int there=0; there < graph[here].size(); there++) {
        while (graph[here][there] > 0) {
            graph[here][there]--;
            getEulerCircuit(there, graph, circuit);
        }
    }
    circuit.push_back(here);
}

void solution() {
    int N;
    cin >> N;
    string s;
    auto words = vector<string>();
    for (int i=0; i<N; i++) {
        cin >> s;
        words.push_back(s);
    }
    auto graph = vector<vector<int>>(ALP, vector<int>(ALP, 0));
    auto wordGraph = vector<vector<vector<string>>>(ALP, vector<vector<string>>(ALP, vector<string>()));
    auto indegree = vector<int>(ALP, 0);
    auto outdegree = vector<int>(ALP, 0);

    char head, tail;
    for (auto& word : words) {
        head = word[0];
        tail = word[word.size()-1];
        graph[head-'a'][tail-'a']++;
        wordGraph[head-'a'][tail-'a'].push_back(word);
        indegree[tail-'a']++;
        outdegree[head-'a']++;
    }

    int plus1 = 0, minus1 = 0, trailStart = -1;
    bool findTrail = false;
    bool findCircuit = false;

    for (int i=0; i<ALP; i++) {
        if (indegree[i] != outdegree[i]) {
            if (indegree[i] == outdegree[i] + 1)
                plus1++;
            if (outdegree[i] == indegree[i] + 1) {
                minus1++;
                trailStart = i;
            }
        }
    }

    findTrail = plus1 == 1 && minus1 == 1;
    findCircuit = plus1 == 0 && minus1 == 0;

    auto circuit = vector<int>();
    if (findTrail) {
        getEulerCircuit(trailStart, graph, circuit);
    } else if (findCircuit) {
        for (int i=0; i<ALP; i++) {
            if (outdegree[i]) {
                getEulerCircuit(i, graph, circuit);
                break;
            }
        }
    }
    if (circuit.size() == N+1)
        for (int i=0; i<N; i++) {
            auto head = circuit[N-i];
            auto tail = circuit[N-i-1];
            cout << wordGraph[head][tail].back() << ' ';
            wordGraph[head][tail].pop_back();
        }
    else
        cout << "IMPOSSIBLE";
    cout << endl;
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
