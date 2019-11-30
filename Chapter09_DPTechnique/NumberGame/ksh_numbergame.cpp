#include<stdio.h>
#define NOT_VISITED 200000
#define OVER_N 200000
#define MIN -100000
#define MAX 100000
#define I 0
#define YOU 1


int take[4][2]={{1,0},{0,1},{2,0},{0,2}};

int N;
int state[2][51][51]; // 현재 state에서 turn이 할 수 있는 최대 optimal값
int num[50];

int game(int turn, int left, int right){
    if(left+right > N){
        return OVER_N;
    }
    if(state[turn][left][right] != NOT_VISITED){
        return state[turn][left][right];
    }
    if(left+right==N){
        return 0;
    }
    int optimal = 0;
    if(turn==I){
        optimal = MIN;
        for(int action=0; action<=3; action++){
            int l_get = take[action][0];
            int r_get = take[action][1];
            int curr_add=0;
            if(action<2){
                curr_add = l_get == 1 ? num[left] : num[N-1-right];
            }
            int next_optimal = game((turn+1)%2, left+l_get, right+r_get);
            if(next_optimal==OVER_N){
                continue;
            }
            int curr = curr_add + next_optimal;
            if(curr > optimal){
                optimal = curr;
            }
        }
    }
    else{
        optimal = MAX;
        for(int action=0; action<=3; action++){
            int l_get = take[action][0];
            int r_get = take[action][1];
            int curr_minus=0;
            if(action<2){
                curr_minus = l_get == 1 ? num[left] : num[N-1-right];
            }
            int next_optimal = game((turn+1)%2, left+l_get, right+r_get);
            if(next_optimal==OVER_N){
                continue;
            }
            int curr = next_optimal-curr_minus;
            if(curr < optimal){
                optimal = curr;
            }
        }
    }
    state[turn][left][right]=optimal;
    return optimal;
}

void init(){
    for(int x=0; x<2; x++){
        for(int y=0; y<=N; y++){
            for(int z=0; z<=N; z++){
                state[x][y][z]=NOT_VISITED;
            }
        }
    }
}

int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            scanf("%d", &num[i]);
        }
        init();
        printf("%d\n", game(I,0,0));
    }
}
