#include <iostream>

#define MAX_CITY 5000

using namespace std;

struct Signpost {
  int start;
  int end;
  int period;
};

int num_tests;
int num_cities;
int kth;
Signpost signpost_array[MAX_CITY];

int get_distance_near_start(int start, Signpost signpost) {
  if (start <= signpost.start) return signpost.start;

  return start + ((signpost.end - start) % signpost.period);
}

int get_distance_near_end(int end, Signpost signpost) {
  if (end >= signpost.end) return signpost.end;

  return end - ((end - signpost.start) % signpost.period);
}

/*
 * @brief If the kth signpost in the range between start and end, then true and its count
 *        Otherwise, return false with the count
 */
pair<bool, int> decision(int start, int end) {
  int count = 0;
  for (int i = 0; i < num_cities; ++i) {
    Signpost curr_signpost = signpost_array[i];
    if (curr_signpost.start > end) continue;
    if (curr_signpost.end < start) continue;
    
    int start_distance = get_distance_near_start(start, curr_signpost);
    int end_distance = get_distance_near_end(end, curr_signpost); 

    count += (end_distance - start_distance) / curr_signpost.period + 1;
  }

  return make_pair((kth <= count), count);
}

void solution() {
  int low = 0;
  int high = 8030000;

  while (low < high) {
    int mid = (low + high) / 2;

    auto result = decision(low, mid);
    bool in_range = result.first;
    int count = result.second; 
    if (in_range) {
      high = mid;
    } else {
      low = mid+1;
      kth -= count;
    }
  }
  cout << low << endl;
}

int main() {
  cin.sync_with_stdio(false);

  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> num_cities; cin >> kth;
    for (int i = 0; i < num_cities; ++i) {
      cin >> signpost_array[i].end;
      cin >> signpost_array[i].start;
      signpost_array[i].start = signpost_array[i].end - signpost_array[i].start;
      cin >> signpost_array[i].period;
    }

    solution();
  }
}
