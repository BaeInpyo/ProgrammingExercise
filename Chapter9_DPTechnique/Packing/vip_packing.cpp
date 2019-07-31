#include <iostream>

using namespace std;

int ith_test;
int n, w;
string items[100];
int weights[100];
int priority[100];

int result_priority_and_num[50][2];
int result_set[50][100];

void packing() {

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
        
        packing();
    }

    for (int i = 0; i < num_tests; ++i) {
        int max_priority = result_priority_and_num[i][0];
        int num_set = result_priority_and_num[i][1];
        cout << max_priority << " " << num_set << endl;
        for(int j = 0; j < num_set; ++j) {
            int idx = result_set[i][j];
            cout << items[idx] << endl;
        }
    }

    return 0;
}