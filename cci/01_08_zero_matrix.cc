/*
@Author: krocki
@Date:   2017-01-12
*/

// if element of a MxN matrix is 0, whole row and column is zeros

#include <stdlib.h>
#include <iostream>
#include <vector>

void print_array(int arr[][5], int n, int k) {

	for (int i = 0; i < n; i++) {

		for (int j = 0; j < k; j++)
			printf("%4d", arr[i][j]);

		printf("\n");
	}

}

// a b c d      a 0 0 m
// e f g h  T   e 0 0 n
// i j 0 l  ->  0 0 0 0
// m 0 o p      0 0 0 0

// solution with rotating layers
void zero_matrix(int arr[][5], int n, int k) {

	std::vector<int> zero_rows;
	std::vector<int> zero_cols;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < k; j++)
			if (arr[i][j] == 0) {
				zero_rows.push_back(i);
				zero_cols.push_back(j);
			}

	for (int i = 0; i < zero_rows.size(); i++)
		for (int j = 0; j < k; j++)
			arr[zero_rows[i]][j] = 0;

	for (int i = 0; i < zero_cols.size(); i++)
		for (int j = 0; j < n; j++)
			arr[j][zero_cols[i]] = 0;

}

int main() {

	int arr[5][5] = {{1, 2, 0, 4, 5}, {6, 7, 8, 9, 10}, {11, 1, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 0, 25}};

	print_array(arr, 5, 5);
	printf("\n");
	zero_matrix(arr, 5, 5);
	print_array(arr, 5, 5);
	printf("\n");
	return 0;

}
