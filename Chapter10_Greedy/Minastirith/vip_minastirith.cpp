#include <iostream>
#include <math>

#define MAX 100

using namespace std;

enum LOC {
  Y = 0,
  X = 1,
  R = 2,
};

struct Point {
  double x;
  double y;
  char quadrant;
};

struct Checkpoint {
  Point start;
  Point center;
  Point end;
};

int num_tests;
int num_checkpoints;
double location[MAX][3]; // 0: y, 1: x, 2: r
vector<Point> aligned_checkpoints;
vector<Point> start_checkpoints;

double distance(int i, int j) {
  double x_i = location[i][X];
  double x_j = location[j][X];

  double y_i = location[i][Y];
  double y_j = location[j][Y];

  return sqrt( pow(x_j - x_i, 2) + pow(y_j - y_i, 2) );
}

// Remove overlapped checkpoints
// only if 'i' checkpoint covers 'j'.
void remove_overlapped() {
  bool temp_location[MAX][3];
  bool deleted[MAX] = { false };
  for (int i = 0; i < num_checkpoints && !deleted[i]; ++i) {
    for (int j = 0; j < num_checkpoints && i != j && !deleted[j]; ++j) {
      double r_i = location[i][R];
      double r_j = location[j][R];
      
      if (r_i < r_j) break;

      if (r_i - r_j > distance(i, j)) {
        deleted[j] = true;
      }
    }
  }
  
  int temp_index = 0;
  for (int i = 0; i < num_checkpoints; ++i) {
    if (i == temp_index) continue;
    if (!deleted[i]) {
      location[temp_index][X] = location[i][X];
      location[temp_index][Y] = location[i][Y];
      location[temp_index][R] = location[i][R];
      ++temp_index;
    }
  }

  num_checkpoints = temp_index;
}

auto f = [](const Point &a, const Point &b) {
  bool result;
  if (a.quadrant < b.quadrant) result = true;
  else if (a.quadrant == b.quadrant) {
    switch(a.quadrant) {
      case 1:
        if (a.
        break;
      case 2:
        break;
      case 3:
        break;
      case 4:
        break;
    }
  } else result = false;
  return result;
}

void align_checkpoints() {

  sort(aligned_checkpoints.begin(), aligned_checkpoints.end(), f);
}

void solution() {
  remove_overlapped();
  align_checkpoints();
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_checkpoints;
    for (int i = 0; i < num_checkpoints; ++i) {
      cin >> location[i][LOC::Y];
      cin >> location[i][LOC::X];
      cin >> location[i][LOC::R];
    }

    solution();
  }
}
