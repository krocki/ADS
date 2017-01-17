/*
* @Author: krocki
* @Date:   2017-01-16 20:00:45
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-16 20:00:45
*/

#include <stdio.h>
#include <string>

double binary_to_double(std::string s) {

	double x = 0.0;
	double y = 1;
	for (int i = 2; i < s.size(); i++) {
		y /= 2;
		if (s[i] == '1') x += y;

	}


	return x;
}

std::string double_to_binary(double x) {

	std::string str = "0.";

	while (x > 0) {

		x *= 2;

		if (x >= 1) {
			str += "1";
			x -= 1;
		} else
			str += "0";

		if (str.size() > 32) {
			return "ERROR (" + std::to_string(binary_to_double(str)) + " " + std::to_string(x) + ")";
		}
	}

	return str;

}

int main() {

	double x = 0.750001;

	std::string str = double_to_binary(x);

	printf("%f = %s\n", x, str.c_str());

}
