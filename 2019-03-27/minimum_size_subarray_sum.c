#include <stdio.h>

int min_sub_array_len(int s, int* nums, int nums_size) {
    int best = nums_size;
    int curr = 0;
    
    for (int left = 0, right = 0; right < nums_size; right++) {
        curr += nums[right];
        
        while (left < right && curr - nums[left] >= s) {
            curr -= nums[left++];
        }
        
        if (curr >= s && right - left < best) {
            best = right - left;
        }
    }
    
    return best < nums_size ? best + 1 : 0;
}

int main() {
    int num_tests = 3;
    int s[] = {31, 15, 29};
    int nums[][50] = {
        {5,1,2,3,5,1,3,2,3,5,1,6,6,1,4,2},
        {8,1,2,3,1,2,3,15},
        {6,7,1,1,1,3,14,5,2,9,12}
    };
    int nums_sizes[] = {16, 8, 11};

    for (int i = 0; i < num_tests; i++) {
        printf("%d\n", min_sub_array_len(s[i], nums[i], nums_sizes[i]));
    }

    return 0;
}
