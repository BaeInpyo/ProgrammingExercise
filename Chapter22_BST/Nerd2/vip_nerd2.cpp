#include <iostream>
#include <map>

#define MAX 50000

using namespace std;

struct Info {
  int num_problem;
  int num_ramen;
};

int num_tests;
int num_people;
Info infos[MAX];
map<int, int> participants;

void Insert(int index) {
  auto &info = infos[index];
  int num_problem = info.num_problem;
  int num_ramen = info.num_ramen;
  auto iter = participants.lower_bound(num_problem);
  if (iter == participants.end()) { // num_problem is biggest
    --iter;
    while (iter != participants.end() && iter->second < num_ramen) {
      iter = participants.erase(iter);
      if (participants.size() > 0) --iter;
    }
  } else {
    if (iter->second > num_ramen) {
      return;
    }
  }
  participants.insert({num_problem, num_ramen});
}

void solution() {
  participants.clear();
  int result = 1;
  participants.insert({infos[0].num_problem, infos[0].num_ramen});
  for (int i = 1; i < num_people; ++i) {
    Insert(i);
    result += participants.size();
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