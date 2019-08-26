#include <iostream>

#define MOD 1000000007

using namespace std;

int num_tests;
int price_len;
int price[14];
int candy_count;

void solution() {
	
}

void change_string_to_num_array(string price_in_str) {
	int i = 0;
	price_len = price_in_str.size();
	for (; i < price_in_str.size(); ++i) {
		price[i] = price_in_str[i];
	}

	for (; i < 14; ++i) {
		price[i] = -1;
	}

	return;
}

int main() {
	cin.sync_with_stdio(false);
	cin >> num_tests;

	while (--num_tests >= 0) {
		string price_in_str; cin >> price_in_str;
		cin >> candy_count;

		change_string_to_num_array(price_in_str);

		solution();
	}
}
