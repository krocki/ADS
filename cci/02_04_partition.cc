/*
@Author: krocki
@Date:   2017-01-12
*/

/*partition a linked list around x value, like quicksort*/


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

void concat(node* head, node *other) {

	while (head->next != NULL)
		head = head->next;

	head->next = other;

}

void traverse(node* head) {

	if (head != NULL) {

		printf("%d ", head->val);
		if (head->next != NULL) traverse(head->next);
		else printf("\n");
	}

}

node* partition(node* head, int x) {

	/* out of place */

	node* low = NULL;
	node* high = NULL;

	while (head != NULL) {

		if (head->val < x) low = append(low, head->val);
		else high = append(high, head->val);

		head = head->next;

	}

	concat(low, high);

	return low;

}

int main() {


	node* head = NULL;

	head = append(head, 5);
	head = append(head, -1);
	head = append(head, 4);
	head = append(head, 9);
	head = append(head, 8);
	head = append(head, 2);
	head = append(head, -4);
	head = append(head, 0);
	head = append(head, 7);
	head = append(head, 6);
	head = append(head, -3);

	traverse(head);

	node* partitioned = partition(head, 4);

	traverse(partitioned);

}
