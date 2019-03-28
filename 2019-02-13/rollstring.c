#include <stdio.h>
#include <string.h>

void roll_string(int str_len, int amounts_len, char *str, int *amounts) {
    int buckets[str_len];
    memset(buckets, 0, str_len * sizeof(int));

    for (int i = 0; i < amounts_len; i++) {
        buckets[amounts[i]-1]++;
    }
    
    for (int i = str_len - 1; i >= 0; i--) {
        str[i] = (str[i] - 97 + buckets[i]) % 26 + 97;

        if (i > 0) {
            buckets[i-1] += buckets[i];
        }
    }
}

int main() {
    char str[] = "adz";
    int amounts[3] = {1, 1, 3};
    roll_string(3, 3, str, amounts);
    printf("%s\n", str);
    return 0;
}
