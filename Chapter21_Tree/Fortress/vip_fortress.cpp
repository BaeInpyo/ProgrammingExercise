#include <iostream>
#include <vector>
#include <cmath>

#define MAX 100

using namespace std;

struct Wall {
  int x;
  int y;
  int r;
  vector<Wall *> inners;
  
  Wall(int _x, int _y, int _r) {
    x = _x;
    y = _y;
    r = _r;
  }

  ~Wall() {
    for (Wall *wall : inners) {
      delete wall;
    }
  }

  int Include(Wall *wall) {
    double distance = sqrt(pow(x - wall->x, 2.0) + pow(y - wall->y, 2.0));
    if (r > distance + wall->r) {
      return 1; 
    } else if (wall->r > distance + r) {
      return 2;
    }
    return 0;
  }

  int get_depth() {
    if (inners.empty()) return 1;
    else {
      int depth = 0;
      for (Wall *inner : inners) {
        depth = max(depth, inner->get_depth());
      }
      return depth+1;
    }
  }
};

class Fortress {
 public:
  Fortress(int x, int y, int r) : root_(new Wall(x, y, r)) {}
  ~Fortress() {
    delete root_;
  }

  void Insert(int x, int y, int r);
  void PrintNumCross();
 private:
  Wall *root_;
};

void Fortress::Insert(int x, int y, int r) {
  Wall *wall = new Wall(x, y, r);
  Wall *current = root_;
  while (true) {
    int include_state = 0;
    for (Wall *&child : current->inners) {
      include_state = child->Include(wall);
      if (include_state == 1) {
        current = child;
        break;
      } else if (include_state == 2) {
        wall->inners.push_back(child);
        child = wall;
        break;
      }
    }

    if (include_state == 0) {
      current->inners.push_back(wall);
      break;
    } else if (include_state == 2) {
      for (auto iter = current->inners.begin(); iter < current->inners.end(); ) {
        if (wall->Include(*iter) == 1) {
          wall->inners.push_back(*iter);
          iter = current->inners.erase(iter);
        } else {
          ++iter;
        }
      }
      break;
    }
  }
}

void Fortress::PrintNumCross() {
  if (root_->inners.empty()) {
    cout << 0 << endl;
    return;
  }
  vector<Wall *> &inners = root_->inners;
  int max_depth = inners[0]->get_depth();
  int snd_depth = -1;
  for (int i = 1; i < inners.size(); ++i) {
    int depth = inners[i]->get_depth();
    if (depth >= max_depth) {
      snd_depth = max_depth;
      max_depth = depth;
    } else if (depth >= snd_depth) {
      snd_depth = depth;
    }
  }

  if (snd_depth == -1) {
    cout << max_depth << endl;
  } else {
    cout << max_depth + snd_depth << endl;
  }
}

int num_tests;
int num_walls;

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_walls;

    int x; int y; int r;
    cin >> x; cin >> y; cin >> r;
    Fortress fortress = Fortress(x, y, r);
    for (int i = 1; i < num_walls; ++i) {
      cin >> x; cin >> y; cin >> r;
      fortress.Insert(x, y, r);
    }
    fortress.PrintNumCross();
  }
  return 0;
}
