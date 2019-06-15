#include <iostream>
#include <algorithm>

#define N_CLOCK 16
#define N_SWITCH 10
#define NOT_FOUND -1

using namespace std;

int clocktime[N_CLOCK] = { };
bool switch_for_clock[N_SWITCH][N_CLOCK] = {
   // 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    { 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, // 0
    { 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0 }, // 1
    { 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1 }, // 2
    { 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 }, // 3
    { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0 }, // 4
    { 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 }, // 5
    { 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 }, // 6
    { 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1 }, // 7
    { 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, // 8
    { 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 }, // 9
};

bool isSync() {
    for (int i = 0; i < N_CLOCK; i++) {
        if (clocktime[i]) return false;
    }
    return true;
}

void turnClock(int switch_idx) {
    for (int clock_idx = 0; clock_idx < N_CLOCK; clock_idx++) {
        if (switch_for_clock[switch_idx][clock_idx]) 
            clocktime[clock_idx] = (clocktime[clock_idx] + 1) % 4;
    }
}

void revertClock(int switch_idx) {
    for (int clock_idx = 0; clock_idx < N_CLOCK; clock_idx++) {
        if (switch_for_clock[switch_idx][clock_idx]) {
            int cur_time = clocktime[clock_idx];
            clocktime[clock_idx] = (cur_time < 3) ? cur_time + 1 : 0;
        }
    }
}

int clockSync(int switch_idx) {
    int min_count, cur_count;

    if (switch_idx == N_SWITCH) return NOT_FOUND;
    
    // 0 rotate
    min_count = clockSync(switch_idx+1);

    // 1, 2, and 3 rotate
    for (int i = 1; i < 4; i++) {
        turnClock(switch_idx);

        cur_count = (isSync()) ? 0 : clockSync(switch_idx+1);

        if (cur_count != NOT_FOUND) {
            cur_count += i;
            if (min_count == NOT_FOUND) {
                min_count = cur_count;
            } else {
                min_count = min(min_count, cur_count);
            }
        }
    }

    revertClock(switch_idx);

    return min_count;
}

int main() {

    for (int i = 0; i < N_CLOCK; i++) {
        int time; cin >> time;
        clocktime[i] = (time / 3) % 4;
    }

    if (isSync()) {
        cout << "0" << endl;
        return 0;
    }

    cout << clockSync(0) << endl;

    return 0;
}
