/*
* @Author: krocki
* @Date:   2017-01-14 12:00:45
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-14 12:07:34
*/

#include <stdio.h>

int main() {

	int M = 0b00000000000000000000010000000000;
	int N = 0b00000000000000000000000000010011;
	int i = 2;
	int j = 6;

	int ones = ~0;

	int leftmask = ones << j;
	int rightmask = ones >> i;

	M = (leftmask | rightmask) & M;
	M = (N << i) | M;

	printf("%d\n", M);
	//1100 = 0b00000000000000000000010001001100
}
