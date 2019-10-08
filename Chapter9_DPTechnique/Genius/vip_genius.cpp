#include <iostream>

#define MAX_MUSIC 50
#define MAX_FAVOR 10
#define MAX_CACHE 5

using namespace std;

int num_tests;
int num_music;
int num_min;
int num_favorite;
int music_len[MAX_MUSIC];
double prob[MAX_MUSIC][MAX_MUSIC];
int favorite[MAX_FAVOR];

double cache[MAX_CACHE][MAX_MUSIC];

void init_cache() {
  for (int i = 0; i < MAX_CACHE; ++i) {
    for (int j = 0; j < num_music; ++j) {
      cache[i][j] = 0;
    }
  }
}

void solution() {
  init_cache();

  double base_prob = 1 / (double)num_music;
  for (int time = 1; time <= num_min; ++time) {
    for (int curr_music = 0; curr_music < num_music; ++curr_music) {
      int curr_music_len = music_len[curr_music];
      int music_end = time - curr_music_len;
      if (music_end < 0) continue;
      if (music_end == 0) cache[curr_music_len][curr_music] = base_prob;
      else {
        music_end = music_end % MAX_CACHE;
        for (int prev_music = 0; prev_music < num_music; ++prev_music) {
          double prev_prob = cache[music_end][prev_music];
          double curr_prob = prev_prob * prob[prev_music][curr_music];
          cache[time % MAX_CACHE][curr_music] = curr_prob;
        }
      }
    }
  } 

  int time = num_min % MAX_CACHE;
  for (int i = 0; i < num_favorite; ++i) {
    int favorite_music = favorite[i];
    int favorite_music_len = music_len[favorite_music];
    double curr_prob = 0;
    bool is_base_added = false;
    for (int prev_music = 0; prev_music < num_music; ++prev_music) {
      for (int music_end = num_min; music_end > num_min - favorite_music_len && music_end >= 0; --music_end) {
        double prev_prob = cache[music_end % MAX_CACHE][prev_music];
        if (!is_base_added && prev_prob == 0) {
          curr_prob += base_prob;
          is_base_added = true;
          break;
        }
        else {
          curr_prob += prev_prob * prob[prev_music][favorite_music];
        }
      }
    } 

    cout << curr_prob << " ";
  }
  cout << endl;
}

int main() {
  cin >> num_tests;

  while (--num_tests >= 0) {
    cin >> num_music; cin >> num_min; cin >> num_favorite;

    for (int i = 0; i < num_music; ++i) {
      cin >> music_len[i];
    }

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
