#include<stdio.h>
#define INF 987654321
#define SAME 1
#define MONO 2
#define REPEAT 4
#define LINEAR 5
#define RANDOM 10

int N;
char input[10001];
int pi[10000];
int memo[10000];
int repeat_num[2];
int abs(int num){
    if (num < 0) {
        num *= -1;
    }
    return num;
}
int difficulty(int start, int end){
    
    bool all_same = true;  
    for(int idx=start+1; idx<=end; idx++)
        if(pi[start] != pi[idx])
            all_same=false;
    if(all_same)
        return SAME;

    bool all_same_gap = true;
    int gap = pi[start+1]-pi[start];
    for(int idx=start+1; idx<end; idx++)
        if(pi[idx+1]-pi[idx] != gap)
            all_same_gap=false;
    if(all_same_gap)
        return ( abs(gap) == 1 ? MONO : LINEAR );

    bool all_repeat = true;
    repeat_num[0]=pi[start];
    repeat_num[1]=pi[start+1];
    int count=0;
    for(int idx=start+2; idx<=end; idx++){
        if(pi[idx]!=repeat_num[count%2]){
            all_repeat=false;    
        }
        count++;
    }
    if(all_repeat)
        return REPEAT;
    
    return RANDOM;
} 

int min(int a, int b, int c){
    int result = a < b ? a : b;
    result = result < c ? result : c;
    return result; 
} 

int solution(){
    // memo[2],[3],[4],[5],[6] 까지는 직접 채울까?
    memo[2]=difficulty(0,2);
    memo[3]=difficulty(0,3);
    memo[4]=difficulty(0,4);
    memo[5]=difficulty(0,2)+difficulty(3,5);
    int case1 = difficulty(0,3)+difficulty(4,6);
    int case2 = difficulty(0,2)+difficulty(3,6);
    int case3 = INF;
    memo[6] = min(case1,case2,case3);
    for(int idx=7; idx<N; idx++){
        case1 = memo[idx-3]+difficulty(idx-2, idx);
        case2 = memo[idx-4]+difficulty(idx-3, idx);
        case3 = memo[idx-5]+difficulty(idx-4, idx);
        memo[idx]=min(case1,case2,case3);
    }
    
    return memo[N-1];
}

int main(){
    //freopen("8_7_input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%s", input);
        N=0;
        while(input[N]){
            pi[N]=input[N]-'0';
            N++;
        }
        printf("%d\n", solution());
    }
}
