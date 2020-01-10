#include<stdio.h>
#define MAX_HI 10000000

int N;
int lo;
int hi;

int board[MAX_HI+1];
int count[MAX_HI+1];
//  에라토스테네스?의 체 응용하면 될듯?

void preprocess(){
    for(int i=1; i<=MAX_HI; i++){
        board[i]=i;
        count[i]=1; 
    }

    
    for(int divisor=1; divisor<=MAX_HI; divisor++){
        // 소수가 아니면 지나가게 된다.
        if (board[divisor] == 1) {
            continue;
        }
        // divisor로 나누어지는 애들은 i칸씩 점프하는 애들
        for(int idx=divisor; idx<=MAX_HI; idx+=divisor){
            // 나누어질때까지 나눈다.
            int square=0;
            for(;; square++){
                if(board[idx]%divisor!=0){
                    break;
                }
                board[idx] /= divisor;
            }
            // 즉, 소인수분해에서의 divisor^x의 x값은 square이다.
            // 약수개수이니까 square+1 곱해주면 된다.
            count[idx] *= (square+1);
        }
    }
}
int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    preprocess();
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d %d", &N, &lo, &hi);
        int result=0;
        for(int idx=lo; idx<=hi; idx++){
            if(count[idx]==N){
                result++;
            }
        }
        printf("%d\n", result);
    }
}
