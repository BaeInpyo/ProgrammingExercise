#include <iostream.h>

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
string test_str[M];

void solution() {
    
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
        }

        solution();
    }

    return 0;
}