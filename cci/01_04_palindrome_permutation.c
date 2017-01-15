/*
* @Author: krocki
* @Date:   2017-01-15 15:24:45
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-15 15:42:24
*/

#include <stdio.h>

int is_palindrome_permutation(char* arr, int len) {

	int N = 256;
	int lookup_table[N];
	int i;
	int allowable_non_pairs;

	if (len % 2 == 1) allowable_non_pairs = 1;
	else allowable_non_pairs = 0;

	for (i = 0; i < N; i++)
		lookup_table[i] = 0;

	for (i = 0; i < len; i++)
		lookup_table[(int)arr[i]]++;

	for (i = 0; i < N; i++) {

		if (lookup_table[i] % 2 != 0)
			allowable_non_pairs--;

		if (allowable_non_pairs < 0)
			return 0;
	}

	return 1;
}

int main() {

	char array[] = "ccaac";
	int len = 5;

	printf("%s -> is palindrome permutation %d\n", array, is_palindrome_permutation(array, len));

	return 0;
}
