'''
17.12 
BiNode: Consider a simple data structure called BiNode, which has pointers to two other nodes.

public class BiNode {
  public BiNode nodel, node2;
  public int data;
}

The data structure BiNode could be used to represent both a binary tree (where nodel is the left
node and node2 is the right node) or a doubly linked list (where nodel is the previous node and
node2 is the next node). Implement a method to convert a binary search tree (implemented with
BiNode) into a doubly linked list. The values should be kept in order and the operation should be
performed in place (that is, on the original data structure).

Hints: #509, #608, #646, #680, #707, #779
'''

class Node:
    def __init__(self, val, node1=None, node2=None):
        self.val = val
        self.node1 = node1
        self.node2 = node2


def to_linked_list(root):
    head = [None]
    to_ll_helper(root, head)
    return head[0]


def to_ll_helper(root, head, prev=None):
    if root:
        prev_left = to_ll_helper(root.node1, head, prev)
        
        if prev_left:
            prev = prev_left

        if prev:
            prev.node2 = root
        else:    
            head[0] = root

        root.node1 = prev
        prev_right = to_ll_helper(root.node2, head, root)

        if prev_right:
            return prev_right
    
    return root


if __name__ == "__main__":
    '''     5
           / \
          2   6
         / \   \
        1   4   7
           /     \
          3       8
    '''
    root = Node(
        5,
        Node(
            2,
            Node(1),
            Node(
                4,
                Node(3)
            )
        ),
        Node(
            6,
            None, 
            Node(
                7, 
                None,
                Node(8)
            )
        )
    )

    head = to_linked_list(root)

    while head:
        print(head.val)
        head = head.node2
