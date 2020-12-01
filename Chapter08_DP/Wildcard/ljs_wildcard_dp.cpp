#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string.h>


using namespace std;

int C, N;
int cache[101][101];
string strw, strs;

bool match(int w, int s) {
    int& ret = cache[w][s];
    if (ret != -1)
        return ret;
    if (w < strw.size() && s < strs.size() && (strw[w] == '?' || strw[w] == strs[s]))
        return match(w+1, s+1);
    if (w == strw.size()) {
        return ret = (s == strs.size());
    } else if (strw[w] == '*') {
        if (match(w+1, s) || (s < strs.size() && match(w, s+1)))
            return ret = 1;
    }
    return ret = 0;
}

void solution() {
    auto files = vector<string>();
    auto matched_files = vector<string>();
    cin >> strw >> N;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        files.push_back(s);
    }
    for (string s : files) {
        strs = s;
        memset(cache, -1, sizeof(cache));
        if (match(0, 0))
            matched_files.push_back(s);
    }

    sort(matched_files.begin(), matched_files.end());
    for (string s : matched_files)
        cout << s << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}

