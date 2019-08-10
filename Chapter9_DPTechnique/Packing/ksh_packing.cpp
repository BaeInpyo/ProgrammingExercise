#include<stdio.h>
#define MAX_N 100
#define MAX_V 1000
#define MAX_LENGTH 20
int N;
int V_limit;
struct Stuff{
    char name[MAX_LENGTH+1];
    int volume;
    int want;
};
Stuff stuff[MAX_N];
int dp[MAX_N][MAX_V+1];
int dp_valid[MAX_N][MAX_V+1];
int valid;
int dp_prev[MAX_N][MAX_V+1];

int packing(int s_idx, int v_lim){ // idx 순서대로, sidx를 무조건 포함해서 vlim까지 가방을 쌓을때의 최대 want
    if (s_idx< 0 || v_lim < 0)
        return 0;
    
    if (dp_valid[s_idx][v_lim]==valid)
        return dp[s_idx][v_lim];
    
    int max_want = 0;
    int max_idx = -1;
    int v_remain = v_lim - stuff[s_idx].volume;

    if(v_remain<0){
        dp[s_idx][v_lim]=0;
        dp_valid[s_idx][v_lim]=valid;
        dp_prev[s_idx][v_lim]=-1;
        return 0;
    }

    for(int prev_idx=0; prev_idx<s_idx; prev_idx++){
        int curr = packing(prev_idx, v_remain);
        if (max_want < curr){
            max_want = curr;
            max_idx = prev_idx * (V_limit+1) + v_remain;
        }
    } 
    dp[s_idx][v_lim]= stuff[s_idx].want + max_want;
    dp_valid[s_idx][v_lim]=valid;
    dp_prev[s_idx][v_lim]=max_idx;
    return dp[s_idx][v_lim];
}
void solution(){
    for(int stuff_idx=0; stuff_idx<N; stuff_idx++){
        for(int v=0; v <= V_limit; v++){
            packing(stuff_idx, v); 
        }
    }
    int max_want=-1;
    int max_idx=-1;
    for( int stuff_idx=0; stuff_idx<N; stuff_idx++){
        int curr = packing(stuff_idx, V_limit);
        if(max_want < curr){
            max_want = curr;
            max_idx=stuff_idx*(V_limit+1)+V_limit;
        }
    }
    int count=0;
    int start= max_idx;
    while(start!=-1){
        int s_idx = start / (V_limit+1);
        int v_lim = start % (V_limit+1);
        start = dp_prev[s_idx][v_lim];
        count++;
    }
    printf("%d %d\n", max_want, count);
    start= max_idx;
    while(start!=-1){
        int s_idx = start / (V_limit+1);
        int v_lim = start % (V_limit+1);
        start = dp_prev[s_idx][v_lim];
        printf("%s\n", stuff[s_idx].name );
    }
    
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        valid=tc;
        scanf(" %d %d ", &N, &V_limit);
        for(int i=0; i<N; i++){
            scanf(" %s %d %d ", stuff[i].name, &stuff[i].volume, &stuff[i].want);
        }

        solution();
        
    }
}
