/*
12/19/2018: Problem 2: Add two numbers stored in linked lists

Utilities for linked list of integers.

Author: Eugene Ma
*/

#ifndef LINKED_LIST_H
#define LINKED_LIST_H

// Definition for singly-linked list (from LeetCode):
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* newListNode(int val, struct ListNode* next);
struct ListNode* newListFromArray(int len, int *arr);
void freeList(struct ListNode* head);

void printList(struct ListNode* head);

#endif
