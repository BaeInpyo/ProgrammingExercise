#include<stdio.h>
#define MAX_N_WORD 500
#define WORD_LENGTH 11
#define MAX_POS 100
#define MOD 10007

char words[MAX_N_WORD][WORD_LENGTH];
float p_first[MAX_N_WORD];
float p_next[MAX_N_WORD][MAX_N_WORD];
float p_recog[MAX_N_WORD][MAX_N_WORD];

float memo[MAX_POS][MAX_N_WORD];
int memo_valid[MAX_POS][MAX_N_WORD];
int prev_word[MAX_POS][MAX_N_WORD];
int valid;

int sentence[MAX_POS];
int n_word;
int length;

int result_sentence[MAX_POS];
///////////////////// hash to find word_idx //////////////////////////
int hash[MOD];
int hash_valid[MOD];

void insertHash(char *word, int pos){
    int key=0;
    for(int i=0; word[i]; i++){
        key *= 10177;
        key += word[i]*1007;
        key %= MOD;
    }

    while(hash_valid[key]!=0){
        key = (key+1)%MOD;
    }
    hash_valid[key]=1;
    hash[key]= pos;
}

int strcmp(char *s1, char *s2){
    int i=0;
    while(s1[i] && s2[i] && (s1[i]==s2[i])){
        i++;
    }
    return s1[i]-s2[i];
}
int wordToIdx(char *word){
    int key=0;
    for(int i=0; word[i]; i++){
        key *= 10177;
        key += word[i]*1007;
        key %= MOD;
    }
    int w_idx=0;
    while(hash_valid[key]!=0){
        w_idx = hash[key];
        if(strcmp(word, words[w_idx])==0){
            break;
        }
        key = (key+1)%MOD;
    }
    return w_idx;
}

float probability(int pos, int curr_idx){
    if (memo_valid[pos][curr_idx]==valid){
        return memo[pos][curr_idx];
    }

    // base
    if(pos==0){
        int recog_idx = sentence[0];
        memo[0][curr_idx] = p_recog[curr_idx][recog_idx] * p_first[curr_idx];
        prev_word[0][curr_idx] = -1;
        memo_valid[0][curr_idx]=valid;
        return memo[0][curr_idx];
    }
    int recog_idx = sentence[pos];
    if(p_recog[curr_idx][recog_idx]==0){
        memo[pos][curr_idx] = 0;
        prev_word[pos][curr_idx] = -1;
        memo_valid[pos][curr_idx]=valid;
        return 0;
    }
    // body
    float max = 0;
    int max_prev_idx = 0;
    for(int prev_idx=0; prev_idx<n_word; prev_idx++){
        if(p_next[prev_idx][curr_idx]==0){
            continue;
        }

        float p_prev = probability(pos-1, prev_idx);
        float p_curr = p_prev * p_recog[curr_idx][recog_idx] * p_next[prev_idx][curr_idx];
            
        if (p_curr > max){
            max = p_curr;
            max_prev_idx = prev_idx;
        }
    }

    memo[pos][curr_idx]= max;
    prev_word[pos][curr_idx] = max_prev_idx;
    memo_valid[pos][curr_idx] = valid;
    return max;
}
/////////////////////////   solution   //////////////////////////////
void solution(){
    float max = 0;
    int start_word_idx = 0;
    for(int w_idx=0; w_idx<n_word; w_idx++){
        float p_curr = probability(length-1, w_idx);
        if(p_curr > max){
            start_word_idx = w_idx;
            max = p_curr;
        }
    }

    int w_idx = start_word_idx;
    int pos = length-1;
    while(pos>=0){
        result_sentence[pos]=w_idx;
        w_idx = prev_word[pos][w_idx];
        pos--;
    }
}



//////////////////////////   main    ////////////////////////////////
int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf(" %d %d ", &n_word, &testcase);
    for(int i=0; i<n_word; i++){
        scanf("%s", words[i]);
        insertHash(words[i], i);
    }
    for(int i=0; i<n_word; i++){
        scanf("%f", &p_first[i]);
    }
    for(int y=0; y<n_word; y++){
        for(int x=0; x<n_word; x++){
            scanf("%f", &p_next[y][x]);
        }
    }
    for(int y=0; y<n_word; y++){
        for(int x=0; x<n_word; x++){
            scanf("%f", &p_recog[y][x]);
        }
    }
    
    for(int tc=1; tc<=testcase; tc++){
        valid = tc;
        scanf(" %d ", &length);
        char word[WORD_LENGTH];
        for(int i=0; i<length; i++){
            scanf("%s", word);
            sentence[i]=wordToIdx(word);
        }

        solution();

        printf("%s", words[result_sentence[0]]);
        for(int i=1; i<length; i++){
            printf(" %s", words[result_sentence[i]]);
        }
        printf("\n");
    }
    

    return 0;
}


