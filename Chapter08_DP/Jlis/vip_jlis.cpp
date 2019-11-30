#include <iostream>

using namespace std;

int N, M;
int *n_arr, *m_arr; 
int *cache;

int jlis(int n_idx, int m_idx) {
    int &ret = cache[n_idx*(M+1) + m_idx];
    if (ret != -1) return ret;

    ret = 1;
    if (n_idx == N && m_idx != M) {
        for (int i = m_idx + 1; i < M; i++) {
            if (m_arr[m_idx] < m_arr[i]) {
                ret = max(jlis(n_idx, i) + 1, ret);
            }
        }
        return ret;
    } else if (n_idx != N && m_idx == M) {
        for (int i = n_idx + 1; i < N; i++) {
            if (n_arr[n_idx] < n_arr[i]) {
                ret = max(jlis(i, m_idx) + 1, ret);
            }
        }
        return ret;
    } else if (n_idx == N && m_idx == M) {
        ret = 0;
        return ret;
    }

    int n_start = n_arr[n_idx];
    int m_start = m_arr[m_idx];
    
    if (n_start < m_start) {
        for (int i = n_idx + 1; i < N; i++) {
            if (n_start < n_arr[i]) {
                ret = max(jlis(i, m_idx) + 1, ret);
            }
        }
        for (int i = m_idx + 1; i < M; i++) {
            if (m_start < m_arr[i]) {
                ret = max(jlis(N, i) + 1, ret);
            }
        }
        if (n_idx == N-1) {
            ret += 1;
        }
    } else if (n_start > m_start) {
        for (int i = m_idx + 1; i < M; i++) {
            if (m_start < m_arr[i]) {
                ret = max(jlis(n_idx, i) + 1, ret);
            }
        }
        for (int i = n_idx + 1; i < N; i++) {
            if (n_start < n_arr[i]) {
                ret = max(jlis(i, M) + 1, ret);
            }
        }
        if (m_idx == M-1) {
            ret += 1;
        }
    } else {
        for (int i = n_idx + 1; i < N; i++) {
            if (n_start < n_arr[i]) {
                ret = max(jlis(i, m_idx+1) + 1, ret);
            }
        }
        for (int i = m_idx + 1; i < M; i++) {
            if (m_start < m_arr[i]) {
                ret = max(jlis(N, i) + 1, ret);
            }
        }
    }

    return ret;
}

int main() {
    int ret = -1;
    cin >> N; cin >> M;

    n_arr = new int[N];
    m_arr = new int[M];
    cache = new int[(N+1)*(M+1)];

    for (int i = 0; i < N; i++) {
        cin >> n_arr[i];
    }

    for (int i = 0; i < M; i++) {
        cin >> m_arr[i];
    }

    for (int i = 0; i < (N+1)*(M+1); i++) {
        cache[i] = -1;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int ret_jlis = jlis(i, j);
            ret = max(jlis(i, j), ret);
        }
    }

    cout << ret << endl;

    return 0;
}