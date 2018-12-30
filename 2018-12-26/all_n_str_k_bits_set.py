'''
Generate all binary strings of length n with k bits set
'''

from itertools import permutations


def all_n_str_k_bits_set_cheapo(n, k):
    return list(set(permutations([1] * k + [0] * (n - k), n)))


def all_n_str_k_bits_set(n, k, curr="", popcount=0):
    if len(curr) == n and popcount == k:
        yield curr
    elif len(curr) < n:
        if popcount < k:
            yield from all_n_str_k_bits_set(n, k, curr + "1", popcount + 1)
            
        yield from all_n_str_k_bits_set(n, k, curr + "0", popcount)


if __name__ == "__main__":
    print(list(all_n_str_k_bits_set(4, 2)))
    print(list(all_n_str_k_bits_set(4, 3)))
