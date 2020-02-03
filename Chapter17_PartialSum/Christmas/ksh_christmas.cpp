#include<stdio.h>

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
// 아 동적계획법이구나 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 
