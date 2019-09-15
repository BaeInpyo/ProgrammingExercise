#include <iostream>

#define N 50
#define INIT -100000000

using namespace std;

int num_tests;
int n;
int numbers[N];

// First index, Last index, Turn (0: 현우, 1: 서하)
int score_cache[N][N][2];
int case_cache[N][N][2];
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
    int temp_case = 0;
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
        first_case_score = numbers[first_index] + calculate(first_index+1, last_index, 1-turn);
        second_case_score = numbers[last_index] + calculate(first_index, last_index-1, 1-turn);
        if (first_case_score > second_case_score) {
            score = first_case_score;
            temp_case = 0;
        } else {
            score = second_case_score;
            temp_case = 1;
        }
        // 2. Or just remove two consecutive numbers of any edges.
        third_case_score = calculate(first_index+2, last_index, 1-turn);
        fourth_case_score = calculate(first_index, last_index-2, 1-turn);
        if (score < third_case_score) { 
            score = third_case_score;
            temp_case = 2;
        }
        if (score < fourth_case_score) {
            score = fourth_case_score;
            temp_case = 3;
        }
    }
    case_cache[first_index][last_index][turn] = temp_case;
    return score;
}

void solution() {
    int hyunwoo_score = calculate(0, n-1, 0);
    int seoha_score;
    switch(case_cache[0][n-1][0]) {
        case 0:
            seoha_score = score_cache[1][n-1][1];
            break;
        case 1:
            seoha_score = score_cache[0][n-2][1];
            break;
        case 2:
            seoha_score = score_cache[2][n-1][1];
            break;
        case 3:
            seoha_score = score_cache[0][n-3][1];
            break;
    }
    cout << hyunwoo_score - seoha_score << endl;
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