#include<stdio.h>
    
char tree[1001];
char buffer[1001];

void swap(int start, int pivot, int end){
    // [int.....pivot]<->[pivot+1.......end]
    for(int i=start; i<=end; i++){
        buffer[i]=tree[i];
    }
    int fill_idx=start;
    for(int i=pivot+1; i<=end; i++){
        tree[fill_idx++]=buffer[i];
    }
    for(int i=start; i<=pivot; i++){
        tree[fill_idx++]=buffer[i];
    }
}

int upDown(int pos){
    if(tree[pos]=='w' || tree[pos]=='b'){
        return pos;
    }
    // 각각 끝나는 지점이 first, second, third, fourth
    int first = upDown(pos+1);
    int second = upDown(first+1); 
    int third = upDown(second+1);
    int fourth = upDown(third+1);
    
    swap(pos+1, second, fourth);
    return fourth;
}

int main(){
    freopen("7_2_input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++){
        scanf("%s", tree);
        upDown(0);
        printf("%s\n", tree);
    }
    
}
