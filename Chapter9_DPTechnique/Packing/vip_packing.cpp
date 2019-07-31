#include <iostream>

using namespace std;

int ith_test;
int n, w;
string items[100];
int weights[100];
int priority[100];

int result_priority_and_count[50][2];
bool result_set[50][100];

int cache[100][1000][2];
void init_cache() {
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j < 1000; ++j) {
            cache[i][j][0] = 0;
            cache[i][j][1] = 0;
        }
    }
}

int packing(int start, int weight) {
    if (start == n) return 0;
    if (weight == 0) return 0;

    int &res = cache[start][weight][0];
    int &max_idx = cache[start][weight][1];
    if (res != 0) return res;

    for (int i = start; i < n; ++i) {
        if (weights[i] <= weight) {
            int partial_priority = priority[i] + packing(i+1, weight-weights[i]);
            if (res < partial_priority) {
                res = partial_priority;
                max_idx = i;
            }
        }
    }

    return res;
}

void find_path() {
    int idx = 0;
    int weight = w;
    int total_priority = 0;
    int count = 0;
    while (total_priority != result_priority_and_count[ith_test][0]) {
        idx = cache[idx][weight][1];
        result_set[ith_test][idx] = true;
        count++;
        weight -= weights[idx];
        total_priority += priority[idx];
        idx += 1;
    }
    result_priority_and_count[ith_test][1] = count;
}

void solution() {
    init_cache();
    result_priority_and_count[ith_test][0] = packing(0, w);
    find_path();
}

int main() {
    int num_tests;
    cin >> num_tests;

    for (ith_test = 0; ith_test < num_tests; ++ith_test) {
        cin >> n; cin >> w;
        for (int j = 0; j < n; ++j) {
            cin >> items[j];
            cin >> weights[j];
            cin >> priority[j];
        }
        
        solution();
    }

    for (int i = 0; i < num_tests; ++i) {
        int max_priority = result_priority_and_count[i][0];
        int num_set = result_priority_and_count[i][1];
        cout << max_priority << " " << num_set << endl;
        for(int j = 0; j < n; ++j) {
            if (result_set[i][j]) {
                cout << items[j] << endl;
            }
        }
    }

    return 0;
}