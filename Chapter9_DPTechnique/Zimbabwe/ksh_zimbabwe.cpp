#include<stdio.h>
#define MOD 1000000007
#define MAX_EGG_LEN 15

int memo_count[1<<15][20][2];
char memo_valid[1<<15][20][2];
char valid;

int E[MAX_EGG_LEN];
int num[MAX_EGG_LEN];
int E_len;
int M;

// taken을 이용해 만든 애가 remain일 때,
// 이 상태에서 만들어 낼 수 있는 모든 M의 배수 개수
int solution(int taken, int remain, int less, int to_pos){
    if(to_pos==E_len){
        if(remain==0 && less==1){
            return 1;
        }
        return 0;
    }
    
    if(memo_valid[taken][remain][less]==valid){
        return memo_count[taken][remain][less];
    }
    
    int result=0;
    int prev_num=-1;
    for(int next_idx=0; next_idx<E_len; next_idx++){
        // to_pos에 넣을 next_idx는 아직 taken되지 않은 idx여야함
        if( ((1<<next_idx) & taken) != 0 ){
            continue;
        }
        // 아... idx는 다르지만 같은 값을 여러번 넣어서 중복연산해구나...
        // sorting되어있는 num[]에서 바로 전에 뽑은애가 현재이면 넘어감.
        if(prev_num == num[next_idx]){
            continue;
        }
        // 여태 넣은게 less가 아닌데, 넣으려는게 원래 to_pos에 있던것 보다 크다?
        if( (less==0) && (num[next_idx] > E[to_pos]) ){
            continue;
        }
        prev_num = num[next_idx];
        int next_taken = taken + (1<<next_idx);
        int next_remain = (remain *10 + num[next_idx]) % M;
        int next_less=0;
        if ( (less==1) || num[next_idx] < E[to_pos]){
            next_less=1;
        }       
        result += solution(next_taken,next_remain,next_less,to_pos+1);
        result %= MOD;
    }
    memo_valid[taken][remain][less]=valid;
    memo_count[taken][remain][less]=result;
    return result;
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf(" %d ", &testcase);
    valid=0;
    for(int tc=1; tc<=testcase; tc++){
        valid++;
        char input[MAX_EGG_LEN+1];
        E_len=0;
        scanf("%s", input);
        scanf(" %d ", &M);
        for(int i=0; input[i]; i++){
            E[i]=input[i]-'0';
            num[i] = E[i];
            E_len++;
        }
        for(int pivot=1; pivot<E_len; pivot++){
            for(int i=pivot; i>0; i--){
                if(num[i] >= num[i-1]){
                    break;
                }
                int temp = num[i-1];
                num[i-1]=num[i];
                num[i]=temp;
            }
        }
        
        int result = solution(0,0,0,0);         
        printf("%d\n", result);
    }
    
}
