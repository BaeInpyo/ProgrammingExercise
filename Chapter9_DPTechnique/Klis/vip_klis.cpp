#include <iostream>

using namespace std;

#define N 500

int num_tests;
int n, k, k_cnt;
int seq[N+1];
int recording[N+1];
int answer[N+1];
int max_len = 0;

void copy_to_answer() {
    for (int i = 0; i <= max_len; ++i) {
        answer[i] = recording[i];
    }
}

int lis(int start, int cnt) {
    int elem = seq[start];
    int len = 1;
    int max_len_internal = 1;
    recording[cnt] = elem;
    if (cnt > max_len) {
        max_len = cnt;
        k_cnt = k - 1;
        if (k_cnt == 0) {
            copy_to_answer();
        }
    } else if (cnt == max_len) {
        --k_cnt;
        if (k_cnt == 0) {
            copy_to_answer();
        }
    }
    
    for (int i = n; i > start; --i) {
        if (elem < seq[i]) {
            len = 1 + lis(i, cnt+1);
            max_len_internal = (max_len_internal < len) ? len : max_len_internal;
        }
    }
    return max_len_internal;
}

void solution() {
    lis(0, 0);

    cout << max_len << endl;
    for (int i = 1; i <= max_len; ++i) {
        cout << answer[i] << " ";
    }
    cout << endl;
}

int main() {
    cin >> num_tests;
    while (--num_tests >= 0) {
        cin >> n; cin >> k;
        seq[0] = -1;
        max_len = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> seq[i];
        }
        solution();
    }
    return 0;
}