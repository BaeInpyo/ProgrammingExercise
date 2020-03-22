#include<iostream>
#include<fstream>
#include<vector>
#include<cstring>
using namespace std;

inline int getLeftChildIndex(int index) {
    return index*2;
}
inline int getRightChildIndex(int index) {
    return index*2+1;
}

pair<int, int> initSTree(vector<pair<int, int>> &maxMinTree, const vector<int> &flags, int l, int r, int nodeIndex) {
    if (l+1 == r) return maxMinTree[nodeIndex] = make_pair(flags[l], flags[l]);
    int mid = (l+r)/2;
    auto lp = initSTree(maxMinTree, flags, l, mid, getLeftChildIndex(nodeIndex));
    auto rp = initSTree(maxMinTree, flags, mid, r, getRightChildIndex(nodeIndex));

    return maxMinTree[nodeIndex] = make_pair(max(lp.first, rp.first), min(lp.second, rp.second));
}

pair<int, int> getPair(const vector<pair<int, int>> &sTree, const int first, const int last, int nodeLeft, int nodeRight, int nodeIndex) {
    
    if (last <= nodeLeft || nodeRight <= first) 
        return make_pair(0, 987654321);
    
    if (first <= nodeLeft && nodeRight <= last) return sTree[nodeIndex];
    int mid = (nodeLeft+nodeRight) / 2;
    auto lp = getPair(sTree, first, last, nodeLeft, mid, getLeftChildIndex(nodeIndex));
    auto rp = getPair(sTree, first, last, mid, nodeRight, getRightChildIndex(nodeIndex));

    return make_pair(max(lp.first, rp.first), min(lp.second, rp.second));
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    #ifdef DEBUG
        freopen("input.txt", "r", stdin);
    #endif

    int n_cases;
    cin >> n_cases;

    while(n_cases--) {
        int n, q;
        cin >> n >> q;
        vector<int> flags;
        for (int i = 0; i < n; i++) {
            int temp;
            cin >> temp;
            flags.push_back(temp);
        }
        vector<pair<int, int>> sTree(4*n);
        initSTree(sTree, flags, 0, n, 1);

        for (int i = 0; i < q; i++) {
            int first, last;
            cin >> first >> last;
            auto p = getPair(sTree, first, last+1, 0, n, 1);
            cout << p.first - p.second << '\n';
        }
    }

    return 0;
}
