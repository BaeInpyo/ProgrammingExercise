#include<stdio.h>
#define MOD 2
int N; 
int K; // after K-m 30-s
int M;

int length[50];
int likes[10];
double T[50][50];
double memo[2][50][4]; // time, music, length
// like부터 찾아가는데, 쭉쭉가서 0번일 확률 전체 다 더해주면 되는데,
// 메모해야할 것 : 0번째에서 내 위치로 올 확률
// 공간이 부족하네.. 이터레이티브로 쭉 값을 그냥 오면서 계산하는...
// 음.. 전에 현재, 1분, 2분 3분 4분 이렇게만 기억하는 슬라이딩 윈도우?

void solution(){
    for(int music=0; music<N; music++){
        for(int l=1; l<=4; l++){
            memo[0][music][l]=0;
        }
        
    }
    memo[0][0][length[0]]=1;

    for(int time=1; time<=K; time++){
        // 그 전에 녀석들중에서 쭉 올수 잇는 애는 쭉 오고,
        // 새로 노래가 시작되어야 한다면 그 전에 놈들에서 뛰어오고,
        int curr_time = time % MOD;
        int prev_time = (time-1)%MOD;
        for(int music=0; music<N; music++){
            int music_length =length[music];
            for(int l=1; l<music_length; l++){
                // 새로 시간이 남았었으면 된다.
                memo[curr_time][music][l] = memo[prev_time][music][l+1];    
            }
            // 노래가 바뀌어서 와야한다.
            double sum=0;
            for(int prev_music=0; prev_music<N; prev_music++){
                sum += T[prev_music][music] * memo[prev_time][prev_music][1];
            }
            memo[curr_time][music][music_length]=sum;
        }
    }
}

int main(){
    freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d %d", &N, &K, &M);
        for(int i=0; i<N; i++){
            scanf("%d", &length[i]);
        }

        for(int x=0; x<N; x++){
            for(int y=0; y<N; y++){
                scanf("%lf", &T[x][y]);
            }
        }
        for(int i=0; i<M; i++){
            scanf("%d", &likes[i]);
        }

        solution();
        
        int like = likes[0];
        double sum =0;
        for(int l=1; l<=length[like]; l++){
            sum += memo[K%MOD][like][l];
        }
        printf("%0.8lf", sum);
        for(int i=1; i<M; i++){
            like = likes[i];
            sum =0;
            for(int l=1; l<=length[like]; l++){
                sum += memo[K%MOD][like][l];
            }
            printf(" %0.8lf", sum);
        }
        printf("\n");
    }
}
