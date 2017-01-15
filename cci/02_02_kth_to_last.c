/*
* @Author: krocki
* @Date:   2017-01-14 20:49:33
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-14 21:20:12
*/

/*
	find kth to last element in a list

*/

#include <stdio.h>
#include <stdlib.h>

typedef struct node {

	struct node* next;
	int val;

} node;

node* append(node* head, int val) {

	if (head == NULL) {

		head = (node*)malloc(sizeof(node));
		head->next = NULL;
		head->val = val;

	} else

		head->next = append(head->next, val);

	return head;

}
// 1 - figure out length n, and retrieve (n-k)th element
// - use recursion:


int length(node* head) {


	if (head == NULL) return 0;
	else return 1 + length(head->next);
}

int get_elem(node* head, int idx) {

	if (head != NULL) {
		if (idx == 0) return head->val;
		else if (head->next != NULL)
			return get_elem(head->next, idx - 1);
	}

	return -1;

}

// 2 - run 2 pointers, delay the 2nd pointer by k

node* advance(node* head, int k) {

	if (head != NULL) {
		if (k == 0) return head;
		else if (head->next != NULL)
			return advance(head->next, k - 1);
	}

	return NULL;

}

int get_elem_2ptrs(node* head, int k) {

	node* ptr1 = advance(head, k + 1);
	node* ptr2 = head;

	while (ptr1) {

		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}

	return ptr2->val;

}

int main() {


	node* head = NULL;

	head = append(head, 1);
	head = append(head, 2);
	head = append(head, 3);
	head = append(head, 4);
	head = append(head, 5);

	int n = length(head);
	int k = 2;

	printf("length = %d\n", n);

	int elem = get_elem(head, n - k - 1);
	printf("1. elem(-%d) = %d\n", k, elem);

	elem = get_elem_2ptrs(head, k);
	printf("1. elem(-%d) = %d\n", k, elem);
}
