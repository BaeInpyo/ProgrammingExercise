#include<stdio.h>
#define ALL1 ((1<<24)-1)
#define NOT_VISIT 0
#define P0 0
#define P1 1
#define P2 2
#define P3 3

int moveCount[1<<24]; // 총 12개의 4bit 순서 : 11,10,......,1,0  
int queue[(1<<24) + 10000];
int front;
int rear;

void qPush(int state) {
	rear++;
	queue[rear] = state;
}
int qPop() {
	int result = queue[front];
	front++;
	return result;
}

bool qIsEmpty(){
	if (rear < front) {
		return true;
	}
	return false;
}

int where(int state, int disc){
    return (state >> (disc*2)) & 3;
}
int move(int state, int disc, int pole){
    // 먼저 disc 위치 부분을 00으로 만들어야함.
    int initialize = ALL1 - (3<<(disc*2));
    state &= initialize;
    // pole << disc*2 더해주면 됨
    state |= (pole<<(disc*2));
    return state;
}

int N;
int abs(int num){
    if (num < 0){
        num*=-1;
    }
    return num;
}
int sign(int x){
    return x >= 0 ? 1 : -1;
}
// 옮길 때 그냥 옮기는게 아니잖아.. 옮길수 있어야 옮기는데
// stack으로 현재 누구눅 올려져있는지를 기억해야하나?
// 그냥 처음에 한번 계산해 두며 되는구나.. 그걸 어레이로 기억하면 되고...

int solution(int initState){
    int lastState = (1<<(N*2)) -1;
    moveCount[initState]=1;
    moveCount[lastState]=-1;
    qPush(initState);
    qPush(lastState);
    
    while(!qIsEmpty()){
        int currState = qPop();
        int top[4]= {100,100,100,100}; // 각 pole에서 제일 위에있는 원판, 100 means empty
        for(int disc=N-1; disc>=0; disc--){ // 아 이거 거꾸로 돌면 if를 안걸어도 되는구나..
            top[where(currState, disc)] = disc;
        }
        // px번 기둥에 있는 애를 py번 기둥으로 옮긴다.. (가능한 경우에)
        for(int px=P0; px<=P3; px++){
            // pole이 비어있으면 skip
            if(top[px]==100){
                continue;
            }
            for(int py=P0; py<=P3; py++){
                // py의 top이 더 큰 경우에만 가면 됨
                if(top[py]>top[px]){
                    int nextState = move(currState, top[px], py);
                    // 아직 방문 하지 않은 경우
                    if(moveCount[nextState]==NOT_VISIT){
                        int count = moveCount[currState];
                        moveCount[nextState]=count+count/abs(count);
                        qPush(nextState);
                    }
                    // 가운데에서 만난 경우(부호가 반대인경우)
                    else if(sign(moveCount[nextState]) != sign(moveCount[currState])){
                        return abs(moveCount[nextState]) + abs(moveCount[currState])-1;
                    }

                }
            }

        }
    }
    return -1;
}

void initialize(){
    int end = 1<<(N*2);
    for (int i=0; i<end; i++){
        moveCount[i]=NOT_VISIT;
    }
    front = 0;
    rear =-1;
}
int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d", &N);
        initialize();
        int initState=0;
        for(int pidx=0; pidx<4; pidx++){
            int pn;
            scanf("%d", &pn);
            for (int i=0; i<pn; i++){
                int disc;
                scanf("%d", &disc);
                disc-=1;
                initState = move(initState, disc, pidx);
            }
        }

        printf("%d\n", solution(initState));
        // test for move, where
        // for(int disc=0; disc<N; disc++){
        //     printf("disc=%d, pole=%d\n", disc, where(initState, disc));
        // }
        // printf("\n");
    }

}
