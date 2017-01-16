/*
@Author: krocki
@Date:   2017-01-12
*/

// check if a list is a palindrome

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

int pop_last(node* head) {

	node* prev = head;

	while (head->next != NULL) {

		prev = head;
		head = head->next;
	}

	int val = head->val;
	prev->next = NULL;

	return head->val;

}

bool is_palindrome(node* head) {

	if (head == NULL) return true;

	else {

		int head_val = head->val;
		int last_val = pop_last(head);

		if (head_val == last_val)
			return is_palindrome(head->next);


	}

}

int main() {


	node* head = NULL;

	head = append(head, 1);
	head = append(head, 2);
	head = append(head, 3);
	head = append(head, 4);
	head = append(head, 3);
	head = append(head, 2);
	head = append(head, 1);

	printf("ispalindrome = %d\n", is_palindrome(head));
}
