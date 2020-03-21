#include <iostream>

#define MAX_N 10000
#define MAX_M 100000

using namespace std;

struct Comment {
  bool ack = false;
  int a = -1;
  int b = -1;
};

int num_tests;
int num_people;
int num_comments;
int parent[MAX_N];
int rank[MAX_N];
int size[MAX_N];
Comment comments[MAX_M];

void solution() {
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> num_comments;
    for (int i = 0; i < num_people; parent[i] = i, ++i);
    for (int i = 0; i < num_comments; ++i) {
      std::string type; cin >> type;
      if (type[0] == 'A') comments[i].ack = true;
      else comments[i].ack = false;

      cin >> comments[i].a;
      cin >> comments[i].b;
    }
    solution();
  }
  return 0;
}