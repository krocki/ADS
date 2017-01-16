/*
* @Author: krocki
* @Date:   2017-01-14 21:21:17
* @Last Modified by:   krocki
* @Last Modified time: 2017-01-14 21:30:12
*/

/*
	remove middle node in a list without access to head
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

void traverse(node* head) {

	if (head != NULL) {

		printf("%d ", head->val);
		if (head->next != NULL) traverse(head->next);
		else printf("\n");
	}

}

node* advance(node* head, int k) {

	if (head != NULL) {
		if (k == 0) return head;
		else if (head->next != NULL)
			return advance(head->next, k - 1);
	}

	return NULL;

}

/*
	['a', 'b', 'c', 'd', 'e']

	remove 'c' -> 1. 'c'.val = 'd'.val, 2. free(c->next), 'c'->next = 'd'->next
*/

void remove_middle(node* ptr) {

	// assume middle node, no need to check for NULLs
	ptr->val = ptr->next->val;
	free(ptr->next);
	ptr->next = ptr->next->next;


}
int main() {

	node* head = NULL;

	head = append(head, 1);
	head = append(head, 2);
	head = append(head, 3);
	head = append(head, 4);
	head = append(head, 5);

	traverse(head);

	node* ptr = advance(head, 2);

	remove_middle(ptr);

	traverse(head);

	return 0;

}
