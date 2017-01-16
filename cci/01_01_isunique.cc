
#include <iostream>
#include <algorithm>
#include <map>

// #1 - sort-based
bool is_unique_v1(std::string str) {

	std::string t = str;
	std::sort(t.begin(), t.end());

	for (int i = 1; i < t.size(); i++) {

		if (t[i - 1] == t[i])
			return false;

	}

	return true;
}

// #2 - hashmap-based
bool is_unique_v2(std::string str) {

	std::map<char, bool> m;

	for (int i = 0; i < str.size(); i++) {

		if (m.find(str[i]) != m.end())
			return false;
		else
			m[str[i]] = true;

	}

	return true;
}

int main() {

	std::string s0 = "abcdefgh";
	std::string s1 = "adbcdefgh";

	std::cout << s0 << ", is unique v1 = " << is_unique_v1(s0) << std::endl;
	std::cout << s1 << ", is unique v1 = " << is_unique_v1(s1) << std::endl;

	std::cout << s0 << ", is unique v2 = " << is_unique_v2(s0) << std::endl;
	std::cout << s1 << ", is unique v2 = " << is_unique_v2(s1) << std::endl;

	return 0;
}

