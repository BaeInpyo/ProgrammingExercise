#include <iostream>

#define N 50
#define INIT 1000000

using namespace std;

int num_tests;
int n;
int numbers[N];

// First index, Last index, Turn (0: 현우, 1: 서하)
int score_cache[N][N][2];
void init_cache() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            score_cache[i][j][0] = INIT;
            score_cache[i][j][1] = INIT;
        }
    }
}

// first and last index and turn: 50x50x2 - score.
// Closed range in both ways.
int calculate(int first_index, int last_index, int turn) {
    if (first_index > last_index) {
        return 0;
    }
    int &score = score_cache[first_index][last_index][turn];
    if (score != INIT) return score;

    int len = last_index - first_index + 1;    
    if (len == 1) {
        score = numbers[first_index];
    } else {
        int first_case_score;
        int second_case_score;
        int third_case_score;
        int fourth_case_score;
        // 1. Take and remove one of numbers of any edges.
        first_case_score = numbers[first_index] - calculate(first_index+1, last_index, 1-turn);
        second_case_score = numbers[last_index] - calculate(first_index, last_index-1, 1-turn);
        score = max(first_case_score, second_case_score);

        // 2. Or just remove two consecutive numbers of any edges.
        third_case_score = -1 * calculate(first_index+2, last_index, 1-turn);
        fourth_case_score = -1 *calculate(first_index, last_index-2, 1-turn);
        score = max(score, third_case_score);
        score = max(score, fourth_case_score);
    }
    return score;
}

void solution() {
    init_cache();
    int score_diff = calculate(0, n-1, 0);
    cout << score_diff << endl;
}

int main() {
    cin.sync_with_stdio(false);
    cin >> num_tests;

    while (--num_tests >= 0) {
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> numbers[i];
        }

        solution();
    }
}
