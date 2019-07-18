#include<stdio.h>

#define THRESHOLD 1000000007
#define MAX 101
    // 1을 a개 2를 b개로 더해서 n을 만드는 거와 경우의 수가 같다.
    // 음.. 그렇게 못하겠다.
    // 그냥 n일때의 모든 경우를 dp로 구하자.
    // 홀수일때는 중간에 1짜리 박고 양옆이 대칭인 경우를 제거하면 됨(왼쪽의 모든 경우)
    // 짝수일때는 모든 경우에서 반나눈경우 제거하고, 중간에 2짜리박고 왼쪽 모든 경우 제거하면됨

int dp[MAX];    
int all_case(int n){
    if(n==0)
        return 1;
    if(n==1)
        return 1;
    if (dp[n] != 0)
        return dp[n];
    
    int result =0;
    if (n%2==0) { // even number
        // half1,half1 (그냥 반 나눠서 전체 경우)
        // half2=half2 (이렇게 사이에 가로블럭 두개)
        long long int half1 = all_case(n/2);
        long long int result1 = (half1 * half1) % THRESHOLD;
        long long int half2 = all_case(n/2-1);
        long long int result2 = (half2 * half2) % THRESHOLD;
        result = (int)((result1 + result2) % THRESHOLD);
        
    }
    else { // odd
        // half1, half1+1 (그냥 반 나눈거)
        // half2=half2+1 (가로블럭 두개 끼우고 반 나눈거) 
        long long int left1 = all_case(n/2);
        long long int right1 = all_case(n/2+1);
        long long int result1 = (left1 * right1) % THRESHOLD;
        long long int left2 = all_case(n/2 -1);
        long long int right2 = all_case(n/2);
        long long int result2 = (left2 * right2) % THRESHOLD;
        result = (int)((result1+result2) % THRESHOLD);
    }
    dp[n]=result;
    return result;
}
int NIsOdd(int n){
    int result=all_case(n);
    // 얘는 대칭이려면 중간에 세로블럭 박혀있어야함
    result = (result - all_case(n/2))%THRESHOLD;
    return result;
}
int NIsEven(int n){
    // 얘는 대칭이려면 왼쪽꺼 전체경우랑
    // 중간에 가로블럭 2개 끼우고 왼쪽꺼 전체경우
    int result = all_case(n);
    result = (result - all_case(n/2)) % THRESHOLD;
    result = (result - all_case(n/2-1)) % THRESHOLD;
    return result;
}

void init(int n){
    for(int i=0; i<=n; i++){
        dp[i]=0;
    }
}
int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        int N;
        scanf("%d", &N);
        init(N);
        int result = (N%2)==0 ? NIsEven(N) : NIsOdd(N);
        if (result <0)
            result = THRESHOLD+result;
        printf("%d\n", result);
    }
}
