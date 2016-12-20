/*
* @Author: krocki
* @Date:   2016-12-20 12:07:44
* @Last Modified by:   krocki
* @Last Modified time: 2016-12-20 12:19:04
*/

#include <stdio.h>
#include <stdlib.h>

#define TYPE int

typedef struct node {

	int val; 
	struct node* next;

} node;

void append(node* head, TYPE elem) {

	if (head == NULL) {

		head = (node*) malloc(sizeof(node));
		head->next = NULL;
		head->val = elem;

	} else {

		append(head->next, elem);

	}
}

//traverses the list and prints it
void traverse(node* head);
//looks for element elem and returns its index otherwise -1
int find(node* head, TYPE elem);
//deletes element at index
int delete(node* head, int index);

//insert elem into list at index
void insert(node* head, int index, TYPE elem);

int main() {

    node* head = NULL;

    append(head, 0);

}