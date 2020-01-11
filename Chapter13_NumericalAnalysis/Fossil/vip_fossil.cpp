#include <iostream>
#include <utility>
#include <algorithm>
#include <iomanip>

//#define DEBUG
#define MAX 100

using namespace std;

struct _Point {
  double x;
  double y;
};

using Point = struct _Point;

int num_tests;

int num_a_points;
Point A[MAX];
int min_A_x_index;
int max_A_x_index;
double min_A_x;
double max_A_x;
double min_A_y;
double max_A_y;

int num_b_points;
Point B[MAX];
int min_B_x_index;
int max_B_x_index;
double min_B_x;
double max_B_x;
double min_B_y;
double max_B_y;

bool upper_b;

pair<double, double> get_A_ys(double input_x) {
  int index = min_A_x_index;
  double lo_y = min_A_y; double hi_y = max_A_y;
  double x0 = A[index].x; double y0 = A[index].y;

  // A Below
  while (index != max_A_x_index) {
    index = (index+1 == num_a_points) ? 0 : index+1;
    double x1 = A[index].x; double y1 = A[index].y;
    if (x0 <= input_x && input_x <= x1) {
      if (x0 == x1) {
        lo_y = min(y0, y1);
      } else {
        lo_y = (y1-y0) * (input_x - x0) / (x1-x0) + y0;
      }
      break;
    }
    x0 = x1; y0 = y1;
  }

  index = min_A_x_index;
  x0 = A[index].x; y0 = A[index].y;
  // A Upper
  while (index != max_A_x_index) {
    index = (index-1 < 0) ? num_a_points-1 : index-1;
    double x1 = A[index].x; double y1 = A[index].y;
    if (x0 <= input_x && input_x <= x1) {
      if (x0 == x1) {
        hi_y = max(y0, y1);
      } else {
        hi_y = (y1-y0) * (input_x - x0) / (x1-x0) + y0;
      }
      break;
    }
    x0 = x1; y0 = y1;
  }

  return make_pair(lo_y, hi_y);
}

pair<double, double> get_B_ys(double input_x) {
  int index = min_B_x_index;
  double lo_y = min_B_y; double hi_y = max_B_y;
  double x0 = B[index].x; double y0 = B[index].y;

  // B Below
  while (index != max_B_x_index) {
    index = (index+1 == num_b_points) ? 0 : index+1;
    double x1 = B[index].x; double y1 = B[index].y;
    if (x0 <= input_x && input_x <= x1) {
      if (x0 == x1) {
        lo_y = min(y0, y1);
      } else {
        lo_y = (y1-y0) * (input_x - x0) / (x1-x0) + y0;
      }
      break;
    }
    x0 = x1; y0 = y1;
  }

  index = min_B_x_index;
  x0 = B[index].x; y0 = B[index].y;
  // B Upper
  while (index != max_B_x_index) {
    index = (index-1 < 0) ? num_b_points-1 : index-1;
    double x1 = B[index].x; double y1 = B[index].y;
    if (x0 <= input_x && input_x <= x1) {
      if (x0 == x1) {
        hi_y = max(y0, y1);
      } else {
        hi_y = (y1-y0) * (input_x - x0) / (x1-x0) + y0;
      }
      break;
    }
    x0 = x1; y0 = y1;
  }

  return make_pair(lo_y, hi_y);
}

double get_distance(pair<double, double> A_ys, pair<double, double> B_ys) {
  double lo_y_A = A_ys.first;
  double hi_y_A = A_ys.second;

  double lo_y_B = B_ys.first;
  double hi_y_B = B_ys.second;

  double distance = min(hi_y_A, hi_y_B) - max(lo_y_A, lo_y_B);

  return distance;
}

void solution() {
#ifdef DEBUG
  cout << "[A] X: " << min_A_x << " ~ " << max_A_x << endl;
  cout << "    i: " << min_A_x_index << ", " << max_A_x_index << endl;
  cout << "[B] X: " << min_B_x << " ~ " << max_B_x << endl;
  cout << "    i: " << min_B_x_index << ", " << max_B_x_index << endl;
#endif
  if (max_A_x < min_B_x || max_B_x < min_A_x) {
    cout << 0 << endl;
    return;
  }

  double lo = max(min_A_x, min_B_x);
  double hi = min(max_A_x, max_B_x);
  double tri0_distance; 
  double tri1_distance; 

#ifdef DEBUG
  cout << lo << " " << hi << " " << upper_b << endl;
#endif
  for (int i = 0; i < 100; ++i) {
    double tri0 = (2*lo+hi)/3.0;
    double tri1 = (lo+2*hi)/3.0;
    
    auto tri0_A_ys = get_A_ys(tri0);
    auto tri0_B_ys = get_B_ys(tri0);
    
    auto tri1_A_ys = get_A_ys(tri1);
    auto tri1_B_ys = get_B_ys(tri1);

    tri0_distance = get_distance(tri0_A_ys, tri0_B_ys);
    tri1_distance = get_distance(tri1_A_ys, tri1_B_ys);
    
#ifdef DEBUG
    cout << "[" << i << "]: " << endl;
    cout << "  Tri0: " << tri0 << ", Tri1: " << tri1 << " | " << endl;
    cout << "  -Tri0-" << endl;
    cout << "    A_ys: " << tri0_A_ys.first << ", " << tri0_A_ys.second << endl;
    cout << "    B_ys: " << tri0_B_ys.first << ", " << tri0_B_ys.second << endl;
    cout << "    DIST: " << tri0_distance << endl;
    cout << "  -Tri1-" << endl;
    cout << "    A_ys: " << tri1_A_ys.first << ", " << tri1_A_ys.second << endl;
    cout << "    B_ys: " << tri1_B_ys.first << ", " << tri1_B_ys.second << endl;
    cout << "    DIST: " << tri1_distance << endl;
#endif

    if (tri0_distance < tri1_distance) {
      lo = tri0;
    } else {
      hi = tri1;
    }
  }

  if (tri0_distance < 0) cout << 0 << endl;
  else cout << setprecision(8) << tri0_distance << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_a_points; cin >> num_b_points;
    min_A_x = 101; max_A_x = -1;
    min_A_y = 101; max_A_y = -1;
    for (int i = 0; i < num_a_points; ++i) {
      double x, y; cin >> x; cin >> y;
      if (min_A_x >= x) {
        min_A_x = x;
        min_A_x_index = i;
      }
      if (max_A_x <= x) {
        max_A_x = x;
        max_A_x_index = i;
      }
      min_A_y = min(min_A_y, y);
      max_A_y = max(max_A_y, y);
      A[i].x = x; A[i].y = y;
    }

    min_B_x = 101; max_B_x = -1;
    min_B_y = 101; max_B_y = -1;
    for (int i = 0; i < num_b_points; ++i) {
      double x, y; cin >> x; cin >> y;
      if (min_B_x >= x) {
        min_B_x = x;
        min_B_x_index = i;
      }
      if (max_B_x <= x) {
        max_B_x = x;
        max_B_x_index = i;
      }
      min_B_y = min(min_B_y, y);
      max_B_y = max(max_B_y, y);
      B[i].x = x; B[i].y = y;
    }

    solution();
  }

  return 0;
}
