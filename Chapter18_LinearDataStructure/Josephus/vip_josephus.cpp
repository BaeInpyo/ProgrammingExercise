#include <iostream>

using namespace std;

struct _Person {
  int number;
  struct _Person *prev;
  struct _Person *next;

  _Person(int number_, struct _Person *prev_, struct _Person *next_) {
    number = number_;
    prev = prev_;
    next = next_;
  }
};
using Person = struct _Person;

int num_tests;
int num_people;
int kth;
Person *first_person;

void initialize() {
  first_person = new Person(1, nullptr, nullptr);
  Person *prev_person = first_person;
  for (int i = 2; i <= num_people; ++i) {
    Person *curr_person = new Person(i, prev_person, nullptr);
    prev_person->next = curr_person;
    prev_person = curr_person;
  }
  prev_person->next = first_person;
  first_person->prev = prev_person;
}

Person *get_next_person(Person *curr_person) {
  Person *next_person = curr_person;
  for (int i = 0; i < kth-1; ++i) {
    next_person = next_person->next;
  }
  
  return next_person;
}

Person *kill_person(Person *curr_person) {
  Person *next_person = curr_person->next;
  curr_person->next->prev = curr_person->prev;
  curr_person->prev->next = curr_person->next;
  --num_people;
  return next_person;
}

void solution() {
  initialize();

  Person *curr_person = first_person;
  while (num_people > 2) {
    curr_person = kill_person(curr_person);
    curr_person = get_next_person(curr_person);
  }

  int person_number1 = curr_person->number;
  int person_number2 = curr_person->next->number;

  if (person_number1 > person_number2) {
    cout << person_number2 << " " << person_number1 << endl;
  } else {
    cout << person_number1 << " " << person_number2 << endl;
  }
  
  return;
}

int main() {
  cin.sync_with_stdio(false);
  
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_people; cin >> kth;
    solution();
  }
  return 0;
}
