#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool playGame() {
    string str = "";
    cin >> str;
    vector<char> stack;
    for (char c : str) {
        if (c == '(' || c == '{' || c == '[') {
            stack.push_back(c);
        } else {
            if (stack.empty()) {
                return false;
            }
            char opened = stack.back();
            if (!((opened == '(' && c == ')') ||
                  (opened == '{' && c == '}') ||
                  (opened == '[' && c == ']'))) {
                return false;
            }
            stack.pop_back();
        }
    }
    return stack.empty();
}

int main() {
    int C;
    cin >> C;
    for (int i=0; i<C; i++) {
        if (playGame() == true) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
