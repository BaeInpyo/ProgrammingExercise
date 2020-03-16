#include <iostream>
#include <vector>

using namespace std;

#define INT_MAX 1234567890

class RMQ {
    public :
        RMQ(const vector<int>& array) {
            n = array.size();
            rangeMin.resize(n * 4);
            init(array, 0, n - 1, 1);
        }

        int query(int left, int right) {
            return query(left, right, 1, 0, n - 1);
        }

    private :
        int init(const vector<int>& array, int left, int right, int node) {
            if (left == right)
                return rangeMin[node] = array[left];
            int mid = (left + right) / 2;
            int leftMin = init(array, left, mid, node * 2);
            int rightMin = init(array, mid + 1, right, node * 2 + 1);
            return rangeMin[node] = min(leftMin, rightMin);
        }

        int query(int left, int right, int node, int nodeLeft, int nodeRight) {
            if (right < nodeLeft || nodeRight < left) return INT_MAX;
            if (left <= nodeLeft && nodeRight <= right) return rangeMin[node];
            int mid = (nodeLeft + nodeRight) / 2;
            return min(query(left, right, node * 2, nodeLeft, mid),
                       query(left, right, node * 2 + 1, mid + 1, nodeRight));
        }

        int n;
        vector<int> rangeMin;
};

void solution() {
    int n, q;
    cin >> n >> q;
    vector<int> array;
    vector<int> negArray;
    while (n--) {
        int h;
        cin >> h;
        array.push_back(h);
        negArray.push_back(-h);
    }
    RMQ minTree = RMQ(array);
    RMQ negMaxTree = RMQ(negArray);
    while (q--) {
        int left, right;
        cin >> left >> right;
        cout << -(negMaxTree.query(left, right)) - minTree.query(left, right) << endl;
    }
}

int main() {
    int c;
    cin >> c;
    while (c--) solution();
    return 0;
}
