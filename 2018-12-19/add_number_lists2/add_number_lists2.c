/*
12/19/2018: Problem 2: Add two numbers stored in linked lists

Main solution.

Author: Eugene Ma
*/

#include "linked_list.h"
#include <string.h>

struct ListNode* addNumsInLists(struct ListNode* h1, struct ListNode* h2, int carry) {
    if (h1 != NULL) {
        if (h2 != NULL) {
            int sum = h1->val + h2->val + carry;

            return newListNode(sum % 10, addNumsInLists(h1->next, h2->next, sum / 10));
        }
        else {
            int sum = h1->val + carry;

            return newListNode(sum % 10, addNumsInLists(h1->next, NULL, sum / 10));
        }
    }
    else {
        if (h2 != NULL) {
            int sum = h2->val + carry;

            return newListNode(sum % 10, addNumsInLists(NULL, h2->next, sum / 10));
        }
        else {
            if (carry > 0) {
                return newListNode(carry, NULL);
            }
            else {
                return NULL;
            }
        }
    }
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    return addNumsInLists(l1, l2, 0);
}

int main() {
    // The number 243
    int a_data[] = {3, 4, 2};
    // The number 95948
    int b_data[] = {8, 4, 9, 5, 9};

    struct ListNode* a = newListFromArray(sizeof a_data / sizeof a_data[0], a_data);
    struct ListNode* b = newListFromArray(sizeof b_data / sizeof b_data[0], b_data);
    struct ListNode* sum = addTwoNumbers(a, b);

    printList(sum);

    freeList(sum);
    freeList(a);
    freeList(b);

    return 0;
}
