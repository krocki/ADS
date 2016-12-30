/*
* @Author: krocki
* @Date:   2016-12-29 12:39:17
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-29 12:49:43
*/

#include <stdio.h>

// complexity O(n)
int parity(int x) {

	int parity = 0;

	while (x) {

		parity ^= 1; //flips if bit is set
		x &= (x - 1);
	}

	//returns 0 if number of 1s is even
	return parity;
}

// complexity O(logn)
int parity2(int x) {

	// idea: XOR of 2 1s gives 0, reduce int to 1 number

	x ^= (x >> 16);
	x ^= (x >> 8);
	x ^= (x >> 4);
	x ^= (x >> 2);
	x ^= (x >> 1);

	return x & 1;

}

/* TODO: lookup table version,
   Can check 2, 4, 8, 16, ... etc bits in parallel */

int main() {

	//11 bits set to 1
	int x = 0b01110000000000000000000011111111;
	//12 bits set to 1
	int y = 0b01110000000001000000000011111111;

	printf("parity(x) = %d, parity(y) = %d\n",
	       parity(x), parity(y));

	printf("parity2(x) = %d, parity2(y) = %d\n",
	       parity2(x), parity2(y));

}