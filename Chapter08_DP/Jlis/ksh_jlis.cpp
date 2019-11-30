/*
 * A = 1 2 3
 * B = 4 5 6
 * 이 있으면 
 * B를 A 사이사이에 다 한번씩 끼워넣어봄.
 * 그리고 LIS를 구한다.
 * LIS는 n*log(n)에 구할수 있다.
 * 즉 (n^2)*log(n)
 */

#include<stdio.h>
#define MAXN 100

int len_first, len_second;
int first[MAXN];
int second[MAXN];

int lenA,lenB,lenAB;
int *A; // 짧은애를 A에 두기 위해서
int *B;
int AB[2*MAXN];

int table[2*MAXN];

void arrAppend(int pos){
    // pos위치부터는 B를 채운다.
    int A_idx=0;
    int B_idx=0;
    int AB_idx=0;
    for(A_idx; A_idx<pos; A_idx++){
        AB[AB_idx++]=A[A_idx];
    }
    for(B_idx; B_idx<lenB; B_idx++){
        AB[AB_idx++]=B[B_idx];
    }
    for(A_idx; A_idx<lenA; A_idx++){
        AB[AB_idx++]=A[A_idx];
    }
}

int binarySearch(int start, int end, int value){
    while(start<end){
        int mid = (start+end)/2;
        if(table[mid]==value){
            start=mid;
            break;
        }
        
        if(table[mid]<value){
            start = mid+1;
        }
        else{
            end = mid-1;
        }
    }
    return start;
}

int lis(){
    
    // table에서 binary 서치하면 어떤 위치가 나오는데,
    // 그 위치에서 나랑 같으면 스킵하고
    // 내가 더 작은 값이면 값을 바꿔주고
    // 만약에 내가 더 큰값인데,
    // 다음 값이 없으면 지금 값을 table에 넣어주고
    // 그 다음 값이 나보다 더 큰값이면 그 다음 값을 내꺼로 바꿔준다.
    // 이렇게 나온 table 길이가 lis 길이이다.
    int end = 0;
    table[0] = AB[0];
    // binary search
    for(int i=1; i<lenAB; i++){

        int pos = binarySearch(0, end, AB[i]);
        if(table[pos]==AB[i]){
            continue;
        }
        else if(table[pos]<AB[i]){
            if(pos==end){
                table[++end] = AB[i];
            }
            else if(AB[i]<table[pos+1]){
                table[pos+1]=AB[i]; 
            }
        }
        else{
            table[pos]=AB[i];
        }
    }
    return end+1;
}

int solution(){
    int maxLen = 0;
    for(int pos=0; pos<=lenA; pos++){   
        arrAppend(pos);
        
        int length = lis();
        maxLen = maxLen < length ? length : maxLen;
    }
    return maxLen;
}


int main(){
    freopen("8_5_input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%d %d", &len_first, &len_second);
        if (len_first <= len_second){
            A = first;
            B = second;
            lenA = len_first;
            lenB = len_second;
        }
        else {
            A = second;
            B = first;
            lenA = len_second;
            lenB = len_first;
        }
        for(int i=0; i<len_first; i++){
            scanf("%d", &first[i]);
        }
        for(int i=0; i<len_second; i++){
            scanf("%d", &second[i]);
        }

        lenAB=lenA+lenB;
        int result = solution(); 
        printf("%d\n", result);      
    }
}
