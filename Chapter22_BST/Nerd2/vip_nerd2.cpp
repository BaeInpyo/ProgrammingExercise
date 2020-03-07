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

class Participant {
  public:
    Participant(Info *info) : info_(info) {};
    ~Participant() { 
      info_ = nullptr;
      left_ = nullptr;
      right_ = nullptr;
    }
    Info *get_info() { return info_; }
    int get_num_problem() { return info_->num_problem; }
    int get_num_ramen() { return info_->num_ramen; }
    Participant *get_left() { return left_; }
    Participant *get_right() { return right_; }

    void set_info(Info *info) { info_ = info; }
    void set_left(Participant *left) { 
      left_ = left;
    }
    void set_right(Participant *right) { 
      right_ = right;
    }

    int Insert(Participant *candidate);
  private:
    bool ShouldDelete(Participant *candidate);
    void Replace(Participant *candidate);
    int Resolve(Participant *candidate);
    bool Delete();

    Info *info_ = nullptr;
    Participant *left_ = nullptr;
    Participant *right_ = nullptr;
};

bool Participant::ShouldDelete(Participant *candidate) {
  return (this->get_num_problem() < candidate->get_num_problem() &&
          this->get_num_ramen() < candidate->get_num_ramen());
}

int Participant::Insert(Participant *candidate) {
  Participant *current = this;
  while (true) {
    if (current->get_num_problem() > candidate->get_num_problem()) {
      if (current->get_num_ramen() > candidate->get_num_ramen()) {
        return 0;
      } else {
        Participant *left = current->get_left();
        if (left != nullptr) current = left;
        else {
          current->set_left(candidate);
          return 1;
        }
      }
    } else {
      if (current->get_num_ramen() > candidate->get_num_ramen()) {
        Participant *right = current->get_right();
        if (right != nullptr) current = right;
        else {
          current->set_right(candidate);
          return 1;
        }
      } else {
        return Resolve(candidate);
      }
    }
  }
}

void Participant::Replace(Participant *candidate) {
  this->set_info(candidate->get_info());
  this->set_left(candidate->get_left());
  this->set_right(candidate->get_right());
  delete candidate;
}

int Participant::Resolve(Participant *candidate) {
  int num_delete = 0;
  while (this->ShouldDelete(candidate)) {
    ++num_delete;
    if (!this->Delete()) {
      this->Replace(candidate);
      return -1 * num_delete + 1;
    }
  }
  return -1 * num_delete + this->Insert(candidate);
}

bool Participant::Delete() {
  Participant *left = this->get_left();
  Participant *right = this->get_right();
  Participant *new_root;
  if (left == nullptr && right == nullptr) {
    return false;
  } else if (left != nullptr && right == nullptr) {
    new_root = left;
  } else if (left == nullptr && right != nullptr) {
    new_root = right;
  } else {
    new_root = left;
    right->Insert(left->get_right());
    left->set_right(right);
  }

  this->Replace(new_root);
  return true;
}

class Contest {
 public:
  Contest() : root_(new Participant(&infos[0])), num_participants_(1) {}
  int get_num_participants();

  void Apply(int index);

 private:
  Participant *root_ = nullptr;
  int num_participants_ = 0;
};

int Contest::get_num_participants() { return num_participants_; }

void Contest::Apply(int index) {
  auto candidate = new Participant(&infos[index]);
  num_participants_ += root_->Insert(candidate);
}

void solution() {
  Contest contest;
  int result = 1;
  for (int i = 1; i < num_people; ++i) {
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