"""
12/26/2018: Problem 1:
Generate all binary strings of length n with k bits set

Implementation by using trailing subproblems
(i.e., subproblems where the bits
have indices in the range [start, n) where start is in [0, n]).

Author: Eugene Ma
"""

import n_choose_k_tests

def gen_n_choose_k_bitsets(n, k):
    def enum_n_choose_k_bitsets_by_subproblems(start, num_to_choose):
        if start == n:
            if num_to_choose == 0:
                yield 0
        else:
            num_remaining = n - start

            if num_to_choose > 0 and num_to_choose <= num_remaining:
                # Choose it...
                for rest in enum_n_choose_k_bitsets_by_subproblems(
                        start + 1, num_to_choose - 1):
                    yield (1 << start) | rest

            if num_to_choose <= num_remaining - 1:
                # ...or don't.
                for rest in enum_n_choose_k_bitsets_by_subproblems(
                        start + 1, num_to_choose):
                    yield rest

    for bitset in enum_n_choose_k_bitsets_by_subproblems(0, k):
        yield bitset

if __name__ == '__main__':
    n_choose_k_tests.test_n_choose_k(gen_n_choose_k_bitsets)
