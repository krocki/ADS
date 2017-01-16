/*
@Author: krocki
@Date:   2017-01-12
*/

// given an image N x N, rotate 90 degrees, can you do it in place? pixel = 4 B


// a b c d      m i e a
// e f g h  ->  n j f b
// i j k l  ->  o k g c
// m n o p      p l h d

#include <stdlib.h>
#include <iostream>

void print_array(int arr[][5], int n, int k) {

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < k; j++)
			printf("%4d", arr[i][j]);

		printf("\n");
	}

}

// a b c d      a e i m         m i e a
// e f g h  T   b f j n flip H  n j f b
// i j k l  ->  c g k o ->  --> o k g c
// m n o p      d h l p         p l h d

void rotate_array(int arr[][5], int n, int k) {

	//transpose
	for (int i = 0; i < n; i++) {

		for (int j = i + 1; j < n; j++)

			std::swap(arr[i][j], arr[j][i]);

	}

	// reverse each row
	for (int i = 0; i < n; i++) {

		for (int j = 0; j < n / 2; j++)

			std::swap(arr[i][j], arr[i][n - j - 1]);

	}

}

// solution with rotating layers
void rotate_array_v2(int arr[][5], int n, int k) {

	for (int i = 0; i < n / 2; i++) {

		for (int j = 0; j < n / 2 + 1; j++) {

			int temp = arr[i][j];
			arr[i][j] = arr[n - 1 - j][i];
			arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j];
			arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i];
			arr[j][n - 1 - i] = temp;
		}
	}


}

int main() {

	int arr[5][5] = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}};

	print_array(arr, 5, 5);
	printf("\n");
	rotate_array_v2(arr, 5, 5);
	print_array(arr, 5, 5);
	printf("\n");
	return 0;

}
