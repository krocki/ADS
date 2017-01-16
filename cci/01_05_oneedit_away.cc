/*
@Author: krocki
@Date:   2017-01-12
*/

#include <iostream>
#include <algorithm>
#include <map>

// one edit away
// there are 3 types of edits: insert, remove, replace
// given 2 string, check if they are 1 edit away (or 0 edits)
bool is_one_edit_away(std::string a, std::string b) {

	if (a.size() < b.size()) return is_one_edit_away(b, a);


	// assume that a is longer or equal
	if (a.size() > b.size() + 1) return false;

	//forward pass
	int count = 0;

	// count matching characters
	for (int i = 0; i < b.size(); i++) {

		if (a[i] == b[i]) count++;
		else break;

	}

	//backward pass
	int k = a.size() - 1;
	for (int i = b.size() - 1; i >= 0; i--) {

		if (a[k] == b[i]) { count++; k--; }
		else break;

	}

	// if all characters or all - 1 in a match
	// those in b, return true
	if (count + 1 >= a.size()) return true;
	else return false;

}

int main() {

	std::string s0 = "pale";
	std::string s1 = "ple";
	std::string s3 = "pales";
	std::string s4 = "bale";
	std::string s5 = "bake";

	std::cout << s0 << ", " << s1 << ", is 1 edit away = " << is_one_edit_away(s0, s1) << std::endl;
	std::cout << s3 << ", " << s0 << ", is 1 edit away = " << is_one_edit_away(s3, s0) << std::endl;
	std::cout << s0 << ", " << s4 << ", is 1 edit away = " << is_one_edit_away(s0, s4) << std::endl;
	std::cout << s0 << ", " << s5 << ", is 1 edit away = " << is_one_edit_away(s0, s5) << std::endl;

	return 0;
}
