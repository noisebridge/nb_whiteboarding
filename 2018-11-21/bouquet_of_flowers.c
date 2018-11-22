/**
 * 1. In a given array of length n, find max(A[j] – A[i]) such that i < j.
 * 
 * 2. A person can create a flower bouquet with either 3 roses (cost of bouquet = p) or 1 rose and 1 lily (cost = q)
 * In an array of flowers, the person has to select contiguous set of flowers i.e. 2 or 3 to gain maximum cost.
 * 
 * Input format: A string of 0(denotes rose) and 1(denotes lily).
 * Output : Maximum cost.
 * 
 * Examples:
 * 
 * Input: p = 2, q = 3, s = 0001000
 * Output: 5
 *
 * https://www.geeksforgeeks.org/flipkart-internship-interview-on-campus/
*/

#include <stdio.h>
#include <string.h>

#define max(x, y) ((x) < (y) ? (y) : (x))

int max_profit(size_t s_len, char *s, int p, int q) {
    int dp[s_len], i;
    char roses[3];
    char rose_lily[2];
    memset(dp, 0, sizeof(dp));

    for (i = 1; i < s_len; i++) {
        dp[i] = dp[i-1];
        memcpy(rose_lily, &s[i-1], 2);
    
        if (!memcmp(rose_lily, "10", 2) || !memcmp(rose_lily, "01", 2)) {
            dp[i] = max(i - 2 >= 0 ? dp[i-2] + q : q, dp[i]);
        }

        if (i > 1) {
            memcpy(roses, &s[i-2], 3);

            if (!memcmp(roses, "000", 3)) {
                dp[i] = max(i - 3 >= 0 ? dp[i-3] + p : p, dp[i]);
            }
        }
    }

    return dp[s_len-1];
}

int main() {
    printf("%d\n", max_profit(8, "00011000", 2, 3));
    printf("%d\n", max_profit(7, "0001000", 2, 3));
    printf("%d\n", max_profit(18, "000101000010101000", 4, 1));
    printf("%d\n", max_profit(3, "010", 2, 3));
    printf("%d\n", max_profit(3, "100", 2, 3));
    printf("%d\n", max_profit(3, "001", 2, 3));
    printf("%d\n", max_profit(3, "000", 2, 3));
    printf("%d\n", max_profit(1, "0", 2, 3));
    return 0;
}
