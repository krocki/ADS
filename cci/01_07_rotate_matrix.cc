/*
@Author: krocki
@Date:   2017-01-12
*/

// given an image N x N, rotate 90 degrees, can you do it in place? pixel = 4 B


// a b c d      m i e a
// e f g h  ->  n j f b
// i j k l  ->  o k g c
// m n o p      p l h d

// a b c d      a e i m         m i e a
// e f g h  T   b f j n flip H  n j f b
// i j k l  ->  c g k o ->  --> o k g c
// m n o p      d h l p         p l h d

// in place -> swap a,m, swap a, p, swap a, d
// repeat for every element

#include <stdlib.h>
#include <iostream>

void print_array(int arr[][4], int n, int k) {

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < k; j++)
			printf("%4d", arr[i][j]);

		printf("\n");
	}

}

void rotate_array(int arr[][4], int n, int k) {

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

	printf("\n");
	print_array(arr, 4, 4);

}

int main() {

	int arr[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};

	print_array(arr, 4, 4);
	rotate_array(arr, 4, 4);

	return 0;

}
