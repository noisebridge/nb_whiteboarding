/**
 * Explanation: https://www.hackerrank.com/challenges/larrys-array/forum/comments/541356
*/

#include <stdio.h>

int larrys_array(size_t len, int *arr) {
    int inversions = 0;

    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) { 
            if (arr[i] > arr[j]) {
                inversions++;
            }
        } 
    }

    return inversions % 2 == 0;
}

int main() {
    int tests[7][30] = {
        {22, 16, 6, 7, 24, 8, 11, 26, 18, 17, 10, 4, 1, 23, 15, 20, 21, 14, 25, 2, 3, 9, 13, 28, 12, 19, 5, 27},
        {7, 10, 9, 4, 6, 11, 3, 2, 8, 1, 5},
        {7, 19, 9, 10, 2, 3, 6, 1, 18, 15, 14, 8, 4, 11, 17, 16, 5, 13, 12},
        {13, 11, 17, 5, 16, 9, 7, 6, 2, 18, 15, 4, 1, 8, 14, 3, 10, 12},
        {4, 20, 22, 17, 8, 14, 11, 9, 3, 12, 7, 1, 10, 2, 15, 18, 5, 13, 6, 19, 16, 21, 23, 24},
        {29, 13, 9, 19, 25, 22, 11, 12, 20, 10, 4, 5, 21, 15, 8, 7, 2, 16, 18, 17, 26, 27, 6, 3, 14, 1, 23, 24, 28},
        {10, 22, 16, 13, 1, 3, 17, 11, 21, 15, 18, 6, 9, 4, 20, 19, 5, 2, 7, 14, 12, 8}
    };
    int test_sizes[7] = {28, 11, 19, 18, 24, 29, 22};

    for (int i = 0; i < 7; i++) {
        printf("%s\n", larrys_array(test_sizes[i], tests[i]) ? "YES" : "NO");
    }

    return 0;
}
