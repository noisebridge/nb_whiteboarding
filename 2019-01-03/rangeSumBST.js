function rangeSum(node, sum, L, R) {
    if (!node) return 0;
    if (node.val >= L && node.val <= R) {
        sum += node.val + rangeSum(node.left, sum, L, R) + rangeSum(node.right, sum, L, R);
        return sum;
    }
    if (node.val < L) return rangeSum(node.right, sum, L, R);
    if (node.val > R) return rangeSum(node.left, sum, L, R);
    return 0;
}

var rangeSumBST = function(root, L, R) {
    var sum = 0;
    sum = rangeSum(root, sum, L, R);
    return sum;
};