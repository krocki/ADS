/*
* @Author: krocki
* @Date:   2016-12-19 10:16:33
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-17 21:18:58
*/

#include <stdio.h>

// arr = [3, 4, 5, 1, 2, 4]
#define SWAP(a, b) do { a ^= b; b ^= a; a ^= b; } while(0)

int partition(int* arr, int low, int high) {

	int pivot = arr[low];

	printf("pivot = %d\n", pivot);

	int i = low + 1;
	int j = high;

	while (i < j) {

		printf("i = %d, j = %d, a[i] = %d, a[j] = %d\n", i, j, arr[i], arr[j]);
		while (arr[i] <= pivot) i++;
		while (arr[j] > pivot) j--;

		if (i < j) SWAP(arr[i], arr[j]);

	}

	printf("i = %d, j = %d, a[i] = %d, a[j] = %d\n", i, j, arr[i], arr[j]);

	arr[0] = arr[j];
	arr[j] = pivot;

	return j;

}

void quicksort(int* arr, int low, int high) {

	if (low < high) {

		int i = partition(arr, low, high);
		printf("low = %d, high = %d, i = %d\n", low, high, i);

		// TODO:
	}
}

void print_array(int* arr, int n) {

	for (int i = 0; i < n; i++)
		printf("%3d", arr[i]);

	printf("\n");

}

int main() {

	int n = 10;
	int arr[10] = { 4, 1, 5, 10, 2, 6, 3, 7, 8, 9};

	print_array(arr, n);
	quicksort(arr, 0, n - 1);
	print_array(arr, n);
}

