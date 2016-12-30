/*
* @Author: krocki
* @Date:   2016-12-29 12:31:11
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-30 09:22:29
*/

#include <stdio.h>

// this one has complexity O(n)
int popcount1(int x) {

	int count = 0;

	while (x) {

		count += x & 1; //adds one if lowest bit set
		x >>= 1; // shift
	}

	return count;
}

// this one has complexity O(k)
// where k is the number of bits set to 1
int popcount2(int x) {

	int count = 0;

	while (x) {

		count++;
		x &= (x - 1); // removes highest 'on' bit
	}

	return count;
}

// O(logn)
int popcount3(int y) {

	int x = y;

	// 0x55555555 = 0b01010101010101010101010101010101
	x = (x & 0x55555555) + ((x >> 1) & 0x55555555);
	// 0x33333333 = 0b00110011001100110011001100110011
	x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
	// 0x0F0F0F0F = 0b00001111000011110000111100001111
	x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F);
	// 0x00FF00FF = 0b00000000111111110000000011111111
	x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF);
	// 0x0000FFFF = 0b00000000000000001111111111111111
	x = (x & 0x0000FFFF) + ((x >> 16) & 0x00FFFFFF);

	return x;
}
int main() {

	//11 bits set to 1
	int x = 0b01110000000000000000000011111111;

	printf("%d\n", popcount1(x));
	printf("%d\n", popcount2(x));
	printf("%d\n", popcount3(x));
}