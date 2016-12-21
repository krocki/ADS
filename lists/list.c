/*
* @Author: krocki
* @Date:   2016-12-20 12:07:44
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-20 19:10:45
*/

#include <stdio.h>
#include <stdlib.h>

#define TYPE int

typedef struct node {

	int val;
	struct node* next;

} node;

void append(node** head, TYPE elem) {

	if (*(head) == NULL) {

		(*head) = (node*) malloc(sizeof(node));
		(*head)->next = NULL;
		(*head)->val = elem;

	} else {

		append(&((*head)->next), elem);

	}
}

void prepend(node** head, TYPE elem) {

	node* new_head = (node*) malloc(sizeof(node));

	new_head->next = (*head);
	new_head->val = elem;

	(*head) = new_head;

}

//traverses the list and prints it
void traverse(node* head) {

	if (head != NULL) {

		printf("[%p] %d\n", head, head->val);
		traverse(head->next);

	}
}

//looks for element elem and returns its address otherwise NULL
node* find(node* head, TYPE elem) {

	if (head != NULL) {

		if (head->val == elem) return head;
		else return find(head->next, elem);

	} else return NULL;

}


//insert elem into list at index
void insert(node* head, node* address, TYPE elem) {

	if (head != NULL) {
		if (head == address) {

			//insert after this element
			node* new_node = (node*) malloc(sizeof(node));
			new_node->val = elem;
			new_node->next = head->next;
			head->next = new_node;

		} else insert(head->next, address, elem);
	}
}

//TODO: delete elem, delete list

int main() {

	node* head = NULL;

	append(&head, 0);
	append(&head, 1);
	append(&head, 2);
	append(&head, 3);

	traverse(head);

	printf("Find 1: %p\n", find(head, 1));
	printf("Find 2: %p\n", find(head, 2));
	printf("Find 4: %p\n", find(head, 4));

	prepend(&head, 4);

	traverse(head);
	printf("Find 4: %p\n", find(head, 4));

	//insert '5' after '2'
	insert(head, find(head, 2), 5);
	traverse(head);


}