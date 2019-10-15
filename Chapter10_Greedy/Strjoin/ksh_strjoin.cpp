#include<stdio.h>
#include<stdlib.h>
#define INF 87654321
#define INF_IDX 127
#define MAX_N 100
#define S_IDX 128

int N;
int indexedTree[256];
int DB[128];


void resolve(int parent){
    if(parent==0){
        return;
    }
    int l_idx =  indexedTree[2*parent];
    int r_idx = indexedTree[2*parent+1];
    indexedTree[parent]= DB[l_idx] <= DB[r_idx] ? l_idx : r_idx;
    resolve(parent/2); 
}

int solution(){
    int result=0;
    while(true){
        int first_idx = indexedTree[1];
        int first_value = DB[first_idx];
        DB[first_idx]=INF;
        resolve((S_IDX+first_idx)/2);
        int second_idx = indexedTree[1];
        int second_value = DB[second_idx];
        DB[second_idx]=INF;
        resolve((S_IDX+second_idx)/2);
        if(second_value==INF){
            break;
        }
        DB[first_idx]=first_value+second_value;
        result += DB[first_idx];
        resolve((S_IDX+first_idx)/2);
    }    
    return result;
}

void init(){
    for(int i=0; i<256; i++){
        indexedTree[i]=INF_IDX;
    }
    for(int i=0; i<128; i++){
        DB[i]=INF;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        
        init();
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            scanf("%d", &DB[i]); 
            indexedTree[S_IDX+i]=i;
            resolve((S_IDX+i) / 2);   
        }

        printf("%d\n", solution());
    }
}
