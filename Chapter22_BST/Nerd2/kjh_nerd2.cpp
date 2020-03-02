#include <iostream>
#include <map>

using namespace std;

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
        auto data = map<int, int>();
        int n;
        cin >> n;
        int ret = 0;
        while (n--) {
            int p, q;
            cin >> p >> q;
            
            auto itr = data.lower_bound(p);
            if (itr == data.end() || itr->second < q) {
                data.insert(itr, make_pair(p, q));
                itr--; // itr points to (p, q)
                while (itr-- != data.begin()) {
                    if (itr->second < q) 
                        itr = data.erase(itr);
                    else break;
                }
            }
            ret += data.size();
        }
        cout << ret << '\n';
    }

    return 0;
}
