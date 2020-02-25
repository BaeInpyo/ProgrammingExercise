#include <iostream>

using namespace std;

int shift(string source, string target, bool clockwise) {
    return clockwise ? (target + target).find(source) : (source + source).find(target);
}

void solution() {
    bool clockwise = true;
    int N;
    int result = 0;
    string source;
    string target;
    cin >> N;
    cin >> source;
    for (int i=0; i<N; i++) {
        cin >> target;
        result += shift(source, target, clockwise);
        clockwise = !clockwise;
        source = target;
    }
    cout << result << endl;
}

int main() {
    int C;
    cin >> C;
    for (int i=0; i<C; i++) {
        solution();
    }
}

