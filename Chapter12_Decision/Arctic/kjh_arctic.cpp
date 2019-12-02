#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <list>
#include <unordered_set>
#include <iomanip>

using namespace std;

double dist[100][100];
double loc_x[100];
double loc_y[100];

void calDist(const int n) {
    for (int i = 0; i < n; i++) {
        dist[i][i] = 0;
        for (int j = i+1; j < n; j++) 
            dist[i][j] = dist[j][i] = sqrt(pow((loc_x[i]-loc_x[j]), 2) + pow((loc_y[i]-loc_y[j]), 2));
    }
}

bool solutionIsValid(const double d, const int n) {
    list<int> toVisit;
    toVisit.push_back(0);
    unordered_set<int> unvisited;
    for (int i = 1; i < n; i++) unvisited.insert(i);

    while (!toVisit.empty()) {
        int here = toVisit.front();
        toVisit.pop_front();

        for (auto itr = unvisited.begin(); itr != unvisited.end();) {
            if (dist[*itr][here] <= d) {
                toVisit.push_back(*itr);
                itr = unvisited.erase(itr);
            }
            else itr++;
        }
    }
    return unvisited.empty();

}

double solve(const int n) {
    calDist(n);
    double hi = 1415, lo = 0;
    for (int it = 0; it < 100; it++) {
        double mid = (hi + lo) / 2;
        if (solutionIsValid(mid, n))
            hi = mid;
        else 
            lo = mid;
    }
    return hi;
}

int main() {
    // ifstream cin("input.txt");
    int n_cases;
    cin >> n_cases;

    for (int c = 0; c < n_cases; c++) {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            double x, y;
            cin >> loc_x[i] >> loc_y[i];
        }
        cout << fixed << setprecision(2) << solve(n) << '\n';

        memset(dist, 0, sizeof(dist));
        memset(loc_x, 0, sizeof(loc_x));
        memset(loc_y, 0, sizeof(loc_y));
    }

}
