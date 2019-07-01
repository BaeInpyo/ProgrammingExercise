#include <iostream>

using namespace std;

int num_cases;
string numbers[50];

int get_difficulty(int start, int end, string number) {
    int a = number[start] - '0';
    int res = 0;

    // check first, second and fourth case
    int b = number[start+1] - '0';
    int diff = a - b;
    if (diff == 0) res = 1;                     // first
    else if (diff == 1 || diff == -1) res = 2;  // second
    else res = 4;                               // fourth
    for (int i = start+2; i < end; i++) {
        int c = number[i] - '0';
        if (b - c == diff) { b = c; } 
        else { res = 0; break; }
    }
    if (res) return res;

    // check third case
    b = number[start+1] - '0';
    for (int i = start+2; i < end; i++) {
        int c = number[i] - '0';
        if ((i-start) % 2 == 0) {
            if(a != c) { res = 0; break; }
            else { res = 3; }
        } else {
            if(b != c) { res = 0; break; }
            else { res = 3; }
        }
    }
    if (res) return res;
    else return 5;                              // last
}

int solution(int start, int index) {
    get_difficulty(start, 5, numbers[index]);
}

int main () {
    cin >> num_cases;
    cin.ignore();
    for (int i = 0; i < num_cases; i++) {
        getline(cin, numbers[i]);
    }

    for (int i = 0; i < num_cases; i++) {
        cout << solution(0, i) << endl;
    }

    return 0;
}