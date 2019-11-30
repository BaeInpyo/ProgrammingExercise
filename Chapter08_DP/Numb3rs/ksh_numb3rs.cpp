#include<stdio.h>
#include<stdlib.h>
#define MAX_DAY 100
#define MAX_N 50

int N;
double ***matrix; // 100 * 50 * 50, matrix[0]= Identity matrix
double **start; // 50 * 1
double **end; // 50 * 1
int is_recorded[MAX_DAY+1];
int valid;


void multiply(double **result, double **left, double **right, 
                int row_left, int column_left, int column_right){
    for(int a=0; a<row_left; a++){
        for(int c=0; c<column_right; c++){
            double sum=0;
            for(int b=0; b<column_left; b++){
                sum += left[a][b] * right[b][c];
            }
            result[a][c]=sum;
        }
    }
}

double** getMul(int day){
    if(is_recorded[day]==valid){
        return matrix[day];
    }
    // 현재 day보다 작은 최대 2^x 값
    int curr=1;
    while((curr*2)<=day){
        curr*=2;
    }
    multiply(matrix[day],getMul(curr),getMul(day-curr),N,N,N);
    is_recorded[day]=valid;
    return matrix[day];
}

void solution(int last_day, int start_idx){
    for(int i=0; i<N; i++){
        start[i][0]=0;
    }
    start[start_idx][0]=1;
    for(int curr=2; curr<=last_day; curr*=2){
        multiply(matrix[curr], matrix[curr/2], matrix[curr/2], N, N, N);
        is_recorded[curr]=valid;
    }
    multiply(end, getMul(last_day), start, N, N, 1);
}

void makeMatrixToMarkov(){
    for(int x=0; x<N; x++){
        double sum=0;
        for(int y=0; y<N; y++){
            sum += matrix[1][y][x];
        }
        for(int y=0; y<N; y++){
            matrix[1][y][x] /= sum;
        }   
    }
}

void init(){
    matrix = (double***)malloc((MAX_DAY+1)*sizeof(double**));
    for(int d=0; d<101; d++){
        matrix[d] = (double**)malloc((MAX_N)*sizeof(double*));
        for(int y=0; y<50; y++){
            matrix[d][y] = (double*)malloc((MAX_N)*sizeof(double));
        }
    }
    // matrix[0] = Identity matrix
    for(int y=0; y<50; y++){
        matrix[0][y][y]=1;
    }
    start = (double**)malloc((MAX_N)*sizeof(double*));
    for(int y=0; y<50; y++){
        start[y] = (double*)malloc(1*sizeof(double));
    }
    end = (double**)malloc((MAX_N)*sizeof(double*));
    for(int y=0; y<50; y++){
        end[y] = (double*)malloc(1*sizeof(double));
    }
    
    
}

int main(){
    //freopen("input.txt","r",stdin);
    int testcase;
    scanf("%d", &testcase);
    init();
    for(int tc=1; tc<=testcase; tc++){
        int last_day, start_idx;
        scanf("%d %d %d", &N, &last_day, &start_idx);
        for(int y=0; y<N; y++){
            for(int x=0; x<N; x++){
                scanf("%lf", &matrix[1][y][x]);
            }
        }
        valid=tc;
        is_recorded[0]=valid;
        is_recorded[1]=valid;
        makeMatrixToMarkov();
        solution(last_day, start_idx);
        
        int n_village;
        int idx;
        scanf("%d", &n_village);
        scanf("%d", &idx);
        printf("%0.8lf", end[idx][0]);
        for(int i=1; i<n_village; i++){
            scanf("%d", &idx);
            printf(" %0.8lf", end[idx][0]);
        }
        printf("\n");
    }
    return 0;
}
