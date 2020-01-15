#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

#define MAX(a, b) (a)>(b)? (a):(b)
#define pdd pair<double, double> 

pdd fp[2][100];
int n[2];

pdd getIntersection(pdd &p, pdd &q0, pdd &q1) {
    double m = (q0.second - q1.second) / (q0.first - q1.first);
    double b = q0.second - m*q0.first;
    return make_pair(p.first, p.first * m + b);
}

vector<pdd> findVerticalIntersections(pdd &p) {
    vector<pdd> ret;
//    ret.push_back(p);
    for (int k = 0; k < 2; k++)
        for (int i = 0; i < n[k]; i++) {
            pdd &q0 = fp[k][i];
            pdd &q1 = fp[k][(i + 1)%n[k]];
            //if (p == q0 || p == q1) continue;
            if ((q0.first < p.first && p.first <= q1.first) ||
                (q1.first <= p.first && p.first < q0.first)) {
                // has intersection
                pdd intersection = getIntersection(p, q0, q1);
                ret.push_back(intersection);
            }
        }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int c;
    std::cin >> c;
    while (c--) {
        std::cin >> n[0] >> n[1];

        memset(fp, 0, sizeof(fp));        

        for (int i = 0; i < n[0]; i++) {
            double _x, _y;
            std::cin >> _x >> _y;
            fp[0][i].first = _x;
            fp[0][i].second = _y; 
        }
        for (int i = 0; i < n[1]; i++) {
            double _x, _y;
            std::cin >> _x >> _y;
            fp[1][i].first = _x;
            fp[1][i].second = _y; 
        }

        double result = 0.0;

        for (int k = 0; k < 2; k++)
            for (int i = 0; i < n[k]; i++) {
                vector<pdd> pdds = findVerticalIntersections(fp[k][i]);
                if (pdds.size() >= 4) {
                    // for (auto _p: pdds) std::cout << _p.first << ", " << _p.second << endl;

                    vector<double> ys(4);
                    transform(pdds.begin(), pdds.end(), ys.begin(),
                        [](pdd p) -> double {return p.second;});
                    if (ys[0] < ys[2] && ys[0] < ys[3] && ys[1] < ys[2] && ys[1] < ys[3])
                        break;
                    if (ys[2] < ys[0] && ys[2] < ys[1] && ys[3] < ys[0] && ys[3] < ys[1])
                        break;
                    // for (auto _y: ys) std::cout << _y << endl;
                    sort(ys.begin(), ys.end());
                    result = MAX(result, ys[2] - ys[1]);
                }
            }
        std::cout << fixed << setprecision(10) << result << '\n';
    }

    return 0;
}
