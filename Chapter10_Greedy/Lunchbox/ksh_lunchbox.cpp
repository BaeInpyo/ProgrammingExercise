#include<stdio.h>
#include<stdlib.h>

#define MAX_N 10000

int N;
int micro[MAX_N];
int eat[MAX_N];
int order[MAX_N];

int compare(const void *a, const void *b){
    return (eat[*(int*)b]-eat[*(int*)a]); // 내림차순
    // (eat[*(int*)a]-eat[*(int*)b]) 요렇게하면 오름차순.
}

int solution(){
    // 그냥 먹는데 오래 걸리는 애들부터 데우면 될듯
    // quick sort (내림차순)
    qsort(order, N, sizeof(int), compare);
    int max_time=0;
    int curr_time=0;
    for(int i=0; i<N; i++){
        int curr = order[i];
        curr_time += micro[curr];
        int end_eat_time = curr_time + eat[curr];
        if(max_time < end_eat_time){
            max_time = end_eat_time;
        }
    }
    return max_time;
}



int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            scanf("%d", &micro[i]);
        }
        for(int i=0; i<N; i++){
            scanf("%d", &eat[i]);
        }
        for(int i=0; i<N; i++){
            order[i]=i;
        }
        printf("%d\n",solution());
    }
}
