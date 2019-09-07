#include <iostream>
#include <unordered_map>

int solution(std::string in_str) {
    int len = in_str.size();
    int min_len = len;
    for (int unit = 1; unit <= len/2; ++unit) {
        std::string curr_key = in_str.substr(0, unit);
        int count = 1;
        int temp_len = unit;
        for (int i = unit; i < len; i += unit) {
            std::string next_key = in_str.substr(i, unit);
            if (curr_key == next_key) {
                count++;
            } else if (curr_key != next_key) {
                if (count != 1) {
                    std::string count_str = std::to_string(count);
                    temp_len += count_str.size();
                }
                count = 1;
                temp_len += next_key.size();
            }
            curr_key = next_key;
        }
        if (count != 1){
            std::string count_str = std::to_string(count);
            temp_len += count_str.size();
        }

        if (temp_len < min_len) {
            min_len = temp_len;
        }
    }

    return min_len;
}

int main() {
    std::string in_str;
    std::cin >> in_str;
    std::cout << solution(in_str) << std::endl;

    return 0;
}