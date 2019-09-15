#include<stdio.h>
#define INF 87654321
#define MAX_N 16
#define MAX_LEN 40
// 15C0 + 15C1 +... + 15C15 = 2^15 // 1~15번까지 사용한 단어의 개수.
int N;
int memo_len[50000];
int memo_word[50000];
char memo_last41[50000][MAX_LEN+1];
int memo_added_size[50000];
char word[MAX_N][MAX_LEN+1];

int strlen(char *str){
    int len=0;
    while(str[len]){
        len++;
    }
    return len;
}
void strcpy(char *src, char *dst){
    int i=0;
    while(src[i]){
        dst[i]=src[i];
        i++;
    }
    dst[i]='\0';
}

int square(int x){
    int square_x = 1;
    for(int i=0; i<x; i++){
        square_x *= 2;
    }
    return square_x;
}
bool canOverride(char *left, char *right){
    int i=0;
    while(left[i] && right[i] && left[i]==right[i]){
        i++;
    }
    if(left[i] == '\0' || right[i] == '\0'){
        return true;
    }
    return false;
}
int append(char *left, char *right, char *res){
    int li=0;
    while(left[li]){
        if(canOverride(left+li, right)){
            break;
        }
        li++;
    }
    int llen = strlen(left);
    int rlen = strlen(right);
    int added_size = rlen - (llen-li);
    if (added_size < 0){
        added_size=0;
    }

    if(added_size ==0){
        strcpy(left,res);
    }
    else{
        if(llen+added_size<=MAX_LEN){
            int res_idx = 0;
            for(; res_idx<li; res_idx++){
                res[res_idx]=left[res_idx];
            }
            for(int ridx=0; ridx<=rlen; ridx++){
                res[res_idx++]=right[ridx];
            }
        }
        else{
            int res_idx=0;
            for(int lidx=li+rlen-40; lidx<li; lidx++){
                res[res_idx++]=left[lidx];
            }
            strcpy(right, res+res_idx);
        }
    }
    return added_size;
}

char* restore(int curr_state){
    if(memo_len[curr_state] != 0){ // 이미 기록되어있다.
        return memo_last41[curr_state];
    }

    if(curr_state==0){
        memo_len[0]=0;
        memo_word[0]=-1;
        memo_last41[0][0]='\0';
        memo_added_size[0]=0;
        return memo_last41[0];
    }

    int min_total_length = INF; // (40 보다 큰 값)
    char res[41]; // 결과 담아오기 
    for(int curr_word_idx=0; curr_word_idx<N; curr_word_idx++){
        int curr_word_pos = square(curr_word_idx);
        if((curr_word_pos & curr_state)==0){
            continue;
        }
        int last_state = curr_state - curr_word_pos;
        int curr_append_length = append(restore(last_state), word[curr_word_idx], res);
        int total_length = memo_len[last_state]+curr_append_length;
        if(total_length < min_total_length){
            min_total_length = total_length;
            strcpy(res, memo_last41[curr_state]);
            memo_len[curr_state]=total_length;
            memo_word[curr_state] = curr_word_idx;
            memo_added_size[curr_state]=curr_append_length;
        }
    }
    
    return memo_last41[curr_state];
}

void solution(){
    int last_state = square(N)-1;
    restore(last_state);
    
    int curr_state=last_state;

    int state[15];
    int order=N-1;
    while(curr_state){ // curr_state != 0
        int curr_word_idx = memo_word[curr_state];
        state[order] = curr_state;
        curr_state -= square(curr_word_idx);
        order--;
    }
    for(int i=0; i<N; i++){
        int added_size = memo_added_size[state[i]];
        char *curr_word = word[memo_word[state[i]]];
        int wlen = strlen(curr_word);
        for(int wi=wlen-added_size; wi<wlen; wi++){
            printf("%c", curr_word[wi]);
        }
    }
    printf("\n");
}


void init(){
    int square_n = square(N);
    
    for(int i=0; i<square_n; i++){
        memo_len[i] = 0;
    }
}

int main(){
    int testcase;
    scanf(" %d ", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf(" %d ", &N);
        init();
        for(int i=0; i<N; i++){
            scanf("%s", word[i]);
        }
        solution();
    }
}

// 단어 최대 15개에서 단어를 가져왔을 때 걔네로 만들수 있는 
// 최소 길이, 마지막 단어, 마지막 단어를 넣으면서 추가된 사이즈
// 예를들어서 총 단어 3개 0,1,2에서 만들 수 있는 최소는
// 1,2로 구성된 string에서 0이 뒤에 붙는 경우,
// 0,2로 구성된 string에서 1이 뒤에 붙는 경우,
// 0,1로 구성된 string에서 2이 뒤에 붙는 경우
// 이렇게 세개, 즉
// 15C15 + 14*15C14 + 13*15C13 + ..... + 2 * 15C2 + 15C1 <= 500,000 (모든 경우를 확인하는데 필요한 횟수)
// 15C15 + 15C14 + 15C13 + ..... + 15C2 + 15C1 <= 50,000 (메모해야하는 모든 경우)
// 사용한 단어에 대해는 1 아니면 0 
// 10101 (0,3,5 번째 단어 사용한 것) 이런식으로 메모하겠다.

// 위의 처럼 하면 되는데...
// 나는 중복제거를 안해서 최근의 40개를 메모해두고 그걸 보고 뒤에붙였다~.~

