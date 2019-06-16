#include<stdio.h>
#define MAX 100
int button[10][5] = {{0,1,2,-1,-1},
                    {3,7,9,11,-1},
                    {4,10,14,15,-1},
                    {0,4,5,6,7},
                    {6,7,8,10,12},
                    {0,2,14,15,-1},
                    {3,14,15,-1,-1},
                    {4,5,7,14,15},
                    {1,2,3,4,5},
                    {3,4,5,9,13}};

int num_connected[10] = {3,4,4,5,5,4,3,5,5,5};
int clocks[16];
int origin_clocks[16];
int result;
int click[10];

void to4bit(int num){
    for(int i=0; i<10; i++){
        click[i]=0;
    } 
    int q=num;
    int r;
    int pos=0;
    while(q){
        r=q%4;
        q=q/4;
        click[pos++]=r;
    }
}
void solution(){
    for(int inc=0; inc<(2<<20); inc++){
        to4bit(inc);
        int count=0;
        for(int button_idx=0; button_idx <10; button_idx++){
            int click_count = click[button_idx];
            int num_connect = num_connected[button_idx];
            for(int num_idx=0; num_idx <num_connect; num_idx++){
                clocks[button[button_idx][num_idx]] 
                    = (clocks[button[button_idx][num_idx]] + click_count) % 4;
            }
            count += click_count;
        }
        int sum=0;
        for(int i=0; i<16; i++){
            sum += clocks[i];
            clocks[i] = origin_clocks[i];
        }
        if (sum==0){
            result = result < count ? result : count;
        }    

    }
    if (result==MAX){
        result = -1;
    }
}

int main(){
    freopen("6_8_input.txt","r",stdin);
    int T;
    scanf("%d", &T);
    for(int tc=1; tc<=T; tc++){
        result=MAX;
        for(int i=0; i<16; i++){
            int hour;
            scanf("%d", &hour);
            clocks[i] = (hour % 12) / 3;
            origin_clocks[i]=clocks[i];
        }
        solution();
        printf("%d\n", result);
    }
}
