#include <iostream>

#define MOD 1000000007

using namespace std;

int *n_array;

int cache_sym[101] = { 0 };
int tiling_sym(int n) {
    int &res = cache_sym[n];
    if (n <= 1) return 1;
    if (res != 0) return res;

    res = (tiling_sym(n-1) + tiling_sym(n-2)) % MOD;

    return res;
}

int cache_asym[101] = { 0 };
int tiling_asym(int n) {
    int &res = cache_asym[n];
    if (n <= 2) return 0;
    if (res != 0) return res;

    res = (tiling_sym(n-3) * 2) % MOD;
    res = (res + tiling_asym(n-2)) % MOD;
    res = (res + tiling_asym(n-4)) % MOD;

    return res;
}

int main() {
    int num_tests;
    cin >> num_tests;

    n_array = new int[num_tests];
    for (int i=0; i<num_tests; i++) {
        cin >> n_array[i];
    }

    for (int i=0; i<num_tests; i++) {
        cout << tiling_asym(n_array[i]) << endl;
    }
    return 0;
}