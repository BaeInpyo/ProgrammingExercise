#include<stdio.h>
int n, k;
int list[1000];
int prev[1000];
int next[1000];

void del(int idx){
    next[prev[idx]]=next[idx];
    prev[next[idx]]=prev[idx];
}

void solution(){
    int current=0;
    del(current);
    for(int live=n-1; live>2; live--){
        for(int i=0; i<k; i++){
            current=next[current];
        }
        del(current);
    }
    int first = next[current]+1;
    int second = next[next[current]]+1;
    if (first > second){
        printf("%d %d\n", second, first);
        return;
    }
    printf("%d %d\n", first, second);
}
void init(){
    list[0]=0;
    prev[0]=n-1;
    next[0]=1;
    for(int i=1; i<n-1; i++){
        list[i]=i;
        prev[i]=i-1;
        next[i]=i+1;
    }
    list[n-1]=n-1;
    prev[n-1]=n-2;
    next[n-1]=0;
}
int main(){
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d", &n, &k);
        init();
        solution();

    }
}
