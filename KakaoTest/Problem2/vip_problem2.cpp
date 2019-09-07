#include <iostream>

bool is_right_parenthesis(std::string p) {
    int stack = 0;
    for (int i = 0; i < p.size(); ++i) {
        char sub_p = p[i];
        if (sub_p == '(') {
            ++stack;
        } else {
            --stack;
        }
        if (stack < 0) {
            return false;
        }
    }

    if (stack != 0) return false;
    return true;
}

std::pair<std::string, std::string> split_uv(std::string p) {
    std::string u, v;
    int stack = 0;
    int pos = 0;
    for (; pos < p.size(); ++pos) {
        char sub_p = p[pos];
        if (sub_p == '(') ++stack;
        else --stack;

        if (stack == 0) {
            break;
        }
    }
    u = p.substr(0, pos+1);
    v = p.substr(pos+1);
    return std::make_pair(u, v);
}

std::string solution(std::string p) {
    if (p.size() == 0) return "";

    std::string answer = "";

    std::pair<std::string, std::string> uv = split_uv(p);
    std::string u = uv.first;
    std::string v = uv.second;

    if (is_right_parenthesis(u)) {
        return u + solution(v);
    }

    answer += "(";
    answer += solution(v);
    answer += ")";
    for (int i = 1; i < u.size() - 1; ++i) {
        char u_i = u[i];
        if (u_i == '(') answer += ')';
        else answer += '(';
    }

    return answer;
}

int main() {
    std::string in_str; std::cin >> in_str;
    std::cout << solution(in_str) << std::endl;

    return 0;
}