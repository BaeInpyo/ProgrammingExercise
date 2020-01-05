#include<stdio.h>
#include<math.h>

#define MAX 87654321

int N;

struct Base{
    double x;
    double y;
};

Base base[100];

bool visit[100];
double dist[100];

void solution(int curr){
   
    visit[curr]=true;
    
    int next=curr;
    double next_dist=MAX;
    
    // 나를 제외하고 visit 안된 애들 resolve
    for(int idx=0; idx<N; idx++){
        if(visit[idx]){
            continue;
        }
        double d = sqrt( pow((base[curr].x-base[idx].x), 2) + pow((base[curr].y-base[idx].y), 2) );
        // resolve
        if(d < dist[idx]){
            dist[idx]=d;
        }
        // resolve 된 애들 중에서 최소값이 다음으로 visit할 곳
        if (dist[idx]<next_dist){
            next_dist=dist[idx];
            next=idx;
        }
    }
    if(next == curr){
        return;
    }
    solution(next);
}
void init(){
    for(int i=0; i<N; i++){
        visit[i]=false;
        dist[i]=MAX;
    }
}
int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        
        scanf("%d", &N);
        init();
        for(int i=0; i<N; i++){
            scanf("%lf %lf", &base[i].x, &base[i].y);
        }
        solution(0);
        double result=0;
        for(int i=1; i<N; i++){
            if(dist[i]>result){
                result = dist[i];
            }
        }
        printf("%.2lf\n", result);
    }
}

