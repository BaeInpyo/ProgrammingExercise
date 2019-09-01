#include <iostream>
#include <utility>
#include <unordered_map>

#define MOD 1000000007

using namespace std;

using l_int = unsigned long long;

int shift_amount = 4;
int num_tests;
int price_len;
int price[15];
int candy_count;

unordered_map<l_int, int> cache; // comb, remainder : count

l_int convert_single_digit(int digit) {
	l_int res;
	res = 1ULL << shift_amount * digit;
	return res;
}

l_int convert_every_digit() {
	l_int num_digit[10];
	l_int res = 0;

	for (int i = 0; i < 10; ++i) { num_digit[i] = 0; }
	for (int i = 0; i < price_len; ++i) { ++num_digit[price[i]]; }
	for (int i = 0; i < 10; ++i) {
		res += num_digit[i] << shift_amount * i;
	}

	return res;
}

bool is_valid_digit(l_int comb, int digit) {
	l_int pos;
	pos = 15ULL << shift_amount * digit;
	pos &= comb;

	return (pos > 0);
}

int calculate_remainder(int digit, int cipher) {
	int remainder = digit % candy_count;
	for (int i = 1; i < cipher; ++i) {
		remainder *= 10;
		remainder %= candy_count;
	}

	return remainder;
}

int get_remainder_count(l_int comb, int remainder, int comb_len) {
	if (comb_len == 0) {
		if (remainder == 0) return 1;
		else return 0;
	}

	l_int key = (comb << 5) + remainder;
	auto res = cache.find(key);
	if (res != cache.end()) return res->second;

	cache[key] = 0;
	
	for (int candidate = 9; candidate >= 0; --candidate) {
		if (is_valid_digit(comb, candidate)) {
			int sub_comb = comb - convert_single_digit(candidate);
			int sub_remainder = remainder - calculate_remainder(candidate, comb_len);
			if (sub_remainder < 0) sub_remainder += candy_count;
			cache[key] += get_remainder_count(sub_comb, sub_remainder, comb_len - 1);
		}
	}

	return cache[key];
}

void solution() {
	int total_count = 0;
	l_int comb = convert_every_digit();
	int remainder = 0;
	for (int i = 0; i < price_len; ++i) {
		int msb = price[i];
		if (i > 0) {
			remainder = (remainder + calculate_remainder(price[i-1], price_len-(i-1))) % candy_count;
			comb -= convert_single_digit(price[i-1]);
		}
		for (int candidate = msb - 1; candidate >= 0; --candidate) {
			if (is_valid_digit(comb, candidate)) {
				int sub_comb = comb - convert_single_digit(candidate);
				int sub_remainder = (remainder + calculate_remainder(candidate, price_len-i)) % candy_count;
				int required_remainder = (candy_count - sub_remainder) % candy_count;
				total_count = (total_count + get_remainder_count(sub_comb, required_remainder, price_len-i-1)) % MOD;
			}
		}
	}

	cout << total_count << endl;
}

void change_string_to_num_array(string price_in_str) {
	int i = 0;
	price_len = price_in_str.size();
	for (; i < price_len; ++i) {
		price[i] = price_in_str[i]-48;
	}

	for (; i < 15; ++i) {
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

		cache.clear();
	}
}
