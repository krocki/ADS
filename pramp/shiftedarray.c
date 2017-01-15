/*
* @Author: krocki
* @Date:   2017-01-14 16:58:58
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-14 19:12:34
*/

#include <stdio.h>

/*
Shifted Array Search

1. Find a given number num in a sorted array arr:
arr = [2, 4, 5, 9, 12, 17]

2. If the sorted array arr is shifted left by an
unknown offset and you don't have a pre-shifted
copy of it, how would you modify your method to
find a number in the shifted array? shiftArr = [9,
12, 17, 2, 4, 5]

Explain and code an efficient solution and analyze
its runtime complexity if num doesn't exist in the
array, return -1
*/

int binary_search(int* arr, int n, int num) {

	/* pivot index */
	int i = n / 2;

	/* pivot == num, return */
	if (arr[i] == num) return i;

	/* i == 0, not found */
	if (i == 0) return -1;

	if (arr[i] < num) {

		/* pivot < num */
		int idx = binary_search(arr + i + 1, n - i, num);
		if (idx != -1) return i + idx + 1; else return -1;
	}

	if (arr[i] > num) {

		/* pivot > num */
		return binary_search(arr, i, num);

	}

	/* not found */
	return -1;
}

int find_rotation_point(int* arr, int n) {

	int i = n / 2;

	if (arr[0] < arr[i]) {

		return i + find_rotation_point(arr + i, n - i);

	}

	if (arr[0] > arr[i]) {

		return find_rotation_point(arr, n - i);

	}

	return 1;
}

int main() {

	int arr0[] = {2, 4, 5, 9, 12, 17};
	int n0 = 6;

	int arr1[] = {2, 4, 5, 9, 12, 17, 19};
	int n1 = 7;

	printf("%d\n", binary_search(arr0, n0, 0));
	printf("%d\n", binary_search(arr1, n1, 19));

	int arr2[] = {19, 2, 4, 5, 9, 12, 17};

	int k = find_rotation_point(arr2, n1);

	printf("%d\n", k);

	int idx = binary_search(arr2 + k, n1 - k, 2);

	if (idx != -1)
		printf("%d\n", k + idx);
	else
		printf("%d\n", binary_search(arr2, k - 1, 2));

	return 0;
}

