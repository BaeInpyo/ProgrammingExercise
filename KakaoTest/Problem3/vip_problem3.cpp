#include <iostream>

int n, m; // n: lock, m: key
bool lock[20][20];
bool key[20][20];

bool is_range(int x, int y) {
    if (0 <= x && x < m && 0 <= y && y < m) return true;
    return false;
}

void rotate() {
    bool key_temp[20][20];
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            key_temp[i][j] = key[i][j];
        }
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            key[i][j] = key_temp[m-1-j][i];
        }
    }
}

bool solution() {
    for (int degree = 0; degree < 4; ++degree) {
        if (degree > 0) rotate();
        for (int m_loc_y = 0; m_loc_y < n+m-1; ++m_loc_y) {
            for (int m_loc_x = 0; m_loc_x < n+m-1; ++m_loc_x) {
                bool unlock = true;
                for (int n_y = 0; n_y < n; ++n_y) {
                    for (int n_x = 0; n_x < n; ++n_x) {
                        bool is_key = false;
                        int m_x = m-1 - m_loc_x + n_x;
                        int m_y = m-1 - m_loc_y + n_y;
                        if (is_range(m_x, m_y)) is_key = key[m_y][m_x];
                        if ((lock[n_y][n_x] && is_key) || (!lock[n_y][n_x] && !is_key)) {
                            unlock = false;
                            break;
                        }
                    }
                    if (!unlock) {
                        break;
                    }
                }
                if (unlock) 
                    return true;
            }
        }
    }
    return false;
}

int main() {
    std::cin >> n; std::cin >> m;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            int value; std::cin >> value;
            if (value == 1) key[i][j] = true;
            else key[i][j] = false;
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int value; std::cin >> value;
            if (value == 1) lock[i][j] = true;
            else lock[i][j] = false;
        }
    }
    
    std::cout << solution() << std::endl;
    return 0;
}