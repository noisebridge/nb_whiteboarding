int rangeSumBST(TreeNode* root, int L, int R) {
    int sum = 0;

    if (root == NULL) return sum;

    if (root->val < L && root->right) {
        return sum += rangeSumBST(root->right,L,R);
    }
    if (R < root->val && root->left) {
        return sum += rangeSumBST(root->left,L,R);
    }
    if (root->val >= L && root->val <= R) {
        // For leetcode's test set the conditionals are faster than combining the three +='s
        sum += root->val;

        if (root->left) {
            sum += rangeSumBST(root->left,L,R);
        }
        if (root->right) {
            sum += rangeSumBST(root->right,L,R);
        }
    }

  return sum;
}