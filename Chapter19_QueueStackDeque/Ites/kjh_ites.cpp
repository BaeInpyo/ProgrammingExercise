#include <iostream>

using namespace std;

inline unsigned int next(unsigned int curr) {
    return curr * 214013u + 2531011u;
}

inline int signal(unsigned int raw) {
    return raw % 10000 + 1;
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
        int k, n;
        cin >> k >> n;
        int window_sum = 0;
        int prev = 1983, curr = 1983;
        int ret = 0;

        for (int i = 0; i < n; i++) {
            int sig = signal(curr);
            window_sum += sig;
            while (window_sum > k) {
                window_sum -= signal(prev);
                prev = next(prev);
            }
            if (window_sum == k) ret++;

            curr = next(curr);
        }
        cout << ret << '\n';
    }
    return 0;
}
