#include <iostream>
#include <vector>

using namespace std;

int num_gallery;
int num_hall;

vector<vector<int>> adj;
vector<int> discovered;
vector<bool> covered;
vector<bool> installed;
int counter;

void initialize() {
  discovered.clear();
  discovered.resize(num_gallery, -1);
  covered.clear();
  covered.resize(num_gallery, false);
  installed.clear();
  installed.resize(num_gallery, false);
  counter = 0;
}

void install_camera(int here, bool is_root) {
  int children = 0;
  discovered[here] = counter++;
  for (int i = 0; i < adj[here].size(); ++i) {
    int there = adj[here][i];
    if (discovered[there] == -1) {
      ++children;
      install_camera(there, false);
    }
  }

  if (!covered[here]) {
    int parent = here;
    int parent_size = 0;
    for (int i = 0; i < adj[here].size(); ++i) {
      int there = adj[here][i];
      if (discovered[there] < discovered[here]) {
        if (adj[there].size() > parent_size) {
          parent_size = adj[there].size();
          parent = there;
        }
      }
    }

    installed[parent] = true;
    covered[parent] = true;
    for (int i = 0; i < adj[parent].size(); ++i) {
      int there = adj[parent][i];
      covered[there] = true;
    }
  }
  
  if (children == 0) {
    if (is_root) installed[here] = true;
  }
}

void solution() {
  initialize();
  for (int i = 0; i < num_gallery; ++i) {
    if (discovered[i] == -1) install_camera(i, true);
  }

  int count = 0;
  for (int i = 0; i < num_gallery; ++i) {
    if (installed[i]) {
      ++count;
    }
  }
  cout << count << endl;
}

int main() {
  cin.sync_with_stdio(false);
  int c; cin >> c;
  while (c--) {
    cin >> num_gallery >> num_hall;
    adj.clear();
    adj.resize(num_gallery, {});
    for (int i = 0; i < num_hall; ++i) {
      int a; int b;
      cin >> a >> b;
      adj[a].push_back(b);
      adj[b].push_back(a);
    }
    solution();
  }
  return 0;
}
