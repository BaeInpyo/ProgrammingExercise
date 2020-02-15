#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        string curr;
        cin >> curr;
        int ret = 0;
        for (int i = 0; i < n; i++) {
            string next;
            cin >> next;
            if (i&1) // anticlockwise
                ret += (curr+curr).find(next);
            else // clockwise
                ret += (next+next).find(curr);
            curr = next;
        }
        cout << ret << '\n';
    }
    return 0;
}
