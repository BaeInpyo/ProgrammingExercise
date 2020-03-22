#include <iostream>
#include <vector>
using namespace std;


/**
 * implementation of Binary Indexed Tree
 * methods : partialSum, update
 * [                 8]
 * [       4]
 * [  2]     [  6]
 * [1]  [3]  [5]  [7]
 */

// get sum in range of [0..i]
int partialSum(vector<int> &tree, int i) {
    int ret = 0;
    while (i > 0) {
        ret += tree[i];
        i -= (i & -i); // 15->14->12->8
    }
    return ret;
}

// update by adding diff
void update(vector<int> &tree, int i, int diff) {
    while (i < tree.size()) {
        tree[i] += diff;
        i += (i & -i); // 5->6->8->16
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif
    int C;
    cin >> C;
    while (C--) {  
        int n, i, val;
        cin >> n;
        long long ret = 0;
        vector<int> ftree(1000001); // ftree [1..n]
        for (i = 1; i <= n; i++) {
            cin >> val;
            ret += partialSum(ftree, 1000000) - partialSum(ftree, val+1);
            update(ftree, val+1, 1);
        }
        cout << ret << '\n';
    }
    return 0;
}
