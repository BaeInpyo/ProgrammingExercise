#include <iostream>
#include <stack>

#define Y "YES"
#define N "NO"

using namespace std;

int num_tests;
string brackets;

bool is_open(char bracket) {
  return (bracket == '(' || bracket == '{' || bracket == '[');
}

bool is_same_type(char b0, char b1) {
  return ((b0 == '(' && b1 == ')') || (b0 == '{' && b1 == '}') || (b0 == '[' && b1 == ']'));
}

void solution() {
  stack<char> status;
  for (char bracket : brackets) {
    if (is_open(bracket)) {
      status.push(bracket);
    } else {
      if (status.empty()) {
        cout << N << endl;
        return;
      } else {
        char top = status.top();
        if (is_same_type(top, bracket)) {
          status.pop();
        } else {
          cout << N << endl;
          return;
        }
      }
    }
  }

  if (!status.empty()) {
    cout << N << endl;
  } else {
    cout << Y << endl;
  }

  return;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> brackets;
    solution();
  }

  return 0;
}
