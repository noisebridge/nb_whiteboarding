"""
12/26/2018: Problem 1:
Generate all binary strings of length n with k bits set

Implementation as a constraint satisfaction problem (CSP).

Author: Eugene Ma
"""

import n_choose_k_tests

def gen_n_choose_k_bitsets(n, k):
    def enum_n_choose_k_bitsets_by_csp(bitset_in_progress, start, num_chosen):
        if start == n:
            if num_chosen == k:
                yield bitset_in_progress
        else:
            num_to_choose = k - num_chosen
            num_remaining = n - start

            if num_chosen < k and num_to_choose <= num_remaining:
                # Choose it...
                bitset_from_choosing = (1 << start) | bitset_in_progress
                for bitset in enum_n_choose_k_bitsets_by_csp(
                        bitset_from_choosing, start + 1, num_chosen + 1):
                    yield bitset

            if num_to_choose <= num_remaining - 1:
                # ...or don't.
                for bitset in enum_n_choose_k_bitsets_by_csp(
                        bitset_in_progress, start + 1, num_chosen):
                    yield bitset

    for bitset in enum_n_choose_k_bitsets_by_csp(0, 0, 0):
        yield bitset

if __name__ == '__main__':
    n_choose_k_tests.test_n_choose_k(gen_n_choose_k_bitsets)
