#include <iostream>

#define MAX 50000

using namespace std;

struct Info {
  int num_problem;
  int num_ramen;
};

int num_tests;
int num_people;
Info infos[MAX];

class Contest {
 public:
  void Apply(int index);
  int get_num_participants();

 private:
  struct Participant {
    int index = -1;
    Participant *left = nullptr;
    Participant *right = nullptr;
  };

  Participant *root_ = nullptr;  
  int num_participants_ = 0;
};

void Contest::Apply(int index) {}
int Contest::get_num_participants() { return num_participants_; }

void solution() {
  Contest contest;
  int result = 0;
  for (int i = 0; i < num_people; ++i) {
    contest.Apply(i);
    result += contest.get_num_participants();
  }
  cout << result << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people;
    for (int i = 0; i < num_people; ++i) {
      cin >> infos[i].num_problem; cin >> infos[i].num_ramen;
    }
    solution();
  }
  return 0;
}