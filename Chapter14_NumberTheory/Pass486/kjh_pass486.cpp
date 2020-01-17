#include <iostream>

using namespace std;

const int HIGH = 10000000;
const int SQRT_HIGH = 3163;

int divs[HIGH+1];

void preprocess() {
    int i, j;
    divs[0] = 0;
    divs[1] = 1;
    for (i = 1; i <= HIGH; i++) 
        divs[i] = 2;
    for (i = 2; i < SQRT_HIGH; i++) {
        divs[i*i] += 1;
        for (j = i*i+i; j <= HIGH; j+=i) {
            divs[j] += 2;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif
    int c;
    cin >> c;
    int i;
    int n, lo, hi;
    int cnt;
    preprocess();
    while (c--) {
        cin >> n >> lo >> hi;
        cnt = 0;
        for (i = lo; i <= hi; i++) {
            if (divs[i] == n) cnt += 1;

        }
        cout << cnt << '\n';
    }
    return 0;
}
