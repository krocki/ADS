/*
* @Author: krocki
* @Date:   2017-01-05 20:46:03
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-06 18:43:30
*/

#include <iostream>

/*
       			4(0)
			   /   \
			10(1)   3(2)
            /   \
	 	5(3)    1(4)

The numbers in bracket represent the indices in the array
representation of data. */

void heapify(int* arr, int idx, int n) {

	if (idx < n) {

		int left = 2 * idx + 1;
		int right = 2 * idx + 2;
		int largest = idx;

		if (left < n && arr[left] > arr[idx])
			largest = left;

		if (right < n && arr[right] > arr[largest])
			largest = right;

		if (idx != largest) {

			std::swap(arr[idx], arr[largest]);
			heapify(arr, largest, n);

		}
	}
}

int main() {

	int i, N = 6;
	int arr[] = { -5, 14, -99, 12, -1, 0};

	printf("Before: \n");
	for (i = 0; i < N; i++) printf("%d ", arr[i]);
	printf("\n");

	// build heap
	for (int i = N / 2 - 1; i >= 0; i--)
		heapify(arr, i, N);

	printf("After build heap: \n");
	for (i = 0; i < N; i++) printf("%d ", arr[i]);
	printf("\n");

	printf("Sorted: \n");

	// One by one extract an element from heap
	for (int i = N - 1; i >= 0; i--) {

		// Move current root to end
		std::swap(arr[i], arr[0]);

		// call max heapify on the reduced heap
		heapify(arr, 0, i);
	}

	for (i = 0; i < N; i++) printf("%d ", arr[i]);
	printf("\n");

}