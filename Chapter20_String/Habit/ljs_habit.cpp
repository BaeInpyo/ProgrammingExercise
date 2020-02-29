#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int commonPrefix(string s1, string s2) {
    int ret = 0;
    for (ret=0; ret<s1.size(); ret++) {
        if (s1[ret] != s2[ret]) break;
    }
    return ret;
}

vector<string>& getSuffixArray(string& s) {
    vector<string>& ret = *(new vector<string>());
    for (int i=0; i<s.size(); i++) {
        ret.push_back(s.substr(i));
    }
    sort(ret.begin(), ret.end());
    return ret;
}

void solution() {
    int K;
    int curr = 0, ret = 0;
    string speech;
    cin >> K;
    cin >> speech;
    vector<string>& suffixArray = getSuffixArray(speech);
    for (int i=0; i+K-1 < suffixArray.size(); i++) {
        curr = commonPrefix(suffixArray[i], suffixArray[i+K-1]);
        if (curr > ret) {
             ret = curr;
        }
    }
    cout << ret << endl;
    delete &suffixArray;
}

int main() {
    int C;
    cin >> C;
    while (C--) {
        solution();
    }
    return 0;
}
