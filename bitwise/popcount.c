/*
* @Author: krocki
* @Date:   2016-12-29 12:31:11
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-29 12:38:29
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

int main() {

	//11 bits set to 1
	int x = 0b01110000000000000000000011111111;

	printf("%d\n", popcount1(x));
	printf("%d\n", popcount2(x));

}