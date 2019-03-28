#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

void deepest_node_r(
    TreeNode *root, TreeNode **deepest, int depth, int *max_depth
) {
    if (root) {
        if (depth > *max_depth) {
            *max_depth = depth;
            *deepest = root;
        }

        deepest_node_r(root->left, deepest, depth + 1, max_depth);
        deepest_node_r(root->right, deepest, depth + 1, max_depth);
    }
}

TreeNode *deepest_node_recursive(TreeNode *root) {
    TreeNode **deepest = &root;
    int max_depth = 0;
    deepest_node_r(root, deepest, 0, &max_depth);
    return *deepest;
}

typedef struct Frame {
    TreeNode *node;
    int depth;
} Frame;

TreeNode *deepest_node_iterative(TreeNode *root) {
    TreeNode *deepest = root;
    int stack_capacity = 2;
    int stack_len = 1;
    int max_depth = 0;
    Frame *stack = malloc(sizeof(*stack) * stack_capacity);
    Frame base = {root, 0};
    stack[0] = base;

    while (stack_len) {
        Frame curr = stack[--stack_len];

        if (curr.node) {
            if (curr.depth > max_depth) {
                max_depth = curr.depth;
                deepest = curr.node;
            }
            
            if (stack_len + 2 > stack_capacity) {
                stack_capacity *= 2;
                Frame *tmp = realloc(stack, sizeof(*tmp) * stack_capacity);

                if (!tmp) {
                    fprintf(stderr, "%s, %d: malloc failed\n", __func__, __LINE__);
                    exit(1);
                }

                stack = tmp;
            }

            Frame left = {curr.node->left, curr.depth + 1};
            Frame right = {curr.node->right, curr.depth + 1};
            stack[stack_len++] = left;
            stack[stack_len++] = right;
        }
    }
    
    free(stack);
    return deepest;
}

int main() {
    TreeNode h = {9, NULL, NULL};
    TreeNode g = {8, &h, NULL};
    TreeNode f = {7, NULL, NULL};
    TreeNode e = {6, NULL, &g};
    TreeNode d = {5, NULL, &f};
    TreeNode c = {4, NULL, NULL};
    TreeNode b = {3, NULL, &e};
    TreeNode a = {2, &c, &d};
    TreeNode root = {1, &a, &b};

    /*      1
           / \
          2   3 
         / \   \
        4   5   6
             \   \
              7   8
                 /
                9    */
    
    printf("%d\n", deepest_node_recursive(&root)->val);
    printf("%d\n", deepest_node_iterative(&root)->val);
    return 0;
}
