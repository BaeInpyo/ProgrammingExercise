#include<stdio.h>
int n;
int k;
int seq[1000];
double r[1000];
double c[1000];
const double err = 0.0000001;

// 기준 : xc-r
// [left, right]
void quickSort(double x, int left, int right) {
      int i = left, j = right;
      int pivot_idx =(left + right) / 2;
      double pivot = x*c[seq[pivot_idx]]-r[seq[pivot_idx]];
      int temp;
      do
      {
        while (x*c[seq[i]]-r[seq[i]] > pivot)
            i++;
        while (x*c[seq[j]]-r[seq[j]] < pivot)
            j--;
        if (i<= j)
        {
            temp = seq[i];
            seq[i] = seq[j];
            seq[j] = temp;
            i++;
            j--;
        }
      } while (i<= j);

    /* recursion */
    if (left < j)
        quickSort(x, left, j);

    if (i < right)
        quickSort(x, i, right);
}

// [left, right]
// mid*c-r 값으로 소팅 (큰 순서로)
// error 범위 이내이면? 스탑.
// 양수면 오른쪽구간으로
// 음수면 왼쪽 구간으로
double solution(double left, double right){
    double mid = (left+right)/2;
    quickSort(mid, 0, n-1);    

    double sum =0;
    for(int i=0; i<k; i++){
        sum += mid * c[seq[i]];
        sum -= r[seq[i]];
    }

    if (-err< sum && sum < err){
        return mid;
    }
    else if (sum > 0){
        return solution(left, mid-err);
    }
    else {
        return solution(mid+err, right);
    }
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d", &n, &k);
        for(int i=0; i<n; i++){
            seq[i]=i;
            scanf("%lf %lf", &r[i], &c[i]);
        }        
    
        printf("%0.10lf\n", solution(0.0, 1.0));
    }
}
