#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

static constexpr int MAX_N = 8;
unordered_map<string, int> dist;

void setup() {
    string s = "01234567";
    auto q = queue<string>({s});
    dist = unordered_map<string, int>{{s, 0}};
    while (!q.empty()) {
        auto here = q.front();
        q.pop();
        int cost = dist.at(here);
        for (int i = 0; i <= MAX_N-2; i++) {
            for (int j = i+2; j <= MAX_N; j++) {
                reverse(here.begin() + i, here.begin() + j);
                if (dist.find(here) == dist.end()) {
                    q.push(here);
                    dist.insert({here, cost+1});
                }
                reverse(here.begin() + i, here.begin() + j);
            }
        }
    }
}

void solution() {
    int N, n;
    cin >> N;
    vector<int> v, v_sorted;
    string normalized;

    for (int i=0; i<N; i++) {
        cin >> n;
        v.push_back(n);
    }

    v_sorted = vector<int>(v);
    sort(v_sorted.begin(), v_sorted.end());

    for (int i=0; i<MAX_N; i++) {
        if (i < N) n = distance(v_sorted.begin(), find(v_sorted.begin(), v_sorted.end(), v[i]));
        else n = i;
        normalized += static_cast<char>(n) + '0';
    }

    cout << dist[normalized] << endl;
}

int main() {
    int C;
    cin >> C;
    setup();
    while (C--) solution();
    return 0;
}

