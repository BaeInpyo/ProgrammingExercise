#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int C, N;

bool match(string w, string s) {
    int pos = 0;
    while (pos < w.size() && pos < s.size() && (w[pos] == '?' || w[pos] == s[pos]))
        pos++;
    if (pos == w.size())
        return pos == s.size();
    else if (w[pos] == '*') {
        for (int i = pos; i <= s.size(); i++) {
            if (match(w.substr(pos+1), s.substr(i)))
                return true;
        }
    }
    return false;
}

void solution() {
    auto files = vector<string>();
    auto matched_files = vector<string>();
    string w;
    cin >> w >> N;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        files.push_back(s);
    }
    for (string s : files)
        if (match(w, s))
            matched_files.push_back(s);

    sort(matched_files.begin(), matched_files.end());
    for (string s : matched_files)
        cout << s << endl;
}

int main() {
    cin >> C;
    for (int i=0; i<C; i++) solution();
    return 0;
}

