#include <iostream>
#include <math.h>

using namespace std;

int nth;
int n, s;

int numbers[100];
int result[50];

int sum[100][100];
int square_sum[100][100];

/*
 * Calculate sum and square sum
 */
void calculate() {
    for (int i=0; i<n; i++){
        for (int j=i; j<n; j++) {
            int number = numbers[j];
            if (i == j) {
                sum[i][j] = number;
                square_sum[i][j] = number * number;
            }
            else {
                sum[i][j] = sum[i][j-1] + number;
                square_sum[i][j] = square_sum[i][j-1] + number * number;
            }
        }
    }
}

/*
 * Calculate error in a single part 
 * between start and end (start <= X <= end)
 */
int calculate_error(int start, int end) {
    double len = end - start + 1;
    return square_sum[start][end] - round(sum[start][end] * sum[start][end] / len);
}

int cache[100][11];
void init_cache() {
    for (int i=0; i<100; i++) {
        for (int j=0; j<11; j++) {
            cache[i][j] = -1;
        }
    } 
}

int quantize(int start, int parts) {
    int &res = cache[start][parts];
    if (res != -1) return res;

    if (parts == 1) {
        res = calculate_error(start, n-1);
        return res;
    }

    res = 2147483646;
    for (int end=start; end<n-parts+1; end++) {
        res = min(res, calculate_error(start,end) + quantize(end+1, parts-1));
    }
    return res;
}

void init_numbers() {
    for (int i=0; i<100; i++) {
        numbers[i] = 1001;
    }
}

void insert(int nth, int number) {
    int loc = nth;
    for (int i=0; i<nth; i++) {
        if (numbers[i] >= number) {
            loc = i;
            for (int j=nth; j>i; j--) {
                numbers[j] = numbers[j-1];
            }
            break;
        }
    }
    numbers[loc] = number;
}

int main() {
    int num_tests;
    cin >> num_tests;
    for (int i=0; i<num_tests; i++) {
        cin >> n; cin >> s;
        init_numbers();
        // 1. Get input sorted
        for (int j=0; j<n; j++) {
            int number; cin >> number;
            insert(j, number);
        }
        // 2. Calculate SUM(X) and SUM(X^2)
        calculate();
        // 3. Quantize
        init_cache();
        result[i] = quantize(0, s);
    }

    for (int i=0; i<num_tests; i++) {
        cout << result[i] << endl;
    }

    return 0;
}