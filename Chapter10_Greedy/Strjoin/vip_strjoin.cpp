#include <iostream>
#include <set>

using namespace std;

int num_tests;
int n;
int lengths[100];

void solution() {
  int result = 0;
  multiset<int> strcat_result;
  for (int i = 0; i < n; ++i) {
    strcat_result.insert(lengths[i]);
  }

  while (strcat_result.size() > 1) {
    int next_length = *(strcat_result.begin()) + *(++strcat_result.begin());
    result += next_length;
    strcat_result.erase(strcat_result.begin());
    strcat_result.erase(strcat_result.begin());
    strcat_result.insert(next_length);
  }
  cout << result << endl;
}

int main() {
  cin.sync_with_stdio(false);
  cin >> num_tests;
  while (--num_tests >= 0) {
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> lengths[i];
    }

    solution();
  }

  return 0;
}
