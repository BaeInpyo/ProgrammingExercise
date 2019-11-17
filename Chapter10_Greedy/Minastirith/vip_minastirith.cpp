#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

#define MAX 100
#define PI_1 M_PI
#define PI_2 PI_1*2

using namespace std;

enum LOC {
  Y = 0,
  X = 1,
  R = 2,
};

struct Checkpoint {
  double start_degree;
  double end_degree;
  
  Checkpoint(double start, double end) : start_degree(start), end_degree(end) {}
};

typedef struct Checkpoint CKP;

int num_tests;
int num_checkpoints;
double location[MAX][3]; // 0: y, 1: x, 2: r
vector<CKP> aligned_checkpoints;
double r_castle = 8.0;

double distance_between_points(double x_i, double y_i, double x_j, double y_j) {
  return sqrt( pow(x_j - x_i, 2) + pow(y_j - y_i, 2) );
}

double distance(int i, int j) {
  double x_i = location[i][X];
  double y_i = location[i][Y];

  double x_j = location[j][X];
  double y_j = location[j][Y];

  return distance_between_points(x_i, y_i, x_j, y_j);
}

// Remove overlapped checkpoints
// only if 'i' checkpoint covers 'j'.
void remove_overlapped() {
  bool temp_location[MAX][3];
  bool deleted[MAX] = { false };
  for (int i = 0; i < num_checkpoints; ++i) {
    if (deleted[i]) continue;
    for (int j = 0; j < num_checkpoints; ++j) {
      if (i == j || deleted[j]) continue;

      double r_i = location[i][R];
      double r_j = location[j][R];
      
      if (r_i < r_j) continue;

      if (r_i - r_j >= distance(i, j)) {
        deleted[j] = true;
      }
    }
  }
  
  int temp_index = 0;
  for (int i = 0; i < num_checkpoints; ++i) {
    if (!deleted[i]) {
      location[temp_index][X] = location[i][X];
      location[temp_index][Y] = location[i][Y];
      location[temp_index][R] = location[i][R];
      ++temp_index;
    }
  }

  num_checkpoints = temp_index;
}

double calculate_degree(double c, int quadrant) {
  double cosine_theta = (128 - c*c) / 128.0;
  double theta = acos(cosine_theta);
  if (quadrant > 2) theta = PI_2 - theta;
  return theta;
}

void align_checkpoints() {
  aligned_checkpoints.clear();
  for (int i = 0; i < num_checkpoints; ++i) {
    double y = location[i][Y];
    double x = location[i][X];
    double r = location[i][R];
  
    // 1. Calculate center degree
    double c = distance_between_points(0, r_castle, x, y);
    double center_degree = (x >= 0) ? calculate_degree(c, 1) : calculate_degree(c, 3);

    // 2. Calculate start, end degree
    double temp_degree = calculate_degree(r, 1);
    double start_degree = center_degree - temp_degree;
    double end_degree = center_degree + temp_degree;

    aligned_checkpoints.emplace_back(CKP{start_degree, end_degree});
  }

  sort(aligned_checkpoints.begin(), aligned_checkpoints.end(), [](CKP a, CKP b) {
    return a.start_degree <= b.start_degree;
  });
  
  for (int i = 0; i < num_checkpoints; ++i) {
    CKP ckp_i = aligned_checkpoints[i];
    aligned_checkpoints.emplace_back(CKP{ckp_i.start_degree+PI_2, ckp_i.end_degree+PI_2});
  }
}

int greedy_solution(int start_index) {
  bool finished = false;
  CKP start_ckp = aligned_checkpoints[start_index];
  double first_degree = start_ckp.start_degree;
  double end_degree = start_ckp.end_degree;

  int count = 1;
  int chosen_index = start_index;
  while (!finished && chosen_index < start_index + num_checkpoints-1) {
    int next_index = chosen_index+1;
    while (next_index < start_index + num_checkpoints) {
      CKP next_ckp = aligned_checkpoints[next_index];
      if (next_ckp.start_degree > end_degree) {
        break;
      }
      ++next_index;
    }
    if (chosen_index == next_index-1) break;

    chosen_index = next_index-1;
    end_degree = aligned_checkpoints[chosen_index].end_degree;
    ++count;
    if (end_degree - first_degree >= PI_2) finished = true;
  }
  
  if (finished) return count;
  return 0;
}

void solution() {
  // Base case
  for (int i = 0; i < num_checkpoints; ++i) {
    if (location[i][R] >= r_castle*2) {
      cout << "1" << endl;
      return;
    }
  }

  remove_overlapped();
  align_checkpoints();
  int min_count = 100;
  for (int i = 0; i < num_checkpoints; ++i) {
    int count = greedy_solution(i);
    min_count = min(count, min_count);
  }
  if (min_count == 0) cout << "IMPOSSIBLE" << endl;
  else cout << min_count << endl;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_checkpoints;
    for (int i = 0; i < num_checkpoints; ++i) {
      cin >> location[i][Y];
      cin >> location[i][X];
      cin >> location[i][R];
    }

    solution();
  }
}
