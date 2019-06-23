#include <iostream>
#include <vector>

#define WILDCARD_ANY '*'
#define WILDCARD_ONE '?'

using namespace std;

int num_files;
string pattern;
vector<string> files;

pair<int,int> find_substring(string file, int file_idx, string pattern, int pattern_idx, bool from_wildcard) {
    int file_start=file_idx;
    int pattern_start=pattern_idx;

    if (!from_whildcard) {
        while(pattern_idx < pattern.length() && pattern[pattern_idx] != '*') {
            if (pattern[pattern_idx] != '?' && pattern[pattern_idx] != file[file_idx]) {
                return make_pair(0,0);
            }
            
            pattern_idx++; file_idx++;
        }
    } else {
        while(file_idx < file.length() && pattern_idx < pattern.length() && pattern[pattern_idx] != '*') {
            if (pattern[pattern_idx] == file[file_idx]) {
                if (file_idx + 1 < file.length() && pattern[pattern_idx] != file[file_idx+1]) {
                    pattern_idx++;
                }
            } else if (pattern[pattern_idx] == '?') {
                pattern_idx++;
            }
            file_idx++;
        }
    }
    
    return make_pair(file_idx, pattern_idx);
}

void find_pattern() {
    for (auto it = files.begin(); it != files.end(); ++it) {
        string file = *it;

        int pattern_idx = 0;
        int file_idx = 0;
        pair<int,int> next_pos;
        bool from_wildcard = false;

        while (file_idx < file.length()) {
            if (pattern_idx == pattern.length()) {
                break;
            }

            char pattern_char = pattern[pattern_idx];
            //cout << file[file_idx] << " & " << pattern[pattern_idx] << endl;
            if (pattern_char == '*') {
                pattern_idx++;
                from_wildcard = true;
                continue;
            }

            next_pos = find_substring(file, file_idx, pattern, pattern_idx, from_wildcard);
            int file_next_pos = next_pos.first();
            int pattern_next_pos = next_pos.second();

            if (!file_next_pos) {
                file_idx += 1;
            } else {
                file_idx = file_next_pos;
                pattern_idx = pattern_next_pos;
            }
        }

        if (pattern_idx == pattern.length()) {
            if (!(pattern[pattern_idx-1] != '*' && file_idx != file.length())) {
                cout << file << endl;
            }
        } else {
            if (pattern[pattern_idx] == '*') {
                cout << file << endl;
            }
        }
    }
}

int main() {
    getline(cin, pattern);

    cin >> num_files;

    for (int i = 0; i <= num_files; i++) {
        string file;
        getline(cin, file);
        if (i != 0) files.push_back(file);
    }

    find_pattern();

    return 0;
}
