#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

static constexpr int FACT8 = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1;
static constexpr int MAX_N = 8;
map<vector<int>, int> dist;

void setup() {
    auto v = vector<int>{ 0, 1, 2, 3, 4, 5, 6, 7 };
    auto q = queue<vector<int>>({v});
    dist = map<vector<int>, int>{{v, 0}};
    while (!q.empty()) {
        auto here = q.front();
        q.pop();
        int cost = dist.at(here);
        for (int i = 0; i <= MAX_N-2; i++) {
            for (int j = i+2; j <= MAX_N; j++) {
                reverse(here.begin() + i, here.begin() + j);
                if (dist.find(here) == dist.end()) {
                    q.push(here);
                    dist.insert(pair<vector<int>, int>(here, cost+1));
                }
                reverse(here.begin() + i, here.begin() + j);
            }
        }
    }
}

void solution() {
    int N, n;
    cin >> N;
    vector<int> v, v_sorted, v_matched;

    for (int i=0; i<N; i++) {
        cin >> n;
        v.push_back(n);
    }

    v_sorted = vector<int>(v);
    sort(v_sorted.begin(), v_sorted.end());

    for (int i=0; i<MAX_N; i++) {
        if (i < N) v_matched.push_back(distance(v_sorted.begin(), find(v_sorted.begin(), v_sorted.end(), v[i])));
        else v_matched.push_back(i);
    }

    cout << dist[v_matched] << endl;
}

int main() {
    int C;
    cin >> C;
    setup();
    while (C--) solution();
    return 0;
}

