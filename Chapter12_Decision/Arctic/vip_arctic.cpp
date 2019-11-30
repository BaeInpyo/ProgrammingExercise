#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

#define MAX 100

struct Point {
  float x;
  float y;
};

int num_tests;
int num_camps;
Point camps[MAX];
float max_freq;
float distances[MAX][MAX];

float calc_distance(int src_idx, int dst_idx) {
  Point src = camps[src_idx];
  Point dst = camps[dst_idx];

  return sqrt((src.x - dst.x)*(src.x - dst.x) + (src.y - dst.y)*(src.y - dst.y));
}

void find_max_freq() {
  int num_connected = 1;
  bool connected_camps[MAX] = { false };
  connected_camps[0] = true;

  while (num_connected < num_camps) {
    int camp_index = -1;
    float min_distance = 100000;
    for (int i = 0; i < num_camps; ++i) {
      if (!connected_camps[i]) continue;
      for (int j = 0; j < num_camps; ++j) {
        if (i == j || connected_camps[j]) continue;
        if (distances[i][j] < min_distance) {
          min_distance = distances[i][j];
          camp_index = j;
        }
      }
    }
    
    if (min_distance > max_freq) {
      max_freq = min_distance;
    }
    connected_camps[camp_index] = true;
    ++num_connected;
  } 
}

void solution() {
  max_freq = 0;
  for (int i = 0; i < num_camps; ++i) {
    for (int j = 0; j < num_camps; ++j) {
      if (i != j) {
        distances[i][j] = calc_distance(i, j);
      }
    }
  }

  find_max_freq();
  cout << fixed << setprecision(2) << max_freq << endl;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_camps;
    for (int i = 0; i < num_camps; ++i) {
      cin >> camps[i].x; cin >> camps[i].y;
    }

    solution();
  }
}
