#include<stdio.h>
int friends[10][10];
int N;
int M;
int alive;
int couple[10];
int result;

void solution(int c1){
    bool complete=true;
    for(int i=0; i<N; i++){
        if(couple[i]!=alive){
            complete=false;
        }
    }
    if(complete){
        result++;
        return;
    }
    if(couple[c1]==alive){
        solution(c1+1);
        return;
    }
    for(int c2=c1+1; c2<N; c2++){
        if(friends[c1][c2]==alive && couple[c2] != alive){
            couple[c1]=alive;
            couple[c2]=alive;
            solution(c1+1);
            couple[c1]=0;
            couple[c2]=0;
        }
    }
}

int main(){
    freopen("6_3_picnic_input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for(alive=1; alive<=T; alive++){
        scanf("%d %d", &N, &M);
        int c1, c2;
        result=0;
        for(int i=0; i<M; i++){
            scanf("%d %d", &c1, &c2);
            friends[c1][c2]=alive;
            friends[c2][c1]=alive;
        }
        solution(0);
        printf("%d\n", result);
    }
    return 0;    
}
