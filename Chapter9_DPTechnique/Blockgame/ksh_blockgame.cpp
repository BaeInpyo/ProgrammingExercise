#include<stdio.h>
#define BLOCK 1
#define EMPTY 0
#define WIN 'W'
#define LOSE 'L'
int block_dy[6][2] = {{0,0},{0,1},{0,1},{1,1},{1,1},{0,1}}; //[block_direction][block_idx]
int block_dx[6][2] = {{0,1},{0,0},{1,1},{0,1},{0,-1},{1,0}};

char memo[33554432]; // 2^25 = 33554432

bool inRange(int y, int x){
    if(y < 0 || y > 4 || x < 0 || x > 4){
        return false;
    }
    return true;
}

char run(int state){ // state상태에서 내가이길수있으면 WIN 아니면 LOSE
    
    if(memo[state]!=0){
        return memo[state];
    }
    // 다음 스텝 중에 LOSE가 없으면 나는 무조건 진다.
    // 다음 스텝 중에 하나라도 LOSE이면 나는 무조건 이긴다.
    
    
    char SCORE = LOSE; // 넣을 수 있는 경우가 없으면 자동으로 LOSE
    for(int idx=0; idx<25; idx++){
        if((state >> idx)%2==BLOCK){
            continue;
        }
        int y = idx/5;
        int x = idx%5;
        // case : blcok2, block3
        for(int shape=0; shape<6; shape++){
            int next_state = state;
            bool can_insert=true;
            for(int b_idx=0; b_idx<2; b_idx++){
                int cy = y+block_dy[shape][b_idx];
                int cx = x+block_dx[shape][b_idx];
                int cidx = cy*5 + cx;
                if(inRange(cy,cx)==false || ((state >> cidx)%2)==BLOCK){
                    can_insert=false;
                    break;
                }
                next_state = next_state | (1<<cidx);
            }
            if(can_insert==false){
                continue;
            }
            next_state = next_state | (1<<idx);
            if(run(next_state)==LOSE){
                SCORE=WIN;
                break;
            }
        }
        if(SCORE==WIN){
            break;
        }
    }

    memo[state]=SCORE;
    return SCORE;
}



int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        char input[6];
        int state=0;
        for(int y=0; y<5; y++){
            scanf("%s", input);
            for(int x=0; x<5; x++){
                state=state<<1;
                state += input[x] == '#' ? 1 : 0;
            }
        }
        
        char result = run(state);
        printf("%s\n",result==WIN ? "WINNING" : "LOSING");
    }
}
