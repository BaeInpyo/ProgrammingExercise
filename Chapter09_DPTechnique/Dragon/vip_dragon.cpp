#include <iostream>

#define N 50

using namespace std;

typedef unsigned long long int l_int;

int num_tests;
int in_gen;
l_int in_start;
int in_len;

l_int count_char[N+1];
string result_seq = "";

void init_cache() {
	for (int i = 0; i <= N; ++i) {
		count_char[i] = 0;
	}
}

/*
 * Calculate the number of characters in nth sequence
 */
void calculate_count() {
	count_char[0] = 5;
	count_char[1] = 5;
	for (int i = 2; i <= N; ++i) {
		count_char[i] = count_char[i-1] * 2 + 1;
	}
}

void print_seq(int nth, l_int start, int len) {
	if (nth <= 1) {
		string temp_seq;
		if (nth == 0) temp_seq = "FX-YF";
		else temp_seq = "FX+YF";
		result_seq += temp_seq.substr(start-1, len);
		return;
	}

	int ancestor = nth - 1;
	while (start > count_char[ancestor]) {
		start -= count_char[ancestor];
		if (start == 1) {
			if (ancestor == nth - 1) result_seq += "+";
			else result_seq += "-";
			--len;
		} else {
			--start;
		}
		--ancestor;
	}

	while (len > 0) {
		l_int subseq_len = count_char[ancestor] - start + 1;
		if (len < subseq_len) subseq_len = len;
		print_seq(ancestor, start, subseq_len);
		len -= subseq_len;
		if (len > 0) {
			if (ancestor == nth - 1) result_seq += "+";
			else result_seq += "-";
			--len;
			--ancestor;
			start = 1;
		}
	}
}

void solution() {
	if (in_gen == 0) {
		string temp_seq = "FX";
		cout << temp_seq.substr(in_start-1, in_len);
		return;
	}

	print_seq(in_gen, in_start, in_len);
}

int main() {
	cin >> num_tests;

	init_cache();
	calculate_count();
	while(--num_tests >= 0) {
		cin >> in_gen; cin >> in_start; cin >> in_len;
		result_seq = "";
		solution();
		cout << result_seq << endl;
	}
}
