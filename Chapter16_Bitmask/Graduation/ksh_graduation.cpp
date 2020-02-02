#include<stdio.h>
#define MAX_MAJOR 12
#define MAX_SEMESTER 10
#define INF 100

int majorN, mustN, semesterN, limit;
int prerequisite[MAX_MAJOR];
int semester[MAX_SEMESTER];
int memo[MAX_SEMESTER][1<<MAX_MAJOR];
int memo_valid[MAX_SEMESTER][1<<MAX_MAJOR];
int valid;

int bitCount(int x){
    if(x==0) return 0;
    return (x%2)+bitCount(x/2);
}

int solution(int seme_idx, int done, int doneN){
    // doneN이 mustN을 넘거나 같고, semester가 semesterN보다 작거나 같으면 남은 학기 0
    if ((doneN >= mustN) && (seme_idx <= semesterN)){
        return 0;
    }
    // semester가 semesterN보다 크거나 같은데, doneN이 mustN보다 작으면... 실패
    if ((doneN < mustN) && (seme_idx == semesterN)){
        return INF;
    }
    if (memo_valid[seme_idx][done]==valid){
        return memo[seme_idx][done];
    }
    // semester에 열리는 애들 중에 done은 빼고, 얘들중에서 선수과목 안들은 애들도 제외하고 비트를 구한다
    int candidate = semester[seme_idx] & (~done);
    for(int midx=0; midx<majorN; midx++){
        int position = 1<<midx;
        if (candidate & position){
            if( (done&prerequisite[midx])!=prerequisite[midx] ){
                candidate -= position;
            }
        }
    }
    // count 개수만큼 골라서 다음 스텝으로 간다.    
    int result = INF;
    // 학기마다 열리는게 다르니까.. 무조건 다 듣는게 좋은게 아니구나..
    // 어쩌면 휴학하는게 더 좋을수가 있네

    // 이거 subset 도는게 개꿀팁이네;;;
    for(int subset=candidate; subset; subset = ((subset-1) & candidate)) {
        int count = bitCount(subset);    
        if(count <= limit){
            int temp = solution(seme_idx+1, done|subset, doneN+count)+1;
            if (temp < result){
                result = temp;
            }
        }
    }
    int temp = solution(seme_idx+1, done, doneN);
    if (temp <result){
        result = temp;
    }
    memo_valid[seme_idx][done]=valid;
    memo[seme_idx][done]=result;
    return result;
}



void init(){
    for(int i=0; i<majorN; i++){
        prerequisite[i]=0;
    }
    for(int i=0; i<semesterN; i++){
        semester[i]=0;
    }
}
int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        valid = tc;
        scanf("%d %d %d %d", &majorN, &mustN, &semesterN, &limit);
        init();
        int count;
        int midx;
        for(int i=0; i<majorN; i++){
            scanf("%d", &count);
            for(int p=0; p<count; p++){
                scanf("%d", &midx);
                prerequisite[i] |= (1<<midx);
            }

        }
        for(int i=0; i<semesterN; i++){
            scanf("%d", &count);
            for(int m=0; m<count; m++){
                scanf("%d", &midx);
                semester[i] |= (1<<midx);
            }
        }
        int result = solution(0, 0, 0);
        if (result >= INF){
            printf("%s\n", "IMPOSSIBLE");
        }
        else {
            printf("%d\n", result);
        }
    }
}
