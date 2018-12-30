/*
12/19/2018: Problem 2: Add two numbers stored in linked lists

Utilities for linked list of integers.

Author: Eugene Ma
*/

#include "linked_list.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode* newListNode(int val, struct ListNode* next) {
    struct ListNode* n = malloc(sizeof(struct ListNode));
    n->val = val;
    n->next = next;

    return n;
}

struct ListNode* newListFromArray(int len, int *arr) {
    struct ListNode* n = NULL;
    for (int i = len - 1; i >= 0; --i) {
        n = newListNode(arr[i], n);
    }

    return n;
}

void freeList(struct ListNode* head) {
    while (head != NULL) {
        struct ListNode* prevHead = head;
        head = head->next;
        free(prevHead);
    }
}

void printList(struct ListNode* head) {
    if (head != NULL) {
        printf("%d", head->val);
        head = head->next;
    }
    while (head != NULL) {
        printf(" -> %d", head->val);
        head = head->next;
    }

    printf("\n");
}
