/*
sorting을 해두면
N개의 arr를 S개의구간으로 나누는 문제가 된다.
지금 자리에서 몇개의 구간으로 나눴을 때의 최소값을 매번 dp로 기록해둘 수 있고,
현재idx 위치에서 부터 s개의 구간으로 나누려고 할 때의 최소 error값 = dp[idx][s]

dp[idx][s] = min( error(1개)+dp[idx+1][s-1], error(2개)+dp[idx+2][s-1], error(3개)+dp[idx+3][s-1], .... )

 */
#include<stdio.h>
#define MAX_N 100
#define INF 100000000
#define MAX_S 10
int N; // 1~100
int S; // 1~10
int arr[MAX_N+1]; // 1~1000
int sum[MAX_N+1];
int square[MAX_N+1];
int dp[MAX_N+1][MAX_S+1];
int valid_dp[MAX_N+1][MAX_S+1];
int valid;

int calcError(int start, int end){
	// start에서 end까지의 error
	// (start-m)^2 + ....... + (end-m)^2
	// (start^2 + .... + end ^2) -2*m*(start+...+end) + (end-start+1) * m^2
	int n = end-start+1;
    int block_square = square[end]-square[start-1];
	int block_sum = sum[end]-sum[start-1];
    int midium = (int)( ((double)block_sum / n)+0.5);
	int error = block_square - 2* midium * block_sum + (end-start+1)*midium*midium;
	return error;
}	

int getMinError(int idx, int s){
	// base
	if(idx > N){ // 더이상 숫자가 없는 경우
		return 0;
	}
	else if(s<=0){ // 숫자가 남았는데, 조합을 할 수 없는 경우
		return INF;
	}
	
	// 
	if(valid_dp[idx][s]==valid){
		return dp[idx][s];
	}

	int minimum=INF;
	for(int end=idx; end<=N; end++){
		int localError = calcError(idx, end) + getMinError(end+1, s-1);
		minimum = minimum < localError ? minimum : localError; 
	}
	valid_dp[idx][s]=valid;
	dp[idx][s]=minimum;
	return minimum;
}


int insertionSort(){
    int temp;
    for(int pivot=2; pivot<=N; pivot++){
        for(int i=pivot-1; i>=1; i--){
            if (arr[i] <= arr[i+1]){
                continue;
            }
            temp=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=temp;
        }
    }
}

void makeSums(){
    // 0의 자리는 0으로 초기화
	// 이렇게 하면 모든 구간에 대해서 sum[b] - sum[a-1] = sum[a:b]
    sum[0]=0;
    square[0]=0;
    for(int i=1; i<=N; i++){
        sum[i] = sum[i-1] + arr[i];
        square[i] = square[i-1] + arr[i] * arr[i];
    }
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        valid=tc;
		scanf("%d %d", &N, &S);
        arr[0]=0;
        for(int i=1; i<=N; i++){
            scanf("%d", &arr[i]);
        }
        insertionSort();
        makeSums();
        int result = getMinError(1, S);
        printf("%d\n", result);        
    }
}
