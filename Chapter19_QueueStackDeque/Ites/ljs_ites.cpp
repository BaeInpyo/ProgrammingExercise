#include <iostream>
#include <queue>

using namespace std;

static int N, K;
static unsigned int genNumber;

class itesQueue {
    public:
        itesQueue() : q(*(new queue<int>())), sum(0) {}
        void push(int n) {
            q.push(n);
            sum += n;
        }
        void pop() {
            sum -= q.front();
            q.pop();
        }
        int getSum() {
            return sum;
        }
    private:
        queue<int>& q;
        int sum;
};

int generateNextInput() {
    genNumber = genNumber * 214013 + 2531011;
    return genNumber % 10000 + 1;
}        

void playGame() {
    cin >> K >> N;
    itesQueue iq;
    genNumber = 1983;
    int ret = 0, i = 0;
    i++;
    while (true) {
        if (i == N) break;
        int sum = iq.getSum();
        if (sum <= K) {
            if (sum == K) {
                ret++;
            }
            i++;
            iq.push(generateNextInput());
        } else if (iq.getSum() > K) {
            iq.pop();
        }
    }
    cout << ret << endl;
}

int main() {
    int C;
    cin >> C;
    for (int i=0; i<C; i++) {
        playGame();
    }
    return 0;
}
