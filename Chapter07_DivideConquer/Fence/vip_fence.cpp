#include <iostream>
#include <vector>

using namespace std;

int total_cnt;
vector<int> fence;

int find_rectangle() {
    int area = -1;
    for (int i = 0; i < total_cnt; i++) {
        int height = fence[i];
        int width = 1;

        // left
        for (int left = i-1; left >= 0 && fence[left] >= height; left--) {
            width++;
        }

        // right
        for (int right = i+1; right < total_cnt && fence[right] >= height; right++) {
            width++;
        }

        area = max(area, height*width);
    }
    return area;
}

int main() {
    cin >> total_cnt;

    for (int i = 0; i < total_cnt; i++) {
        int height;
        cin >> height;
        fence.push_back(height);
    }

    cout << find_rectangle() << endl;
    return 0;
}
