#include <iostream>

using namespace std;

int num_tests;
int k;
string words[15];

void solution() {

}

int main() {
    cin.sync_with_stdio(false);
    cin >> num_tests;
    while (--num_tests >= 0) {
        cin >> k;
        for (int i = 0; i < k; i++) {
            cin >> words[i];
        }

        solution();
    }
}