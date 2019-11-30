#include <iostream>
using namespace std;

#define MAX_GENERATION_MEMO 23
// 1,000,000 (1백만)= 1MB
 
string memo[MAX_GENERATION_MEMO+1];
long long int L[51];

void solution(int generation, long long int start, long long int length){
    if(length==0){
        return;
    }
    if(start+length >= L[generation]){
        length = L[generation]-start;
    }
    if(generation <= MAX_GENERATION_MEMO){
        cout << memo[generation].substr(start, length);
        return;
    }
    
    long long int middle = L[generation]/2;
    if (start < middle){
        solution(generation-1, start, length);
    }

    if (start+length > middle){
        cout << "+";
        long long int used = middle-start+1;
        long long int remain_length = length - used;
        long long int p_middle = L[generation-1]/2;
        if(remain_length <= p_middle){ // middle보다 작을 때
            solution(generation-1, 0, remain_length);
        }
        else{
            solution(generation-1, 0, p_middle);
            cout << "-";
            used = p_middle + 1; 
            remain_length = remain_length - used;
            solution(generation-1, p_middle+1, remain_length);
        }
        
    }
}


// [0, 23] 세대는 메모해두자.
void init(){
    int curr = 0;
    int curr_len = 2;
    memo[curr] = "FX";
    curr = 1;
    curr_len = 2 * curr_len + 1;
    memo[curr] = "FX+YF";

    while(curr<=MAX_GENERATION_MEMO){
        curr++;
        memo[curr]=memo[curr-1];
        memo[curr].append("+");
        memo[curr].append(memo[curr-1].substr(0,curr_len/2));
        memo[curr].append("-");
        memo[curr].append(memo[curr-1].substr(curr_len/2+1,curr_len));
        curr_len=2*curr_len+1;
    }
    
    L[0]=2;
    curr=1;
    while(curr<=50){
        L[curr]=2*L[curr-1]+1;
        curr++;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    init();
    int testcase;
    cin >> testcase;
    for(int tc=1; tc<=testcase; tc++){
        long long int generation, start, length;
        cin >> generation;
        cin >> start;
        cin >> length;
        start= start-1;
        solution(generation, start, length);
        cout << endl;
    }

    
}
