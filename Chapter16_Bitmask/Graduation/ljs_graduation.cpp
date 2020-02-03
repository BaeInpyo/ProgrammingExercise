#include <iostream>
#include <vector>

using namespace std;

static const int INF = 987654321;
static int N, K, M, L;
static int prerequsites[12];
static int classes[10];

int count(int taken) {
    if (taken == 0) return 0;
    return taken%2 + count(taken/2);
}

int cannotTake(int newClass, int taken) {
    int prerequsite = prerequsites[newClass];
    return (taken & prerequsite) == prerequsite ? 0 : 1;
}

int graduate(int semester, int taken, int enrolledSemester) {
    int ret = INF;
    if (count(taken) >= K) return enrolledSemester; // taken all required classes
    if (semester == M) return ret;           // all semesters finished : IMPOSSIBLE
    int openClasses = classes[semester] & (~taken);
    for (int i=0; i<N; i++) {
        openClasses &= ~(cannotTake(i, taken) << i);
    }

    for (int subset = openClasses; subset > 0; subset = ((subset-1) & openClasses)) {
        if (count(subset) > L) continue; // cannot take more than L classes
        ret = min(ret, graduate(semester+1, taken | subset, enrolledSemester+1));
    }
    return min(ret, graduate(semester+1, taken, enrolledSemester));
}

void playGame() {
    cin >> N >> K >> M >> L;
    int ret;
    int taken = 0;

    for (int i=0; i<12; i++) prerequsites[i] = 0;
    for (int i=0; i<10; i++) classes[i] = 0;
    
    for (int i=0; i<N; i++) {
        int n;
        cin >> n;
        for (int j=0; j<n; j++) {
            int prer;
            cin >> prer;
            prerequsites[i] |= (1 << prer);
        }
    }
    for (int i=0; i<M; i++) {
        int n;
        cin >> n;
        for (int j=0; j<n; j++) {
            int open;
            cin >> open;
            classes[i] |= (1 << open);
        }
    }
    ret = graduate(0, taken, 0);
    if (ret == INF) cout << "IMPOSSIBLE" << endl;
    else cout << ret << endl;
}

int main() {
    int C;
    cin >> C;
    for (int i=0; i<C; i++) {
        playGame();
    }
    return 0;
}
