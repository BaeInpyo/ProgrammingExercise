#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int r[1001], c[1001];

bool solValid(double x, int n, int k) {
    vector<double> v;
    for (int i = 0; i < n; i++) 
        v.push_back(x * c[i] - r[i]);
    sort(v.rbegin(), v.rend());
    double sum = 0;
    for (auto itr = v.begin(); itr != v.begin() + k; itr++) {
        sum += *itr;
        if (sum < 0) return false;
    }
    return true;
}

double getMinVal(int n, int k) {
    double hi = 1.0000001, lo = 0;
    for (int i = 0; i < 100; i++) {
        double mid = (hi + lo) /2;
        if (solValid(mid, n, k))
            hi = mid;
        else
            lo = mid;
    }
    return hi;
}

int main() {
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    #endif
    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++)
            cin >> r[i] >> c[i];
        cout << fixed << setprecision(10) << getMinVal(n, k) << '\n';
    }
    memset(r, 0, sizeof(r));
    memset(c, 0, sizeof(c));
    return 0;
}
