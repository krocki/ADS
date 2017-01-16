/*
@Author: krocki
@Date:   2017-01-12
*/

// "aabcccccaaa" -> "a2b1c5a3"

#include <iostream>

std::string compress(std::string original) {

	std::string compressed = "";

	int counter = 1;
	int i;

	for (i = 1; i < original.size(); i++) {


		if (original[i - 1] != original[i]) {
			compressed += original[i - 1];
			compressed += std::to_string(counter);
			counter = 1;
		} else counter++;
	}

	compressed += original.back();
	compressed += std::to_string(counter);

	if (compressed.size() > original.size())
		return original;
	else
		return compressed;

}

int main() {

	std::string str = "aabcccccaaa";
	std::string str2 = "aabc";

	printf("%s -> %s\n", str.c_str(), compress(str).c_str());
	printf("%s -> %s\n", str2.c_str(), compress(str2).c_str());
}
