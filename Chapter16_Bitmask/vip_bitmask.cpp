#include <iostream>

#define MAX_C 12
#define MAX_S 10

using namespace std;

int num_tests;
int num_courses;
int num_must_take;
int num_semester;
int max_course_in_semester;

int priors[MAX_C];
int courses[MAX_S];

void solution() {
#ifdef DEBUG
  for (int i = 0; i < num_courses; ++i) {
    cout << "PRIOR[" << i << "]: " << priors[i] << endl;
  }

  for (int i = 0; i < num_semester; ++i) {
    cout << "COURSE[" << i << "]: " << courses[i] << endl;
  }
#endif
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_courses;
    cin >> num_must_take;
    cin >> num_semester;
    cin >> max_course_in_semester;

    for (int i = 0; i < num_courses; ++i) {
      int count; cin >> count;
      priors[i] = 0;
      for (int j = 0; j < count; ++j) {
        int course; cin >> course;
        priors[i] |= (1 << course);
      }
    }

    for (int i = 0; i < num_semester; ++i) {
      int count; cin >> count;
      courses[i] = 0;
      for (int j = 0; j < count; ++j) {
        int course; cin >> course;
        courses[i] |= (1 << course);
      }
    }

    solution();
  }

  return 0;
}
