/* Two sum variant where sum should be as close to a target value *
 * but not more, e.g. `[1,4,6,8], target = 11` returns `[4, 6]`.  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b) {
    return *((int *)a) - *((int *)b);
}

int *two_sum_or_less(size_t nums_len, int *nums, int target) {
    int left = 0;
    int right = nums_len - 1;
    int best = 0;
    int *res = calloc(2, sizeof(int));
    qsort(nums, nums_len, sizeof(int), cmp);

    while (left < right) {
        int total = nums[left] + nums[right];

        if (total <= target) {
            if (total > best) {
                best = total;
                res[0] = nums[left];
                res[1] = nums[right];
            }

            left++;
        }
        else {
            right--;
        }
    }
    
    return res;
}

int main() {
    int i;
    int nums[] = {1, 4, 6, 8};

    for (i = 0; i < 16; i++) {
        int *res = two_sum_or_less(4, nums, i);
        printf("target %d => [%d, %d]\n", i, res[0], res[1]);
        free(res);
    }

    return 0;
}
