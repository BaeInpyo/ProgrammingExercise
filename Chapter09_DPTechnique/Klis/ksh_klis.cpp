#include<stdio.h>
#define MAX_N 500

int N;
long long int k_th;
int arr[MAX_N+1];

int lis[MAX_N+1];
int nexts[MAX_N+1][MAX_N];
int n_nexts[MAX_N+1];
long long int n_total[MAX_N+1];

int result[MAX_N];
// lis[idx] -> idx위치에서부터 시작해서 최대 lis길이
// nexts[idx] - > 최대길이 lis에서 idx 다음으로 올수있는 모든애들 
// n_nexts[idx] -> 최대길이 lis에서 idx 다음으로 올수있는 모든애들 개수
// n_total[idx] -> 최대길이 lis를 트리구조로 만들었을 때 자기 subtree의 leaf 개수


int getLis(int idx){ // idx를 시작으로 제일 긴 lis
    // max_lis 구하기
    int max_lis = 0;
    for(int n_idx=idx+1; n_idx<=N; n_idx++){
        if (arr[idx] < arr[n_idx]){
            max_lis = lis[n_idx] > max_lis ? lis[n_idx] : max_lis;
        }
    }

    lis[idx]=max_lis+1;
    if(max_lis==0){
        n_total[idx]=1;
    }

    // 다음으로 올수잇는 애들 모두 연결하기
    for(int n_idx=idx+1; n_idx<=N; n_idx++){
        if((arr[idx] < arr[n_idx]) && (lis[n_idx]==max_lis)){
            nexts[idx][n_nexts[idx]]=n_idx;
            n_nexts[idx]++;
            if(n_total[n_idx]>=k_th){
                n_total[idx]=k_th;
            }
            n_total[idx] += n_total[n_idx];
        }
    }

    return lis[idx];
}
void insertionSort(int curr){
    // idx 순이 아니라 idx 안에 값에 따라 insertSort로 소팅
    for(int pivot=1; pivot<n_nexts[curr]; pivot++){
        for(int i=pivot-1; i>=0; i--){
            int next_idx = nexts[curr][i+1];
            int prev_idx = nexts[curr][i];
            if (arr[prev_idx] > arr[next_idx]){
                int temp = next_idx;
                nexts[curr][i+1] = prev_idx;
                nexts[curr][i] = temp;
            }
        }
    }
}

void solution(){
    int max=0;
    
    for(int idx=N; idx>=0; idx--){
        getLis(idx);
    }
    int curr = 0;
    int size=0;
    
    while(n_nexts[curr]){
        // 내가 갈수잇는 자식들 중에서 사전순서로 몇번째 자식으로 가야하는지
        insertionSort(curr);
        
        for(int i=0; i<n_nexts[curr]; i++){
            int next_idx = nexts[curr][i];
            if ( n_total[next_idx] >= k_th){
                curr = next_idx;
                break;
            }
            else { 
                k_th-=n_total[next_idx];
            }
        }    
        
        result[size] = arr[curr];
        size++;   
    }

    printf("%d\n", size);
    printf("%d", result[0]);
    for(int i=1; i<size; i++){
        printf(" %d", result[i]);
    }
    printf("\n");
}

void init(){
    for(int i=0; i<=N; i++){
        lis[i]=0;
    }
    for(int i=0; i<=N; i++){
        n_nexts[i]=0;
    }
    for(int i=0; i<=N; i++){
        n_total[i]=0;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %lld", &N, &k_th);
        
        init();

        arr[0]=-1;
        for(int i=1; i<=N; i++){
            scanf("%d", &arr[i]);
        }
        
        solution();        
    }
    return 0;
}

// 음... 전체 경우가 long long int마저 넘은건가?
// 그러면 k_th 가 넘는거에 대해서는 그만 구해야하나? 아예 long long int 마저도 넘어버려서 에러떴나봄
// -> 그래서 n_total이 k_th가 넘으면 그냥 k_th값을 넣어줌.
