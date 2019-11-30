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
int dp_want[MAX_N][MAX_V+1];
int dp_prev[MAX_N][MAX_V+1];
int dp_packed[MAX_N][MAX_V+1];

int dp_valid[MAX_N][MAX_V+1];

int valid;

int packing(int s_idx, int v_lim){
    if(s_idx < 0 || v_lim < 0){
        return 0;
    }

    if(dp_valid[s_idx][v_lim]==valid){
        return dp_want[s_idx][v_lim];
    }

    int packed = 0;
    int not_packed = 0;
    if (stuff[s_idx].volume <= v_lim){
        packed = stuff[s_idx].volume + packing(s_idx-1, v_lim-stuff[s_idx].volume);    
    }
    not_packed = packing(s_idx-1, v_lim);
    
    if(not_packed < packed){
        dp_want[s_idx][v_lim] = packed;
        dp_prev[s_idx][v_lim] = (s_idx-1)*(V_limit+1) + v_lim-stuff[s_idx].volume;
        dp_packed[s_idx][v_lim] = valid;
        dp_valid[s_idx][v_lim] = valid;
        return packed;
    }

    dp_want[s_idx][v_lim] = not_packed;
    dp_prev[s_idx][v_lim] = (s_idx-1)*(V_limit+1) + v_lim;
    dp_packed[s_idx][v_lim] = valid;
    dp_valid[s_idx][v_lim] = valid;
    return not_packed;
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        valid=tc;
        scanf(" %d %d ", &N, &V_limit);
        for(int i=0; i<N; i++){
            scanf(" %s %d %d ", stuff[i].name, &stuff[i].volume, &stuff[i].want);
        }

        packing(N-1, V_limit);
        
        int curr = (N-1)*(V_limit+1) + V_limit;
        int count=0;
        while(curr >= 0){
            int s_idx = curr / (V_limit+1);
            int v_lim = curr % (V_limit+1);
            if(dp_packed[s_idx][v_lim]==valid)
                count++;
            curr = dp_prev[s_idx][v_lim];
        }
        printf("%d %d\n", dp_want[N-1][V_limit], count);
        curr = (N-1)*(V_limit+1) + V_limit;
        while(curr >= 0){
            int s_idx = curr / (V_limit+1);
            int v_lim = curr % (V_limit+1);
            if(dp_packed[s_idx][v_lim]==valid)
                printf("%s\n", stuff[s_idx].name );
            curr = dp_prev[s_idx][v_lim];   
        }
    }
}
