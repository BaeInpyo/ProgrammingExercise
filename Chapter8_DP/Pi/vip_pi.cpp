#include <iostream>

#define MAX 50000

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
    else res = 5;                               // fourth
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
            else { res = 4; }
        } else {
            if(b != c) { res = 0; break; }
            else { res = 4; }
        }
    }
    if (res) return res;
    else return 10;                              // last
}

int solution(int start, string number) {
    int three = MAX, four = MAX, five = MAX;
    int len = number.length() - start;
    if (len <= 5) {
        return get_difficulty(start, number.length(), number);
    }

    three = get_difficulty(start, start+3, number) + solution(start+3, number);

    if (len > 6) four  = get_difficulty(start, start+4, number) + solution(start+4, number);
    if (len > 7) five  = get_difficulty(start, start+5, number) + solution(start+5, number);

    return min(min(three, four), five);
}

int main () {
    cin >> num_cases;
    cin.ignore();
    for (int i = 0; i < num_cases; i++) {
        getline(cin, numbers[i]);
    }

    for (int i = 0; i < num_cases; i++) {
        cout << solution(0, numbers[i]) << endl;
    }

    return 0;
}