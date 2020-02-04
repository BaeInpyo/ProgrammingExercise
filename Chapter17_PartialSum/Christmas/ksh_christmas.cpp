#include<stdio.h>
#define NOT_EXIST -1

int n,k;
int r[100001];
int r_prev[100001];
int num[1000001];
int until[1000001];
int prev[100001];
int memo[100001]; // 1~i아이템까지에서 최대구간 개수

int getAnswer1(){
    long long int result =0;
    for(int i=0; i<k; i++){
        long long int a = r[i];
        long long int temp = (a*(a-1))/2;
        result = (result+temp)%20091101;
    }
    return (int)result;
}

int getAnswer2(){ // (현재 item idx, 최근에 고른 item)에서의 
    memo[0]=0;
    for(int i=1; i<=n; i++){
        int pick=0;
        int skip=0;
        // 나를 안골랏을때의 최대값
        skip = memo[i-1];
        // 나를 골랐을때의 최대값
        if(prev[i]!=NOT_EXIST){
            pick = 1+memo[prev[i]];
        }
        memo[i]=pick > skip ? pick : skip;
    }
    return memo[n];
}
void init(){
    for(int i=0; i<k; i++)
        r[i]=0;
    r[0]++;
    r_prev[0]=0;
    until[0]=0;
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d", &n, &k);
        init();
        for(int i=1; i<=n; i++){
            scanf("%d", &num[i]);
            until[i] = (until[i-1]+num[i])%k;
            prev[i]=NOT_EXIST;
            if(r[until[i]]){ // 0이 아니면 이미 누군가가 들어왔던 적이 있는 것
                prev[i] = r_prev[until[i]]; // 가장 최근에 들어왔던 인덱스
            }
            r[until[i]]++;
            r_prev[until[i]]=i; // 가장 최근에 들어왔던 인덱스 업데이트
        }
        int answer1 = getAnswer1();
        int answer2 = getAnswer2();
        printf("%d %d\n", answer1, answer2);
    }
}


/*
int n,k;
int r[100000];  //얘는 그냥 나머지 나오는 애들 다 저장 
                // 그리고 2개씩 조합 개수를 구한다.
                // 0은 처음부터 자기까지 다하는 경우도 포함되므로 r[0]=1부터 시작
int near[100000];   // 스스로 0으로 나눠지는애 만나도 0으로 초기화, 이미 있던 애 만나도 초기화 시작할때 0 넣고 시작
                    // 여기서 초기화란 현재의 카운터를 1로 올려준다는 것(만난다는 것도 현재의 카운터와 만나는 것) 초기화할때마다 0 넣고 시작

void solution(){
    int mod = 0;
    int answer2=1; // 그.. 1로시작해야 0하고 구분이 됨 나중에 정답낼때는 1뺀다.
    for(int i=0; i<n; i++){
        int box;
        scanf("%d", &box);
        mod = (mod+box)%k;
        r[mod]++;
        // for answer2
        if(box%k==0){
            answer2++;
            near[0]=answer2;
        }
        else if(near[mod]==answer2){
            answer2++;
            near[0]=answer2;
        }
        else{
            near[mod]=answer2;
        }
    }
    long long int answer1 =0;
    for(int i=0; i<k; i++){
        long long int temp = (r[i]*(r[i]-1))/2;
        answer1 = (answer1+temp)%20091101;
    }

    printf("%d %d\n", (int)answer1, answer2-1);
}

void init(){
    for(int i=0; i<k; i++){
        r[i]=0; 
        near[i]=0;      
    }
    r[0]++;
    near[0]++;
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d", &n, &k);
        init();
        solution();
    }
}
*/
