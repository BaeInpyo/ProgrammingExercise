#include <vector>
#include <stdio.h>

using namespace std;

static const int MAX = 100000;
static const int MOD = 20091101;
static const int UNINITIALIZED = -1;
static int N, K;
static int D[MAX];
static int maxOrdersCache[MAX];
static int pSum[MAX];

void init() {
    for (int i=0; i<MAX; i++) {
        D[i] = 0;
        pSum[i] = 0;
        maxOrdersCache[i] = UNINITIALIZED;
    }
}

void getInput() {
    scanf("%d %d ", &N, &K);
    for (int i=0; i<N; i++) scanf("%d ", &D[i]);
}


/****** Q1 ******/

int getCombinations() {
    vector< vector<int> > modPsumSet;
    {
        int sum = 0;   
        for (int i=0; i<K; i++) {
            modPsumSet.push_back(vector<int>());
        }
        
        for (int i=0; i<N; i++) {
            sum += D[i];
            sum %= K;
            modPsumSet.at(sum).push_back(i);
        }
    }
    long long ret = 0;
    for (int i=0; i<K; i++) {
        const vector<int>& modPsum = modPsumSet.at(i);
        long long size = modPsum.size();
        ret += (size * (size - 1) / 2);
        ret += (i == 0 ? size : 0);
    }
    return ret % MOD;
}


/****** Q2 ******/

void calculatePsum() {
    for (int i=0; i<N; i++) {
        pSum[i] = D[i] + (i > 0 ? pSum[i-1] : 0);
    }
    return;
}

int getMaxOrders(int n) {
    if (n == 0) {
        return (D[0] % K == 0 ? 1 : 0);
    }
    if (maxOrdersCache[n] != UNINITIALIZED) {
        return maxOrdersCache[n];
    }
    
    int ret = 0;
    /* case a : order nth box (ret) */
    for (int i=n; i>=0; i--) {
        if ((pSum[n] - (i == 0 ? 0 : pSum[i-1])) % K == 0) {
            ret = 1 + getMaxOrders(i-1);
            break;
        }
    }
    /* case b : do not order nth box (getMaxOrders(n-1)) */
    ret = max(ret, getMaxOrders(n-1));
    maxOrdersCache[n] = ret;
    
    return ret;
}

void playGame() {
    init();
    getInput();
    // Q1
    int combi = getCombinations();
    // Q2
    calculatePsum();
    int orders = getMaxOrders(N-1);
    printf("%d %d\n", combi, orders);
}

int main() {
    int C;
    scanf("%d ", &C);
    for (int i=0; i<C; i++) {
        playGame();
    }
    return 0;
}
