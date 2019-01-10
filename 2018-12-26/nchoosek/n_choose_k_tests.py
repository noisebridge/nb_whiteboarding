"""
Test utilities for n-choose-k implementations.

Author: Eugene Ma
"""

def bitset_to_str(bitset, n):
    """
    Returns the string for the bitset where n bits are shown.
    Most significant bits will be on the left.
    """

    sb = [str((bitset >> i) & 1) for i in range(n - 1, -1, -1)]

    return ''.join(sb)

def test_n_choose_k(gen_n_choose_k_bitsets):
    """
    Tests the generator, which generates all the possible n-choose-k bitsets.
    The generator should take parameters: n, k.
    """

    nks = [
        (8, 3),
        (4, 2),
        (4, 3),
        (1, 1),
        (1, 0),
        (0, 0)
    ]

    for n, k in nks:
        print("{} choose {} bitsets:".format(n, k))
        num_bitsets = 0
        for bitset in gen_n_choose_k_bitsets(n, k):
            print(bitset_to_str(bitset, n))
            num_bitsets += 1
        print("({} {} for {} choose {})\n".format(
                num_bitsets, "bitset" if num_bitsets == 1 else "bitsets", n, k))
