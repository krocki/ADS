/*
* @Author: krocki
* @Date:   2016-12-29 12:50:12
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-29 13:18:30
*/

#include <stdio.h>

void swapbits(int* x, int i, int j) {

	if (((*x >> i) & 1) != ((*x >> j) & 1)) {

		//flip bits at positions i and j
		int bitmask = (1 << i) | (1 << j);
		*x ^= bitmask;
	}

}

int main() {

	int x = 0b00000000000000000000000000000001;

	printf("before swap (should be 1) = %d\n", x);

	int i = 0;
	int j = 4;
	swapbits(&x, i, j);

	printf("after swap (should be 16) = %d\n", x);

}