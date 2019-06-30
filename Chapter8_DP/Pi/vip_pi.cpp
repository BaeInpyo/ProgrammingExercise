#include <iostream>

using namespace std;

string number[50];

int get_difficulty() {

}

int main () {
    int num_cases;
    cin >> num_cases;

    for (int i = 0; i < num_cases; i++) {
        getline(cin, number[i]);
    }

    for (int i = 0; i < num_cases; i++) {
        cout << get_difficulty() << endl;
    }

    return 0;
}