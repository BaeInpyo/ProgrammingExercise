#include <iostream>

#define MAX_FILE 50
#define MAX_STR 100

using namespace std;

int num_files;
string pattern;
int pattern_ast[MAX_STR];
int num_ast = 0;
string files[MAX_FILE];

pair<bool, int> compare_string(int pattern_start, int pattern_end, int file_start, int file_idx, bool is_ast) {
    string file = files[file_idx];
    char pattern_first = pattern[pattern_start];
    bool found_next = false;
    int next = file_start + 1;

    for (int i = pattern_start; i < pattern_end; i++) {
        if (file_start >= file.length()) { return make_pair(false, file_start); }

        char file_i = file[file_start];
        char pattern_i = pattern[i];
        if (!(pattern_i == '?' || pattern_i == file_i)) { return make_pair(false, next); }

        // 두번째 비교부터 만약 패턴 처음 문자랑 같은 순간이 오면 그 위치 최초만 기록 (caching)
        if (i != pattern_start && file_i == pattern_first && !found_next) {
            found_next = true;
            next = file_start;
        }

        file_start++;
    }
    
    if (!is_ast && file_start != file.length()) return make_pair(false, next);
    return make_pair(true, file_start);
}

void find_asterisk() {
    int idx = 0;
    for (int i = 0; i < MAX_STR; i++) {
        pattern_ast[i] = -1;
    }

    for (int i = 0; i < pattern.length(); i++) {
        if (pattern[i] == '*') {
            pattern_ast[idx++] = i;
            num_ast++;
        }
    }
}

void find_pattern() {
    for (int i = 0; i < num_files; i++) {
        int pattern_start = 0, file_start = 0, pattern_end = pattern.length();
        bool strict_compare = true;
        pair<bool, int> result;

        for (int j = 0; j < num_ast; j++) {
            pattern_end = pattern_ast[j];
            if (pattern_end == 0) {
                pattern_start = 1;
                strict_compare = false;
            } else {
                while (true) {
                    result = compare_string(pattern_start, pattern_end, file_start, i, true);
                    file_start = result.second;
                    if (result.first) {
                        strict_compare = false;
                        pattern_start = pattern_end + 1;
                        break;
                    } else {
                        if (strict_compare) return;
                        if (files[i].length() - file_start < pattern_end - pattern_start) return;
                    }
                }
            }
        }

        if (pattern_end != pattern.length()-1) {
            result = compare_string(pattern_start, pattern.length(), file_start, i, false);
        }

        if (result.first) { cout << files[i] << endl; }
    }
}

int main() {
    getline(cin, pattern);

    cin >> num_files;
    cin.ignore();
    for (int i = 0; i < num_files; i++) {
        string file;
        getline(cin, file);
        files[i] = file;
    }
    find_asterisk();
    find_pattern();

    return 0;
}
