#include <iostream>
#include <iomanip>

using namespace std;

int n, d, p;
double A[50][50];
double prob[7][50][50];
double res[50][50];

int q[50];

void init_matrix() {
    for (int s = 1; s < 7; ++s) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                double sum = 0.0;
                for (int k = 0; k < n; ++k) {
                    sum += prob[s-1][i][k] * prob[s-1][k][j];
                }
                prob[s][i][j] = sum;
            } 
        }
    }
}

void move_to_res(double mat[50][50]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            res[i][j] = mat[i][j];
        }
    }
}

void multiply_to_res(double mat[50][50]) {
    double temp[50][50];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            double sum = 0.0;
            for (int k = 0; k < n; ++k) {
                sum += res[i][k] * mat[k][j];
            }
            temp[i][j] = sum;
        } 
    }
    move_to_res(temp);
}

void solution() {
    init_matrix(); 
    
    int nth = 0;
    bool is_first = true;
    while (d > 0) {
        int days_in_binary = d % 2;

        if (days_in_binary) {
            if (is_first) {
                move_to_res(prob[nth]);            
                is_first = false;
            } else {
                multiply_to_res(prob[nth]);                
            }
        }

        d /= 2;
        nth++;
    }

    return;
}

int main() {
    int num_tests;
    cin >> num_tests;
    for (int c = 0; c < num_tests; ++c) {
        cin >> n; cin >> d; cin >> p;

        for (int i = 0; i < n; ++i) {
            double sum = 0.0;
            for (int j = 0; j < n; ++j) {
                cin >> A[i][j];
                if (A[i][j]) sum += 1;
            }
            if (sum != 0) {
                for (int j = 0; j < n; ++j) {
                    A[i][j] /= sum;
                    prob[0][i][j] = A[i][j];
                }
            } else {
                for (int j = 0; j < n; ++j) {
                    prob[0][i][j] = 0.0;
                }
            }
        }

        solution();

        int t; cin >> t;
        for (int i = 0; i < t; ++i) {
            cin >> q[i];
        }
        
        for (int i = 0; i < t; ++i) {
            cout << setprecision(8) << res[p][q[i]] << endl;
        }
    }

    return 0;
}