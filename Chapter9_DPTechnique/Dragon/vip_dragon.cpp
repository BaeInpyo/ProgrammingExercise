#include <iostream>

#define N 50

using namespace std;

int num_tests;
int gen;
int start_index;
int len;

int count_char[N+1];
string cache_sequence[N+1];
string result_sequence = "";

void init_cache() {
	for (int i = 0; i <= N; ++i) {
		cache_sequence[i] = "";
		count_char[i] = 0;
	}
}

/*
 * Calculate the number of characters in nth sequence
 */
void calculate_count() {
	count_char[0] = 2;
	for (int i = 1; i <= N; ++i) {
		count_char[i] = count_char[i-1] * 2 + 1;
	}
}

/*
 * Get sequence of nth generation
 */
string get_sequence(int nth) {
	string &temp_sequence = cache_sequence[nth];

	if (temp_sequence.size() != 0) return temp_sequence;

	if (nth == 0) { temp_sequence = "FX"; }
	if (nth == 1) { temp_sequence = "FX+YF"; }
	for (int i = 2; i <= nth; ++i) {
		cache_sequence[i] = "FX-YF";
		for (int j = 1; j < i-1; ++j) {
			cache_sequence[i] = cache_sequence[j] + "-" + cache_sequence[i];
		}
		cache_sequence[i] = cache_sequence[i-1] + "+" + cache_sequence[i];
	}

	return temp_sequence;
}

void make_result(int nth) {
	while (len > 0) {
		string temp_sequence = get_sequence(nth);
		if (start_index + len - 1 >= temp_sequence.size()) {
			result_sequence += temp_sequence.substr(start_index-1);
		} else {
			result_sequence += temp_sequence.substr(start_index-1, len);
			cout << result_sequence << endl;
			return;
		}
		len -= (temp_sequence.size() - start_index + 1);
		if (len > 0) {
			if (nth == gen - 1) result_sequence += "+";
			else result_sequence += "-";
			--len;
			start_index = 1;
		}
		--nth;
	}
	cout << result_sequence << endl;
	return;
}

void solution() {
	int nth = gen - 1;

	while (start_index > count_char[nth]) {
		start_index -= count_char[nth];

		if (start_index == 1) {
			if (nth == gen - 1) result_sequence += "+";
			else result_sequence += "-";
			--len;
		} else {
			--start_index;
		}
		
		--nth;
	}

	make_result(nth);
}

int main() {
	cin >> num_tests;

	init_cache();
	calculate_count();
	while(--num_tests >= 0) {
		cin >> gen; cin >> start_index; cin >> len;
		result_sequence = "";
		solution();
	}
}
