#include <iostream>

#define M 500
#define Q 20
#define N 100

using namespace std;

int num_words;
int num_str;
string words[M];

double probs_of_first_appear[M];
double probs_of_next_appear[M][M];
double probs_of_decoding[M][M]; 

int num_words_in_str;
string test_str[N];
int str_idx[N];

double prob_cache[N][M];
int path_cache[N][M];
void init_cache() {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            prob_cache[i][j] = -1;
            path_cache[i][j] = -1;
        }
    }
}
/*
 * ocr(n, i) = max_{0<=j<m}(T[j][i] * M[words(n)][i] * ocr(n-1, j))
 *   0 <= n < N
 *   0 <= i < M
 */
double ocr(int n, int i) {
    double &res_prob = prob_cache[n][i];
    int &res_path = path_cache[n][i];
    if (n == 0) {
        res_prob = probs_of_first_appear[i] * probs_of_decoding[str_idx[n]][i];
        return res_prob;
    }

    if (res_prob != -1) return res_prob;

    for (int j = 0; j < num_words; ++j) {
        double temp_prob = probs_of_next_appear[j][i] * probs_of_decoding[str_idx[n]][i] * ocr(n-1, j);
        if (res_prob < temp_prob) {
            res_prob = temp_prob;
            res_path = j;
        }
    }
    return res_prob;
}

void print_answer(int path) {
    string result = words[path];

    for (int i = num_words_in_str-1; i > 0; ++i) {
        path = path_cache[i][path];
        result = path + " " + result;
    }

    cout << result << endl;

    return;
}

void solution() {
    double res_prob = -1;
    int res_path;
    init_cache();
    for (int i = 0; i < num_words; ++i) {
        double temp_prob = ocr(num_words_in_str-1, i);
        if (res_prob < temp_prob) {
            res_prob = temp_prob;
            res_path = i;
        }
    }

    print_answer(res_path);
}

int main () {
    cin >> num_words; cin >> num_str;

    for (int i = 0; i < num_words; ++i) {
        cin >> words[i];
    }

    for (int i = 0; i < num_words; ++i) {
        cin >> probs_of_first_appear[i];
    }

    for (int i = 0; i < num_words; ++i) {
        for (int j = 0; j < num_words; ++j) {
            cin >> probs_of_next_appear[i][j];
        }
    }

    for (int i = 0; i < num_words; ++i) {
        for (int j = 0; j < num_words; ++j) {
            cin >> probs_of_decoding[i][j];
        }
    }
    
    while(--num_str >= 0) {
        cin >> num_words_in_str;
        for (int i = 0; i < num_words_in_str; ++i) {
            cin >> test_str[i];
            for (int j = 0; j < num_words; ++j) {
                if (test_str[i].compare(words[j])) {
                    str_idx[i] = j; break;
                }
            }
        }

        solution();
    }

    return 0;
}