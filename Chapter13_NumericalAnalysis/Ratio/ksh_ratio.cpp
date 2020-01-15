#include<stdio.h>
#define MAX_VICTORY 2000000000
long int n;
long int m;
long int percent;

int search(long int lo, long int hi){
    long int mid = (lo + 1 + hi)/2;
    if ( ((m+mid)*100)/(n+mid) == percent ){
        return search(mid, hi);
    }
    else{
        if (hi-lo<=1){
            return (int) hi;
        }
        else {
            return search(lo, mid);
        }
    }
}

int main(){
    // freopen("input.txt", "r", stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%ld %ld", &n, &m);
        percent = (m*100)/n;
        if ( ((m+MAX_VICTORY)*100)/(n+MAX_VICTORY) == percent ){
            printf("%d\n", -1);
        }
        else{
            printf("%d\n", search(0, MAX_VICTORY));
        }
    }
}
