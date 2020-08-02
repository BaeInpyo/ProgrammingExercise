#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int C, N;
map<pair<string, string>, bool> cache;

bool match(string w, string s) {
    if (cache.count(make_pair(w, s)) > 0) {
        cout << "HIT" << endl;
        return cache.at(make_pair(w, s));
    }
    cout << "MISS" << endl;
    int pos = 0;
    while (pos < w.size() && pos < s.size() && (w[pos] == '?' || w[pos] == s[pos]))
        pos++;
    if (pos == w.size()) {
        bool result = (pos == s.size());
        cache.insert(make_pair(make_pair(w, s), result));
        return result;
    }
    else if (w[pos] == '*') {
        for (int i = pos; i <= s.size(); i++) {
            if (match(w.substr(pos+1), s.substr(i)))
                return true;
        }
    }
    cache.insert(make_pair(make_pair(w, s), false));
    return false;
}

void solution() {
    auto files = vector<string>();
    auto matched_files = vector<string>();
    cache.clear();
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

