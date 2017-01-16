
#include <iostream>
#include <algorithm>
#include <map>

// #1 - sort-based
bool is_permutation_v1(std::string str0, std::string str1) {

	std::string t0 = str0;
	std::string t1 = str1;

	std::sort(t0.begin(), t0.end());
	std::sort(t1.begin(), t1.end());

	for (int i = 0; i < t0.size(); i++) {

		if (t0[i] != t1[i])
			return false;

	}

	return true;
}

// #2 - hashmap-based
bool is_permutation_v2(std::string str0, std::string str1) {

	std::map<char, int> m;

	for (int i = 0; i < str0.size(); i++)
		m[str0[i]]++;

	for (int i = 0; i < str1.size(); i++)
		m[str1[i]]--;

	for (std::map<char, int>::iterator it = m.begin(); it != m.end(); it++)
		if (it->second != 0) return false;

	return true;
}

int main() {

	std::string s0 = "abcdefgh";
	std::string s1 = "agchdebf";
	std::string s2 = "agchrebf";

	std::cout << s0 << ", " << s1 << ", is permutation v1 = " << is_permutation_v1(s0, s1) << std::endl;
	std::cout << s0 << ", " << s2  << ", is permutation v1 = " << is_permutation_v1(s0, s2) << std::endl;

	std::cout << s0 << ", " << s1  << ", is permutation v2 = " << is_permutation_v2(s0, s1) << std::endl;
	std::cout << s0 << ", " << s2  << ", is permutation v2 = " << is_permutation_v2(s0, s2) << std::endl;

	return 0;
}

