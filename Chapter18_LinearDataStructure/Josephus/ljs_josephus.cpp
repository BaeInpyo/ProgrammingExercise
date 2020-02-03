#include <iostream>

using namespace std;

static const int MAX = 1000;
static int N, K;
static bool dead[MAX];

void input() {
    cin >> N >> K;
}

void init() {
    for (int i=0; i<MAX; i++) dead[i] = false;
}

void suicide() {
    int survivors = N;
    int soldier = 0;
    int count = 0;
    while (true) {
        if (survivors <= 2) 
            break;
        if (!dead[soldier]) {
            if (count == 0) {
                dead[soldier] = true;
                survivors--;
            }
            count = (count + 1) % K;
        }
        soldier = (soldier + 1) % N;
    }
    int survivor1 = 0, survivor2 = 0;
    for (int soldier=0; soldier<N; soldier++) {
        if (!dead[soldier]) {
            if (survivor1 == 0) {
                survivor1 = soldier+1;
            } else {
                survivor2 = soldier+1;
                break;
            }
        }
    }
    cout << survivor1 << " " << survivor2 << endl;
    return;
}

void playGame() {
    input();
    init();
    suicide();
}

int main() {
    int C;
    cin >> C;
    for (int i=0; i<C; i++) {
        playGame();
    }
    return 0;
}
