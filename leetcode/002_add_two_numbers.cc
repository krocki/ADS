/**

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        return add(l1, l2);
    }

    ListNode* add(ListNode* a, ListNode* b, int carry = 0) {

        ListNode* digit = NULL;

        if (a != NULL || b != NULL || carry > 0) {

            digit = (ListNode*)malloc(sizeof(ListNode));

            int sum = carry;

            if (a) sum += a->val;
            if (b) sum += b->val;

            int carry = sum / 10;
            int remainder = sum % 10;

            digit->val = remainder;

            if (a && b) digit->next = add(a->next, b->next, carry);
            else if (a) digit->next = add(a->next, NULL, carry);
            else if (b) digit->next = add(b->next, NULL, carry);
            else digit->next = add(NULL, NULL, carry);

        }

        return digit;
    }
};

// or iterative

/*class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        return add(l1, l2);
    }

    ListNode* add(ListNode* a, ListNode* b) {

        ListNode* digit = NULL;
        ListNode* head = NULL;
        ListNode* prev = NULL;

        int sum, remainder, carry;

        carry = 0;

        while (a != NULL || b != NULL || carry) {

            prev = digit;
            digit = (ListNode*)malloc(sizeof(ListNode));
            if (head == NULL) head = digit;
            if (prev != NULL) prev->next = digit;

            sum = carry;

            if (a) sum += a->val;
            if (b) sum += b->val;

            carry = sum / 10;
            remainder = sum % 10;

            digit->val = remainder;

            if (a) a = a->next;
            if (b) b = b->next;

        }

        return head;
    }
};
*/
