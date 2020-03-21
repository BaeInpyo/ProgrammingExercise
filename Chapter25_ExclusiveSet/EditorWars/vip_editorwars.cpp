#include <iostream>
#include <vector>
#include <unordered_map>

#define MAX_N 10000
#define MAX_M 100000

using namespace std;

int num_tests;
int num_people;
int num_comments;
int parent[MAX_N];
int height[MAX_N];
int party_size[MAX_N];
int disjoint_set[MAX_N];
int max_size;

void initialize() {
  for (int i = 0; i < num_people; ++i) parent[i] = i;
  for (int i = 0; i < num_people; ++i) height[i] = 1;
  for (int i = 0; i < num_people; ++i) party_size[i] = 1;
  for (int i = 0; i < num_people; ++i) disjoint_set[i] = -1;
  max_size = 0;
}

int find(int a) {
  if (a == parent[a]) return a;
  return parent[a] = find(parent[a]);
}

void merge(int a, int b) {
  int p_a = parent[a]; int p_b = parent[b];
  if (p_a == p_b) return;

  if (height[p_a] > height[p_b]) {
    int temp = p_a;
    p_a = p_b;
    p_b = temp;
  }

  if (height[p_a] == height[p_b]) ++height[p_b];

  parent[p_a] = p_b;
  party_size[p_b] += party_size[p_a];
  max_size = max(max_size, party_size[p_b]);
}

void solution() {
  initialize();
  int ith = 0;
  for (ith = 0; ith < num_comments; ++ith) {
    std::string type; cin >> type;
    int a; cin >> a;
    int b; cin >> b;

    if (type == "ACK") {
      int root_a = find(a);
      int root_b = find(b);
      if (disjoint_set[root_a] == root_b) {
        cout << "CONTRADICTION AT " << ith+1 << endl;
        break;
      }
      merge(root_a, root_b);

      int opp_a = disjoint_set[root_a];
      int opp_b = disjoint_set[root_b];

      if (opp_a == -1 && opp_b == -1) {
        continue;
      }
      
      if (opp_a != -1 && opp_b != -1) {
        merge(opp_a, opp_b);
      }
      disjoint_set[find(root_a)] = find(max(opp_a, opp_b));
      disjoint_set[find(max(opp_a, opp_b))] = find(root_a);
    } else {
      int root_a = find(a);
      int root_b = find(b);
      if (root_a == root_b) {
        cout << "CONTRADICTION AT " << ith+1 << endl;
        break;
      }
      
      int opp_a = disjoint_set[root_a];
      int opp_b = disjoint_set[root_b];

      if (opp_a != -1 && opp_b != -1) {
        merge(opp_b, root_a);
        merge(opp_a, root_b);
      } else if (opp_a == -1 && opp_b != -1) {
        merge(opp_b, root_a);
      } else if (opp_b == -1 && opp_a != -1) {
        merge(opp_a, root_b);
      }

      disjoint_set[find(max(opp_a, root_b))] = find(max(opp_b, root_a));
      disjoint_set[find(max(opp_b, root_a))] = find(max(opp_a, root_b));
    }
  }

  if (ith < num_comments) {
    while (ith < num_comments-1) {
      std::string temp0;
      int temp1, temp2;
      cin >> temp0; cin >> temp1; cin >> temp2;
      ++ith;
    }
    return;  
  }

  int ack_tree = -1;
  for (int i = 0; i < num_people; ++i) {
    if (parent[i] == i) {
      auto opp_i = disjoint_set[i];
      if (opp_i != -1) {
        if (party_size[i] > party_size[find(opp_i)]) {
          if (ack_tree == -1) ack_tree = i;
          else if (find(ack_tree) != find(i)) merge(ack_tree, i);
        } else {
          if (ack_tree == -1) ack_tree = find(opp_i);
          else if (find(ack_tree) != find(i)) merge(ack_tree, opp_i);
        }
      } else {
        if (ack_tree == -1) ack_tree = i;
        else merge(ack_tree, i);
      }
    }
  }
  cout << "MAX PARTY SIZE IS " << max_size << endl;

  return;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> num_comments;
    solution();
  }
  return 0;
}