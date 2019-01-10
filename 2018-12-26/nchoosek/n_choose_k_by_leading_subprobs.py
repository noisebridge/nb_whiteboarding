"""
12/26/2018: Problem 1:
Generate all binary strings of length n with k bits set

Implementation by using leading subproblems
(i.e., subproblems where the bits
have indices in the range [0, end) where end is in [0, n]).

Author: Eugene Ma
"""

import n_choose_k_tests

def gen_n_choose_k_bitsets(n, k):
    if n == 0:
        # Base case
        if k == 0:
            yield 0
        else:
            raise ValueError("Illegal value for k: {}. (n = {})".format(k, n))
    elif n >= 1:
        if k > 0 and n >= k:
            # Choose it...
            for rest in gen_n_choose_k_bitsets(n - 1, k - 1):
                yield (1 << (n - 1)) | rest

        if n - 1 >= k:
            # ...or don't.
            for rest in gen_n_choose_k_bitsets(n - 1, k):
                yield rest
    else:
        raise ValueError("Illegal value for n: {}. (k = {})".format(n, k))

if __name__ == '__main__':
    n_choose_k_tests.test_n_choose_k(gen_n_choose_k_bitsets)
