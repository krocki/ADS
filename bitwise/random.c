/*
* @Author: krocki
* @Date:   2016-12-31 11:24:19
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-31 11:59:11
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
// generate a random int from range [a, b] given [0,1]

int roundup2 (int v) {

	v--;
	v |= v >> 1;
	v |= v >> 2;
	v |= v >> 4;
	v |= v >> 8;
	v |= v >> 16;
	v++;

	return v;
}

int rand_0_1() {

	return rand() % 2;
}

int rand_range(int a, int b) {

	int range = b - a;
	//Round up to the next highest power of 2
	int next_pow2 = roundup2(range);

	int i = 0;
	int number = 0;

	for (i = 0; i < (int)log2(next_pow2); i++) {

		number += rand_0_1() * (1 << i);

	}

	if (number < range) return a + number;
	else return rand_range(a, b);

}

int main() {

	struct timespec ts;
	clock_gettime(CLOCK_MONOTONIC, &ts);

	srand((time_t)ts.tv_nsec);

	printf ("%d\n", rand_range(0, 30));

}