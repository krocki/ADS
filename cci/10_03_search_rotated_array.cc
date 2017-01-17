
#include <iostream>

void print_arr(int* arr, int len) {

	for (int i = 0; i < len; i++)
		std::cout << arr[i];

	std::cout << std::endl;

}

int binary_search(int* arr, int len, int k) {

	int i = len / 2;

	if (arr[i] == k) { return i; }

	if (len == 1) return -1;

	if (arr[i] < k) {
		return i + 1 + binary_search(arr + i + 1, len - i - 1, k);
	}

	if (arr[i] > k) {
		return binary_search(arr, len - i - 1, k);
	}

	return -1;
}

int binary_rotation_search(int* arr, int len) {

	int i = len / 2;

	if (len == 2 && arr[i] < arr[0]) { return i; }

	if (arr[0] < arr[i]) {
		return i + binary_rotation_search(arr + i, len - i);
	}

	if (arr[0] > arr[i]) {
		return binary_rotation_search(arr, len - i - 1);
	}

	return 0;
}

int main() {

	int s0[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	int s1[] = {5, 6, 7, 8, 9, 1, 2, 3, 4};
	int len = 9;

	int k = 6;

	int result = binary_search(s0, len, k);

	std::cout << "s0, find(" << k << ") = " << result << std::endl;

	int i = binary_rotation_search(s1, len);

	std::cout << "s1, find rotation pt = " << i << std::endl;

	if (s1[0] > k)
		result = i + binary_search(s1 + i, len - i, k);
	else
		result = binary_search(s1, i, k);

	std::cout << "s1, find(" << k << ") = " << result << std::endl;

	return 0;
}
