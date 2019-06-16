#include<stdio.h>
#define BLACK '#'
#define WHITE '.'
struct Lshape{
    int dy;
    int dx;
};

Lshape Lshapes[4][3] = { {{0,0},{0,1},{1,0}},
                         {{0,0},{0,1},{1,1}},
                         {{0,0},{1,0},{1,1}},
                         {{0,0},{1,0},{1,-1}} };
char board[22][22];
int H,W;
int result;

void solution(int curr, int remain){
    if(remain==0){
        result++;
        return;
    }
    if(curr >= (W+1)*(H+1)){
        return;
    }

    int y = curr / (W+1);
    int x = curr % (W+1);
    if(board[y][x]=='#'){
        solution(curr+1, remain);
        return;
    }

    for(int shape=0; shape<4; shape++){
        bool can_insert=true;
        for (Lshape dxdy : Lshapes[shape]){
            if (board[y+dxdy.dy][x+dxdy.dx] == '#'){
                can_insert=false;
                break;
            }
        }

        if(can_insert){
            for (Lshape dxdy : Lshapes[shape]){
                board[y+dxdy.dy][x+dxdy.dx]='#';
            }
            solution(curr+1, remain-3);
            for (Lshape dxdy : Lshapes[shape]){
                board[y+dxdy.dy][x+dxdy.dx]='.';
            }
        }       
    }
}
int main(){
    freopen("6_6_gameboard_input.txt", "r", stdin);
    int T;
    char line[21];
    scanf("%d", &T);
    for(int tc=1; tc<=T; tc++){
        scanf("%d %d", &H, &W);
        result=0;
        int count=0;
        for(int x=0; x<=W+1; x++){
            board[0][x]='#';
        }
        for(int y=1; y<=H; y++){
            board[y][0]='#';
            scanf("%s", board[y]+1);
            board[y][W+1]='#';
        }
        for(int x=0; x<=W+1; x++){
            board[H+1][x]='#';
        }
        for(int y=0; y<=H+1; y++){
            for(int x=0; x<=W+1; x++){
                printf("%c", board[y][x]);
            }
            printf("\n");
        }
        for(int y=1; y<=H; y++){
            for(int x=1; x<=W; x++){
                if(board[y][x]=='.'){
                    count++;
                }
            }
        }
        solution(0,count);
        printf("%d\n", result);
    }
    return 0;
}
