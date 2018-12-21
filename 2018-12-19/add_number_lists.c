#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int val;
    struct Node *next;
} Node;

Node *new_node(int val) {
    Node *new = malloc(sizeof(*new));
    new->next = NULL;
    new->val = val;
    return new;
}

Node *list(int len, int *arr) {
    int i;
    Node dummy;

    if (len > 0) {
        Node *current = new_node(arr[len-1]);
        dummy.next = current;
        
        for (i = len - 2; i >= 0; i--) {
            current->next = new_node(arr[i]);
            current = current->next;
        }
    }
    
    return dummy.next;
}

void add_r(Node *a, Node *b, Node *sum) {
    if (a) { sum->val += a->val; }
    if (b) { sum->val += b->val; }

    if (sum->val > 9) {
        sum->val -= 10;
        sum->next = new_node(1);
        sum = sum->next;
    }
    else if ((a && a->next) || (b && b->next)) {    
        sum->next = new_node(0);
        sum = sum->next;
    }

    if (a || b) {
        add_r(a ? a->next : NULL, b ? b->next : NULL, sum);
    }
}

Node *add(Node *a, Node *b) {
    if (a || b) {
        Node *sum = new_node(0);
        add_r(a, b, sum);
        return sum;
    }

    return NULL;
}

void print(Node *head) {
    while (head) {
        printf("%d->", head->val);
        head = head->next;
    }
    
    puts("");
}

void free_list(Node *head) {
    while (head) {
        Node *tmp = head;
        head = head->next;
        free(tmp);
    }
}

int main() {
    int a_data[3] = {2, 4, 3};
    int b_data[5] = {9, 5, 9, 4, 8};
    Node *a = list(3, a_data);
    Node *b = list(5, b_data);
    Node *sum = add(a, b);
    print(sum);
    free_list(sum);
    free_list(a);
    free_list(b);
    return 0;
}
