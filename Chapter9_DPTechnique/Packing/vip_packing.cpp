#include <iostream>

using namespace std;

int ith_test;
int n, w;
string items[100];
int weights[100];
int priority[100];

int result_priority_and_num[50][2];
bool result_set[50][100];

int cache[100][1000];
void init_cache() {
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j < 1000; ++j) {
            cache[i][j] = 0;
        }
    }
}
int packing(int start, int weight) {
    if (start == n) return 0;
    if (weight == 0) return 0;

    int &res = cache[start][weight];
    if (res != 0) return res;

    int max_idx = 0;
    for (int i = start; i < n; ++i) {
        if (weights[i] <= weight) {
            int partial_priority = priority[i] + packing(i+1, weight-weights[i]);
            if (res < partial_priority) {
                res = partial_priority;
                max_idx = i;
            }
        }
    }

    if (res != 0) {
        result_set[ith_test][max_idx] = true;
        result_priority_and_num[ith_test][1] += 1;
    }

    return res;
}

void solution() {
    init_cache();
    result_priority_and_num[ith_test][0] = packing(0, w);
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
        int max_priority = result_priority_and_num[i][0];
        int num_set = result_priority_and_num[i][1];
        cout << max_priority << " " << num_set << endl;
        for(int j = 0; j < num_set; ++j) {
            if (result_set[i][j]) {
                cout << items[j] << endl;
            }
        }
    }

    return 0;
}