#include <iostream>
#include <vector>

#define STR_LEN 10000

int w, q;
std::string words[100000];
std::vector<std::string> queries;
std::vector<std::string> words_of_len[STR_LEN+1];

std::vector<int> solution() {
    std::vector<int> result;
    for (std::string q : queries) {
        
    }

    return result;
}

int main() {
    std::cin >> w; std::cin >> q;
    for (int i = 0; i < w; ++i) {
        std::string in_str; std::cin >> in_str;
        words_of_len[in_str.size()].push_back(in_str);
    }

    for (int i = 0; i < q; ++i) {
        std::string in_str; std::cin >> in_str;
        queries.push_back(in_str);
    }

    std::vector<int> result = solution();
    for (auto element : result) {
        std::cout << std::to_string(element) << " ";
    }

    std::cout << std::endl;
    return 0;
}