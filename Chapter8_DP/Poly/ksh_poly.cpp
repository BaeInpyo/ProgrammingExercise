#include<stdio.h>

#define MAXN 100
#define MOD 10000000

int dp[100][100];

int count(int n, int curr ){ // 전체 남은 블럭, 현재자리에 놓을 블럭
    if(n==curr){
        return 1;
    }
    if(dp[n][curr] != 0){
        return dp[n][curr];
    }
    int remain=n-curr;
    long long int result=0;
    for(int next=1; next<=remain; next++){
        result += (curr+next-1)*count(remain, next);
        result %= MOD;
    }
    dp[n][curr]=result;
    return result;
}

int solution(int N){
    int result=0;
    for(int i=1; i<=N; i++){
        result += count(N, i);
        result %= MOD;
    }
    
    return result;
}

int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        int N;
        scanf("%d", &N);
        printf("%d\n", solution(N));
    }
}

