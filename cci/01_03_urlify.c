/*
* @Author: krocki
* @Date:   2017-01-15 15:09:06
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-15 15:24:50
*/

#include <stdio.h>

int count_spaces(char* arr, int len) {

	int i;
	int counter = 0;

	for (i = 0; i < len; i++)
		if (arr[i] == ' ') counter++;

	return counter;

}

void urlify(char* arr, int len) {

	int num_spaces = count_spaces(arr, len);
	int extended_length = len + num_spaces * 2;

	int i = extended_length - 1;
	int k;

	for (k = len - 1; k >= 0; k--) {

		if (arr[k] != ' ') {

			arr[i] = arr[k];
			--i;

		} else {

			arr[i] = '0';
			arr[i - 1] = '2';
			arr[i - 2] = '%';
			i -= 3;

		}

	}

}

int main() {

	char array[] = "abc string zyx    ";
	int len = 14;

	urlify(array, len);

	int i;

	printf("%s\n", array);
	return 0;
}
