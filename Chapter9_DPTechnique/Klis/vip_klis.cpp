#include <iostream>

using namespace std;

#define N 500

int num_tests;
int n, k;
int seq[N+1];
int answer[N+1];

int max_len[N+1];
int klis_next[N+1][N+1];
long long int count[N+1];

void init_cache() {
    for(int i = 0; i < n+1; ++i) {
        max_len[i] = 0;
        count[i] = 0;
        for (int j = 0; j < n+1; ++j) {
            klis_next[i][j] = -1;
        }
    }
}

void set_next(int start, int next_idx, bool init) {
    int count_temp = 0;
    if (init) {
        count[start] = 0;
        klis_next[start][0] = next_idx;
        for (int i = 1; i < n+1; ++i) {
            if (klis_next[start][i] == -1) break;
            klis_next[start][i] = -1;
        }
    } else {
        int i = 0;
        for (; i < n+1; ++i) {
            if (klis_next[start][i] == -1) break;
        }
        klis_next[start][i] = next_idx;
    }

    if (next_idx == n+1)
        count_temp = 1;
    else count_temp = count[next_idx];
    count[start] += count_temp;
}

int lis(int start) {
    int elem = seq[start];
    int &len = max_len[start];
    if (len != 0) return len;
    len = 1;
    for (int i = n; i > start; --i) {
        if (elem < seq[i]) {
            int temp_len = 1 + lis(i);
            if (len < temp_len) {
                len = temp_len;
                set_next(start, i, true);
            } else if (len == temp_len) {
                set_next(start, i, false);
            }
        }
    }
    if (len == 1) set_next(start, n+1, true);

    return len;
}

void find_answer() {
    int i = 0, j = 0;
    int ans_idx = 0;

    while (true) {
        int next_idx = klis_next[i][j];
        if (next_idx == n+1) break;
        int count_temp = count[next_idx];
        if (count_temp >= k) {
            i = next_idx;
            j = 0;
            answer[ans_idx++] = seq[next_idx];
        } else {
            k -= count_temp;
            ++j;
        }
    }
}

void solution() {
    init_cache();

    lis(0);

    find_answer();
    int answer_len = max_len[0] - 1;
    cout << answer_len << endl;
    for (int i = 0; i < answer_len; ++i) {
        cout << answer[i] << " ";
    }
    cout << endl;
}

int main() {
    cin >> num_tests;
    while (--num_tests >= 0) {
        cin >> n; cin >> k;
        seq[0] = -1;
        for (int i = 1; i <= n; ++i) {
            cin >> seq[i];
        }
        solution();
    }
    return 0;
}