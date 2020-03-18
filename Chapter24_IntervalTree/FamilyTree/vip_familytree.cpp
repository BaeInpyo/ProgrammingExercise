#include <iostream>
#include <vector>
#include <deque>

#define MAX_N 100000
#define MAX_Q 10000

using namespace std;

int num_tests;
int num_people;
int num_pairs;
vector<int> children_map[MAX_N];
int serialized[MAX_N];
int serial_map[MAX_N];
int pairs_first[MAX_Q];
int pairs_second[MAX_Q];
int depth[MAX_N];

class Person {
 public:
  Person(int _id) : id(_id) {}
  int get_id() { return id; }
  void PushChild(int child_id) { children.push_back(new Person(child_id)); }
  void PushChild(int parent_id, int child_id);
  Person *FindNextParent(int child_id);
  int CalcDepth(int child_id);
  void PrintPreOrder() {
    cout << id << endl;
    for (auto child : children) {
      child->PrintPreOrder();
    }
  }
  void PrintBFS() {
    for (auto child : children) {
      cout << child->id << endl;
    }
    for (auto child : children) {
      child->PrintBFS();
    }
  }
 private:
  vector<Person *> children;
  int id;
};

void Person::PushChild(int parent_id, int child_id) {
  Person *current = this;
  while (current->id != parent_id) {
    for (int i = current->children.size()-1 ; i >= 0; --i) {
      Person *child = current->children[i];
      if (parent_id >= child->id) {
        current = child;
        break;
      }
    }
  }
  current->PushChild(child_id);
  depth[child_id] = depth[current->id] + 1;
}

Person *Person::FindNextParent(int child_id) {
  for (int i = children.size()-1 ; i >= 0; --i) {
    Person *child = children[i];
    if (child_id >= child->id) {
      return child;
    }
  }
  return this;
}

int Person::CalcDepth(int child_id) {
  if (id == child_id) return 0;
  return 1 + FindNextParent(child_id)->CalcDepth(child_id);
}

int calcKinship(int a, int b, Person *root) {
  if (a == b) return 0;
  Person *next_parent_a = root->FindNextParent(a);
  Person *next_parent_b = root->FindNextParent(b);
  if (next_parent_a != next_parent_b) {
    return depth[a] + depth[b] - 2 * depth[root->get_id()];
  } else {
    return calcKinship(a, b, next_parent_a);
  }
}

void initialize() {
  int serial_no = 0;
  deque<pair<int, int>> stack;
  for (int child : children_map[0]) {
    stack.push_back({0, child});
  }
  while (!stack.empty()) {
    auto info = stack.front();
    stack.pop_front();
    serialized[serial_no] = info.first;

    for (int i = children_map[info.second].size() - 1; i >= 0; --i)
      stack.push_front({serial_no+1, children_map[info.second][i]});
    serial_map[info.second] = serial_no+1;
    ++serial_no;
  }
  for (int i = 0; i < num_people; ++i) children_map[i].clear();
}

void solution() {
  initialize(); 
  Person *root = new Person(0);
  depth[0] = 1;

  for (int i = 0; i < num_people-1; ++i) {
    root->PushChild(serialized[i], i+1);
  }

  for (int i = 0; i < num_pairs; ++i) {
    cout << calcKinship(serial_map[pairs_first[i]], serial_map[pairs_second[i]], root) << endl;
  }
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> num_pairs;
    for (int i = 0; i < num_people-1; ++i) {
      int p; cin >> p;
      children_map[p].push_back(i+1);
    }
    for (int i = 0; i < num_pairs; ++i) {
      cin >> pairs_first[i];
      cin >> pairs_second[i];
    }
    solution();
  }
  return 0;
}
