#include<stdio.h>
#define MAXN 20000
#define MIN 0
int N;
int height[MAXN];
    // 나는 말이야 뭘 할거냐면...
    // middle을 무조건 포함하는 애 중에서 제일 넓은애를 고를거야
    // 그 방법으로는
    // 왼쪽 오른쪽 비교해서 제일 높이가 높은 애를 먼저 픽하는 방법으로 차근차근
    // 그렇게 src부터 dst 까지 다 보고나면
    // 최대값이 나올거고 그 값하고
    // 깊이 하나 더 들어간거하고 비교
    // 얘가 왜 N log N 이냐! 
    // 그건 말이지~
int solution(int left, int right){
    if (left>=right){
        return height[left];
    }
    
    int middle = (left+right)/2;

    int local_l = middle;
    int local_r = middle;
    int result = height[middle];
    int min_height = height[middle]; 
    while(true){
        // 이번 스텝을 어디로 확장할지 정한다.
        if (local_l==left && local_r==right){
            break;
        }
        else if (local_l == left){
            local_r++;
            min_height = min_height < height[local_r] ? min_height : height[local_r];
        }
        else if (local_r == right){
            local_l--;
            min_height = min_height < height[local_l] ? min_height : height[local_l];
        }
        else {
            if (height[local_l-1] < height[local_r+1]){
                local_r++;
                min_height = min_height < height[local_r] ? min_height : height[local_r];
            }
            else {
                local_l--;
                min_height = min_height < height[local_l] ? min_height : height[local_l];
            }
        }
        int local_square = min_height * (local_r - local_l + 1);
        result = result < local_square ? local_square : result;
    }

    int left_max = solution(left, middle-1);
    int right_max = solution(middle+1, right);
    result = result < left_max ? left_max : result;
    result = result < right_max ? right_max : result;
    return result;
}


int main(){
    freopen("7_4_input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            scanf("%d", &height[i]);
        }
        int result = solution(0, N-1);
        printf("%d\n", result);
    }

}
