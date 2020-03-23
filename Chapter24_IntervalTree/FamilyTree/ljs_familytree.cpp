#include <iostream>
#include <vector>

using namespace std;

#define MAX_N 100000
#define MAX_Q 10000

void print(vector<int>& trip) {
    for (int i : trip) cout << i << ' ';
    cout << endl;
}
void visitPreOrder(int pos_f, int& pos_t, vector<vector<int> >& familyTree, vector<int>& trip) {
    trip[pos_t] = pos_f;
    print(trip);
    cout << pos_f << ' ' << pos_t << endl;
    pos_t++;
    if (familyTree[pos_f].empty()) return;
    for (int child : familyTree[pos_f]) {
        visitPreOrder(child, pos_t, familyTree, trip);
        trip[pos_t] = pos_f;
        pos_t++;
    }
    return;
}
void print(vector<vector<int> >& mat) {
    int k = 0;
    for (vector<int> v : mat) {
        cout << '[' << k++ << "] ";
        for (int i : v) cout << i << ' ';
        cout << endl;
    }
}

void solution() {
    int n, q;
    cin >> n >> q;
    vector<vector<int> > familyTree(n + 1, vector<int>());
    for (int i = 1; i < n; i++) {
        int father;
        cin >> father;
        familyTree[father].push_back(i);
    }
    vector<int> trip(2 * n - 1);
    print(familyTree);
    int pos_t = 0;
    visitPreOrder(0, pos_t, familyTree, trip); // fill trip
}

        

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
