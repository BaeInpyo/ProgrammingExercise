#include<stdio.h>
#define MAX 200000

/*
111000 <- fan
1100   <- idol

idol이 쉬프트 되면서 악수하거나 포옹하거나.

이때 idol을 reverse하고

111000
0011   *
-------------------
000000
 000000
  111000
   111000
-------------------
   abc              <- a는 (fan0, idol0).......(fan3, idol3)
                    <- b는 (fan1, idol0).......(fan4, iodl3)
                    <- c는 (fan2, idol0).......(fan5, idol3)

즉 두 숫자 곱해서
곱한 결과 어레이에서
[ Nidol-1 : Nfan-1 ] 에서 보면 된다.
*/



char str_idol[MAX+1];
char str_fan[MAX+1];
int Nidol, Nfan;
int idol[MAX];
int fan[MAX];
int C[2*MAX];
int buf[2*MAX];

int temp[MAX];
void reverse(int *arr){
    int end = Nidol-1;
    for(int i=0; i<=end; i++){
        temp[i]=arr[i];
    }
    for(int i=0; i<=end; i++){
        arr[end-i] = temp[i];
    }
}

void multiply(int sf, int ef, int si, int ei){
    for(int idxF=sf; idxF<=ef; idxF++){
        for(int idxI=si; idxI<=ei; idxI++){
            C[idxF+idxI]== fan[idxF]*idol[idxI];
        }
    }
}

void karatsuba(int sf, int ef, int si, int ei){ 
    // start_fan, end_fan, start_idol, end_idol
    if(sf==ef || si==ei){
        multiply(sf,ef,si,ei);
        return;
    }

    int mf = (sf+ef)/2;
    int mi = (si+ei)/2;
    karatsuba(sf, mf, si, mi);
    karatsuba(mf+1,ef, mi+1, ei);
    // [sf+si : mf+mi] [mf+mi+2 : ef+ei]
    for(int i=)
    karatsuba()


}

int solution(){
    reverse(idol);
    int lenC=Nidol+Nfan;
    /*for(int i=0; i<lenC; i++){
        C[i]=0;
    }*/
    karatsuba(0, Nfan-1, 0, Nidol-1);
}



int str2int(char *str, int *arr){
    int len=0;
    while(str[len]){
        arr[len] = str[len]=='F' ? 0 : 1;
        len++;
    }
    return len;
}

int main(){
    freopen("input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    for(int testcase=1; testcase<=T; testcase++){
        scanf("%s", str_idol);
        scanf("%s", str_fan);
        Nidol = str2int(str_idol, idol);
        Nfan = str2int(str_fan, fan);
        
        int result = solution();
        printf("%d\n", result);
    }
}
