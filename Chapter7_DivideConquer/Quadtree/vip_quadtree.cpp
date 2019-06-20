#include <iostream>

#define N 1000
#define MIX 'x'

using namespace std;

string tree;
bool isLeafPrintable(int index) {
    return (tree[index] != MIX);
}

string reverseTree(int index) {
    string first(1, tree[index]);
    if (isLeafPrintable(index)){
        return first;
    }

    index += 1; string second = reverseTree(index);
    index += second.length(); string third = reverseTree(index);
    index += third.length(); string fourth = reverseTree(index);
    index += fourth.length(); string fifth = reverseTree(index);

    return first + fourth + fifth + second + third;
}

int main() {
    getline(cin, tree);
    cout << reverseTree(0) << endl;
    return 0;
}