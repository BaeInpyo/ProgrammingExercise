#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int getCommonPrefix(const char *a, const char *b) {
    int ret = 0;
    while (*a && *a == *b) {
        a++; b++; ret++;
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int C;
    cin >> C;
    while (C--) {
        int k;
        cin >> k;
        string s;
        cin >> s;
        const char* charPtr = s.c_str();
        
        vector<int> suffixArray(s.length());
        for (int i = 0; i < s.length(); i++) {
            suffixArray[i] = i;
        }
        
        sort(suffixArray.begin(), suffixArray.end(),
            [&charPtr](int a, int b){
                return strcmp(charPtr+a, charPtr+b) < 0;
            }
        );
        
        int ret = 0;
        for (int i = k-1; i < s.length(); i++) {
            int cp = getCommonPrefix(charPtr + suffixArray[i], charPtr + suffixArray[i-k+1]);
            if (cp > ret) ret = cp;
        }
        cout << ret << '\n';
    }
    return 0;
}
