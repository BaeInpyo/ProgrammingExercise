#include <iostream>
#include <vector>

using namespace std;

#define MAX_INPUT 1000000

struct FenwickTree {
    vector<int> tree;
    FenwickTree(int n) : tree(n + 1) {}
    int sum(int pos) {
        pos++;
        int result = 0;
        while (pos) {
            result += tree[pos];
            pos &= (pos - 1); // remove rightmost bit to find next range to sum
        }
        return result;
    }
    void add(int pos, int val) {
        pos++;
        while (pos < tree.size()) {
            tree[pos] += val;
            pos += (pos & -pos); // add rightmost bit to itself to find corresponding ranges
        }
    }
};

void solution() {
    int n;
    long long result = 0;
    cin >> n;
    FenwickTree f(MAX_INPUT);
    for (int i = 0; i < n; i++) {
        int input;
        cin >> input;
        f.add(input, 1);
        result += (f.sum(MAX_INPUT - 1) - f.sum(input));
    }
    cout << result << endl;
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
