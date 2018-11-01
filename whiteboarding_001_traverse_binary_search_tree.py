#!/usr/bin/env python

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

# Defining this tree:
#
#        5
#      /   \
#     3     10
#    / \   /  \
#   2   4 6    11

n2 = Node(2, None, None)
n4 = Node(4, None, None)
n3 = Node(3, n2, n4)
n6 = Node(6, None, None)
n11 = Node(11, None, None)
n10 = Node(10, n6, n11)
n5 = Node(5, n3, n10)

def traverse(node):
    if node is None:
        return
    traverse(node.left)
    print node.value
    traverse(node.right)

traverse(n5)
