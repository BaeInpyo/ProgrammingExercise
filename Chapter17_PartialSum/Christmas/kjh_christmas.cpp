#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int DIVISOR = 20091101;

int getFirstAnswer(vector<int> &v, int k) {
    int ret = 0;
    vector<long long> count(k, 0);

    for (auto itr = v.begin(); itr != v.end(); itr++) {
        count[*itr]++;
    }
    for (int i = 0; i < k; i++)
        if (count[i] >= 2)
            ret = (ret + ((count[i] * (count[i]-1)) / 2)) % DIVISOR;
    return ret;
}

int getSecondAnswer(const vector<int> &v, int k) {
    vector<int> prev(k, -1);
    vector<int> ret;
    ret.push_back(0);

    for (int i = 0; i < v.size(); i++) {
        if (i > 0)
            ret.push_back(ret.back());
        int &ref = prev[v[i]];
        if (ref != -1) ret[i] = max(ret[i], ret[ref] + 1);
        ref = i;
    }
    return ret.back();
}  

int main() {
    ios::sync_with_stdio(false);
    int nCases;
    cin >> nCases;

    while (nCases--) {
        int n, k;
        cin >> n >> k;
        int sum = 0;
        vector<int> remainderVector;
        remainderVector.push_back(0);
        for (int i = 0; i < n; i++) {
            int t;
            cin >> t;
            sum += t;
            sum %= k;
            remainderVector.push_back(sum);
        }
        cout << getFirstAnswer(remainderVector, k) << " " << getSecondAnswer(remainderVector, k) << '\n';
        
    }
    return 0;
}
