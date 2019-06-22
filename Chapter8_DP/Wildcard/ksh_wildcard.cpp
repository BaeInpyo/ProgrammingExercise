#include<stdio.h> 
#define MAX_W_LENGTH 1002
#define MAX_LENGTH 102
#define MAX_N 50
    // *p*?a 일때
    // ----p----ppa도 체크해야하는거잖아. 
    // ****p******?, a로 봐야할지
    // *, ?, alphabet 이렇게 세가지
    // 근데 틀렷을 경우 어떻게 돌아 갈거냐?
    // 그냥 재귀에서 뒤로 돌아가면 되네;
    // 뭐할거냐면 지금 보고있는 str_idx번째와
    // w_idx를 보고 채워나가다가 안맞으면 지우고???
    // 근데 지금 보는 *이 옛날 4번째*일수 있고 8번째 *인걸수도잇는데
    // 이게되니ㅏ?.
    /*
    그.. str idx랑 w_idx로 dp 테이블을 그리고
    
        -  h  e  l  p  \0
    -   t  f  f  f  f  f
    *   f  t  t  t  t  t
    e   f  f  t  f  f  f    
    *   f  f  t  t  t  t         
    \0              
    
    *       : 왼쪽 or 왼쪽 위 or 위 -> true
    ?       : 왼쪽 위 -> true 
    number  : 왼쪽 위, str_idx -> true
    */

char W[MAX_W_LENGTH];
int len_w;
char str[MAX_LENGTH];
int len_str;
bool cache[MAX_W_LENGTH][MAX_LENGTH];
char result[MAX_N][MAX_LENGTH];
int result_n;

int strlen(char *s){
    int len=0;
    while(s[len]){
        len++;
    }
    return len;
}
void strcpy(char *dst, char *src){
    int i=0;
    while(src[i]){
        dst[i]=src[i];
        i++;
    }
    dst[i]='\0';
}
int strcmp(char *l, char *r){
    int i=0;
    while(l[i] && r[i] && l[i]==r[i]){
        i++;
    }
    return l[i]-r[i];
}

void solution(){
    for(int idx_w=0; idx_w<len_w; idx_w++){
        for(int idx_str=0; idx_str<len_str; idx_str++){
            switch(W[idx_w]){
            case '-' :
                if(str[idx_str]=='-')
                    cache[idx_w][idx_str]=true;
                else
                    cache[idx_w][idx_str]=false;
                break;
            case '*' :
                if(cache[idx_w-1][idx_str-1] || cache[idx_w][idx_str-1] 
                                                || cache[idx_w-1][idx_str])
                    cache[idx_w][idx_str]=true;
                else
                    cache[idx_w][idx_str]=false;
                break;
            case '?' :
                if(cache[idx_w-1][idx_str-1])
                    cache[idx_w][idx_str]=true;
                else
                    cache[idx_w][idx_str]=false;
                break;
            default :
                if(cache[idx_w-1][idx_str-1] && str[idx_str]==W[idx_w])
                    cache[idx_w][idx_str]=true;
                else
                    cache[idx_w][idx_str]=false;
                break;    
            }
        }
    }
    if(cache[len_w-1][len_str-1]){
        strcpy(result[result_n++], str+1);
    }
}
void swap(char *l, char *r){
    char temp[MAX_LENGTH];
    strcpy(temp, r);
    strcpy(r, l);
    strcpy(l, temp);
}
void sort(){
    // insertion sort
    for(int pivot=1; pivot<result_n; pivot++){
        for(int i=pivot-1; i>=0; i--){
            if(strcmp(result[i], result[i+1])<=0){
                break;
            }
            swap(result[i], result[i+1]);
        }
    }
}

int main(){
    freopen("8_2_input.txt", "r",stdin);
    int T;
    int N;
    scanf("%d ", &T);
    for(int tc=1; tc<=T; tc++){
        W[0]='-';
        scanf("%s", (W+1));
        len_w = strlen(W);
        scanf("%d ", &N);
        result_n = 0;
        for(int n=1; n<=N; n++){
            str[0]='-';
            scanf("%s", (str+1));
            len_str = strlen(str);
            solution();    
        }
        sort();
        for(int i=0; i<result_n; i++){
            printf("%s\n", result[i]);
        }
    }
}
