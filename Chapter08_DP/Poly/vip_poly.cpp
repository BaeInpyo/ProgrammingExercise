#include <iostream>

using namespace std;

#define MAX 10000000

int num_tests;
int res[50];

int cache[101][101];
void init_cache() {
    for (int i=0; i<101; i++) {
        for (int j=0; j<101; j++) {
            cache[i][j] = -1;
        }
    }
}

/*
 * Calculate number of ways using n blocks where s blocks are in first layer
 * n: total number of blocks
 * s: number of blocks in first layer
 */
int poly_internal(int n, int s) {
    if (n == s) return 1;
    int &res = cache[n][s];
    if (res != -1) return res;

    res = 0;
    for (int i=1; i<n-s+1; i++) {
        // s+i-1: number of ways to locate 'poly_internal(n-s, i)' 
        // with s blocks in first layer
        res += poly_internal(n-s, i) * (s+i-1);
        res = (res >= MAX) ? res % MAX : res;
    }
    return res;
}

/*
 * Calculate the number of poly ways using n blocks
 */
int poly(int n) {
    if (n <= 2) return n;

    init_cache();
    int res = 0;
    // Result is the sum of poly_internal from 1 to n
    for (int i = 1; i <= n; i++) {
        res += poly_internal(n, i);
        res = (res >= MAX) ? res % MAX : res;
    }
    return res;
}

int main() {
    cin >> num_tests;

    for (int i=0; i<num_tests; i++) {
        int n;
        cin >> n;
        res[i] = poly(n);
    }

    for (int i=0; i<num_tests; i++) {
        cout << res[i] << endl;
    }

    return 0;
}