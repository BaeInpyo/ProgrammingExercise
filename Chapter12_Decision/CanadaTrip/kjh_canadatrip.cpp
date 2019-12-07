#include <iostream>
#include <cstring>

using namespace std;

int l[5000], m[5000], g[5000];

bool hasSolution(const int n, int d, const int k) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        int _l = l[i], _m = m[i], _g = g[i];
        int start = _l - _m;
        if (d < start) continue;
        cnt += (min(_l, d) - start) / _g + 1;
        if (cnt >= k) return true;
    }
    return false;
}

int getLocation(const int n, const int k) {
    int hi =  8030000, lo = 0;

    for (int it = 0; it < 100; it++) {
        int mid = (hi + lo) /2;
        if (hasSolution(n, mid, k)) 
            hi = mid;
        else 
            lo = mid;
    }
    return hi;
}

int main() {
        ios::sync_with_stdio(false);  
    cin.tie(NULL);
    cout.tie(NULL);
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif
    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++)
            cin >> l[i] >> m[i] >> g[i];
        cout << getLocation(n, k) << '\n';
        memset(l, -1, sizeof(l));
        memset(m, -1, sizeof(m));
        memset(g, -1, sizeof(g));
    }
    return 0;

}
