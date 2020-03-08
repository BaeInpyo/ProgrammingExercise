#include<map>
#include<stdio.h>
using namespace std;

map<int, int> applyer;

bool inRange(int p, int q){
    map<int, int>::iterator it = applyer.lower_bound(p);
    if(it==applyer.end()){
        return false; // 얘가 p가 젤 큰경우
    }
    if(it->second < q){
        return false;
    }
    return true;
}

int deleteInRange(int p,int q){
    map<int, int>::iterator it = applyer.lower_bound(p);
    if(it ==applyer.begin()){
        return 0; // 지울게 없는 경우..
    }
    int count = 0;
    --it;
    while(true){
        // q값보다 더 커진 경우에 멈춰야하고,
        if(it->second > q){
            break;
        }
        // 지워야하는데 맨 처음인 경우 지우고 끝
        if(it==applyer.begin()){
            applyer.erase(it);
            count++;
            break;    
        }

        map<int, int>::iterator jt = it;
        --jt;
        applyer.erase(it);
        count++;
        it=jt;
    }
    return count;
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        int n;
        scanf("%d", &n);

        applyer.clear();
        int candidate=0;
        int sum=0;
        for(int i=0; i<n; i++){
            int p, q;
            scanf("%d %d", &p, &q);
            if (inRange(p,q)){
                continue;
            }
            // 그리고 얘가 들어오면서 지울 애를지워줘야함
            candidate -= deleteInRange(p,q);
            applyer[p]=q;
            candidate++; // 후보에 들어올 수 있으면 추가됨
            sum += candidate;
        }  
        printf("%d\n", sum);
    }
}
