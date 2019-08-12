#include <iostream>

#define N 500
#define K 

int num_tests;
int n, k;
int seq[N];

void solution() {

}

int main() {
    cin >> num_tests;
    while (--num_tests > 0) {
        cin >> n; cin >> k;
        for (int i = 0; i < n; ++i) {
            cin >> seq[i];
        }
        solution();
    }
    return 0;
}