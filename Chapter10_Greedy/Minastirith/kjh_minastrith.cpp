#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
#include<map>
#define PI 3.14159265
#define INF 987654321

using namespace std;

pair<double, double> convertToStartLenPair(double a, double b, double r) {
    double theta = 2*asin(r/16);
    double loc = atan2(b,a) - theta;
    return make_pair(fmod(fmod(loc, 2*PI) + 2*PI, 2*PI), theta*2);
}

int coverable(vector<pair<double, double> > startings, multimap<double, double> cp) {
    int mincnt = INF;
    for (auto sitr = startings.begin(); sitr != startings.end(); sitr++) {
        auto checkpoints = cp;
        double start = sitr->first;
        if (start < 0.0000001) start += 2*PI;
        double end = fmod(start + sitr->second, 2*PI);

        int cnt = 1;
        // loop until end reaches to start
        while (end < start) {
            // itr up to ub(end)
            auto enditr = checkpoints.upper_bound(end);
            double maxend = end;
            multimap<double, double>::iterator maxitr;
            for (auto itr = checkpoints.begin(); itr != enditr; itr++) {
                double currend = itr->first + itr->second;
                if (currend > maxend) {
                    maxitr = itr;
                    maxend = currend;
                }
            }
            if (maxend <= end) { 
                cnt = -1;
                break;
            }
            end = maxend;
            cnt++;
            checkpoints.erase(maxitr);
        }
        if (cnt < 0) continue;
        mincnt = min(cnt, mincnt);
    }
    return mincnt;
}

int main() {
    ifstream cin("input.txt");
    int cases;
    cin >> cases;
    for (int c=0; c<cases; c++) {
        int n;
        cin >> n;
        vector<pair<double, double> > startings;
        multimap<double, double> checkpoints;
        for (int i = 0; i < n; i++) {
            double a, b, r;
            cin >> a >> b >> r;
            pair<double, double> tp;
            tp = convertToStartLenPair(a, b, r);

            if (tp.first < 0.0000001 || tp.first + tp.second >= 2*PI) startings.push_back(tp);
            checkpoints.insert(tp);
        }
        int cnt = coverable(startings, checkpoints);
        if (cnt==INF) cout << "IMPOSSIBLE" << '\n';
        else cout << cnt << '\n';
    }
    return 0;
}
