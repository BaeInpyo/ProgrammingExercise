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

void install_camera(int here) {
  int children = 0;
  discovered[here] = counter++;
  for (int i = 0; i < adj[here].size(); ++i) {
    int there = adj[here][i];
    if (discovered[there] == -1) {
      ++children;
      install_camera(there);
    }
  }

  if (children > 0) {
    bool need_to_install = false;
    for (int i = 0; i < adj[here].size(); ++i) {
      int there = adj[here][i];
      if (discovered[there] > discovered[here] && !covered[there]) {
        need_to_install = true;
        break;
      }
    }
    if (need_to_install) {
      installed[here] = true;
      covered[here] = true;
      for (int i = 0; i < adj[here].size(); ++i) {
        int there = adj[here][i];
        covered[there] = true;
      }
    }
  }
}

void solution() {
  initialize();
  for (int i = 0; i < num_gallery; ++i) {
    if (discovered[i] == -1) install_camera(i);
    if (!covered[i]) installed[i] = true;
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
