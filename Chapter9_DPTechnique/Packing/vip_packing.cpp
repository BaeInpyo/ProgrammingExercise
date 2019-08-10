#include <iostream>

using namespace std;

int n, w;
string items[100];
int weights[100];
int priority[100];

int result_priority;
int result_count;
bool result_set[100];

int cache[100][1000][2];
void init_cache() {
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j < 1000; ++j) {
            cache[i][j][0] = -1;
            cache[i][j][1] = -1;
        }
        result_set[i] = false;
    }
    result_priority = 0;
    result_count = 0;
}

int packing(int start, int weight) {
    if (start == n) return 0;
    if (weight == 0) return 0;

    int &res = cache[start][weight][0];
    int &max_idx = cache[start][weight][1];
    if (res != -1) return res;

    res = 0;
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
    while (total_priority != result_priority) {
        idx = cache[idx][weight][1];
        result_set[idx] = true;
        count++;
        weight -= weights[idx];
        total_priority += priority[idx];
        idx += 1;
    }
    result_count = count;
}

void solution() {
    init_cache();
    result_priority = packing(0, w);
    find_path();
}

int main() {
    int num_tests;
    cin >> num_tests;

    for (int i = 0; i < num_tests; ++i) {
        cin >> n; cin >> w;
        for (int j = 0; j < n; ++j) {
            cin >> items[j];
            cin >> weights[j];
            cin >> priority[j];
        }
        
        solution();

        cout << result_priority << " " << result_count << endl;
        for(int j = 0; j < n; ++j) {
            if (result_set[j]) {
                cout << items[j] << endl;
            }
        }
    }

    return 0;
}