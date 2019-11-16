#include<iostream>
#include<fstream>
#include<unordered_map>
// #include<vector>
#include<array>
#include<algorithm>

using namespace std;
const int INF = 987654321;
int best;

void minDishes(const array<array<int, 51>, 50> &dishes, const int &n_dishes, const int &n_friends, int edible[], const int n) {
    if (n >= best) return;

    int toFeed = 1;
    for (; toFeed <= n_friends && edible[toFeed] > 0; toFeed++);
    if (toFeed > n_friends) {
        best = n;
        return;
    }
    for (int j = 0; j <= n_dishes; j++) {
        if (dishes[j][toFeed]) {
            for (int k = 1; k <= n_friends; k++) 
                if (dishes[j][k]) edible[k]++;
            minDishes(dishes, n_dishes, n_friends, edible, n+1);   
            for (int k = 1; k <= n_friends; k++) 
                if (dishes[j][k]) edible[k]--;
        }
    }
    return;
}

int main() {
    ifstream cin("input.txt");

    int ncases;
    cin >> ncases;
    for (int c=0; c<ncases; c++) {
        int n_friends, n_dishes;
        array<array<int, 51>, 50> dishes;
        dishes.fill({});

        cin >> n_friends >> n_dishes;
        unordered_map<string, int> nameIndexMap;
        int edible[51] = {0};
        for (int i = 1; i <= n_friends; i++) {
            string name;
            cin >> name;
            nameIndexMap[name] = i;
        }
        for (int i = 0; i < n_dishes; i++) {
            int k;
            cin >> k;
            dishes[i][0] = k;
            for (int j = 0; j < k; j++) {
                string name;
                cin >> name;
                dishes[i][nameIndexMap[name]] = 1;
            }
        }
        sort(dishes.begin(), dishes.begin() + n_dishes, [](const array<int, 51> &a, const array<int, 51> &b) {
            return a[0] > b[0];
        });
        best = INF;
        minDishes(dishes, n_dishes, n_friends, edible, 0);
        cout << best << '\n';
    }
    return 0;
}
