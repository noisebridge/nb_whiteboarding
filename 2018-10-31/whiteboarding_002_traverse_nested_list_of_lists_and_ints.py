#!/usr/bin/env python

from __future__ import print_function

def depth_sum(L, d=0):
    if type(L) is int:
        return L * d

    count = 0
    for e in L:
        count += depth_sum(e, d+1)

    return count


print(depth_sum([[2], 3]))
print(depth_sum([[1, 2], 3, [4, 5, 6]]))
