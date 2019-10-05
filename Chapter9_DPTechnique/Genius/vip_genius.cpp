#include <iostream>

#define MAX_MUSIC 50
#define MAX_FAVOR 10

using namespace std;

int num_tests;
int num_music;
int num_min;
int num_favorite;
double prob[MAX_MUSIC][MAX_MUSIC];
int favorite[MAX_FAVOR];

void solution() {
}

int main() {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_music; cin >> num_min; cin >> num_favorite;
    for (int i = 0; i < num_music; ++i) {
      for (int j = 0; j < num_music; ++j) {
        cin >> prob[i][j];
      }
    }

    for (int i = 0; i < num_favorite; ++i) {
      cin >> favorite[i];
    }
    
    solution();
  }

  return 0;
}
