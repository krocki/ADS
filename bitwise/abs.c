/*
* @Author: krocki
* @Date:   2016-12-30 22:25:25
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-31 12:22:16
*/

#include <stdio.h>

// http://stackoverflow.com/questions/21923791/how-to-get-absolute-value-of-a-number-in-java-using-bit-manipulation

int absolute(int n) {

	int const mask = n >> (31);
	return ((n ^ mask) - mask);

	// for positive, do nothing
	// x =        0b00000000000000000000000000000100
	// mask =     0b00000000000000000000000000000000
	// x ^ mask = 0b00000000000000000000000000000100
	// - mask =   0b00000000000000000000000000000100

	// for negative, toggle all bits and add 1
	// y =        0b11111111111111111111111111111100
	// mask =     0b11111111111111111111111111111111 = -1
	// y ^ mask = 0b00000000000000000000000000000011 = 3
	// - mask =   0b00000000000000000000000000000100 = + 1
}

int main() {

	int x = 0b00000000000000000000000000000100;
	int y = 0b11111111111111111111111111111100;

	printf("x = %d, y = %d abs(x) = %d, abs(y) = %d\n", x, y, absolute(x), absolute(y));

}