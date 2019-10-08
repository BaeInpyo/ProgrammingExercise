#include<stdio.h>
#define BOUNDARY 10000000
#define INF 87654321
#define NOT_VISITED -1
int price[21];
int prefer[21];
int costQ[21]; // price / prefer
int costR[21]; // price % prefer
int budget; // 예산
int N;

int memo[BOUNDARY];

int compare(int a, int b){
    if(costQ[a]==costQ[b]){
        return costR[a]-costR[b];
    }
    return costQ[a]-costQ[b];
}

int findBest(int remain){
    // base_case : 남은 돈이 없으면 0
    if(remain<=0){
        return 0;
    }
    // 방문한적 있으면
    if(memo[remain] != NOT_VISITED){
        return memo[remain];
    }
    // 현재에서 다 먹어보자. 그 중 맥스값
    int curr_prefer = 0;
    for(int i=1; i<=N; i++){
        if(remain < price[i]){
            continue;
        }
        int do_eat = findBest(remain-price[i])+prefer[i];
        if (curr_prefer < do_eat){
            curr_prefer = do_eat;
        }
    }
    memo[remain]=curr_prefer;
    return curr_prefer;
}

int solution(int minimum_cost_idx){
    //400 이하가 될때까지 price[minimum_cost_idx]를 빼겠다.
    //mod를 때려서 거기서부터 더해가다가 400넘기전에 멈추는게 낫겠다..
    int count = budget / price[minimum_cost_idx];
    int remain = budget % price[minimum_cost_idx];
    while(remain<BOUNDARY){
        count--;
        remain+=price[minimum_cost_idx];  
    }
    remain-=price[minimum_cost_idx];
    count++;
    int total_prefer = prefer[minimum_cost_idx]*count;
    return findBest(remain) + total_prefer; 
}
void init(){
    for(int i=0; i<BOUNDARY; i++){
        memo[i]=NOT_VISITED;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    price[0]=20000;
    prefer[0]=1;
    costQ[0]=20000;
    costR[0]=0;
    for(int tc=1; tc<=testcase; tc++){
        init();
        scanf("%d %d", &N, &budget);
        budget /= 100;
        int minimum_cost_idx=0;
        for(int i=1; i<=N; i++){
            scanf("%d %d", &price[i], &prefer[i]);
            price[i] /= 100;
            costQ[i] = price[i]/prefer[i];
            costR[i] = price[i]%prefer[i];
            if(compare(minimum_cost_idx, i)>=0){ // i가 더 작으면
                minimum_cost_idx=i;
            }
        }
        printf("%d\n", solution(minimum_cost_idx));
    }
}
