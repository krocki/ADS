#include <iostream>
#include <algorithm>
#include <string>

int main() {

	std::string s =  "the sky is blue blue is the sky";

	std::cout << s << std::endl;

	std::reverse(begin(s), end(s));


	int j = 0;

	for (int i = 0; i < s.size(); i++) {

		if (s[i] == ' ' || i == s.size() - 1) {

			if (i == (s.size() - 1)) i++;

			std::reverse(s.begin() + j, s.begin() + i);
			j = i + 1;


		}

	}

	std::cout << s << std::endl;

}
