"""
https://www.hackerrank.com/challenges/larrys-array/problem

See the doc tests for testing.

For more explanation of the 15 tiles solvability:
https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
"""


def larrysArray(A):
    """ Checks if an array can be sorted with rotations based on the parity of a permutations, which are preserved on rotations 
    >>> larrysArray([3, 1, 2])
    'YES'
    >>> larrysArray([1, 3, 4, 2])
    'YES'
    >>> larrysArray([1, 2, 3, 5, 4])
    'NO'
    >>> larrysArray([1, 6, 5, 2, 3, 4])
    'NO'
    """

    inversions = mergeSortCt(A, 0, len(A))
    return 'YES' if inversions % 2 == 0 else 'NO' # An even amount of inversions is sortable, since a sorted array has 0 inversions.

def mergeSortCt(A, start, end):
    """ Applies merge sort algorithm but counts  every time an element must be swapped to keep track the count of the inversions
    >>> mergeSortCt([3, 1, 2], 0, 3)
    2
    >>> mergeSortCt([5, 6, 7, 8], 0, 4)
    0
    """

    if start >= end-1:
        return 0
    else:

        mid = (start + end)//2
        inversions =  mergeSortCt(A, start, mid) \
                    + mergeSortCt(A, mid, end) \
                    + merge(A, start, mid, end) 
        return inversions


def merge(A, start, mid, end):
    """ Merges two sorted halves, separated by indexes: 
    [start, mid)  and [mid, end)
    >>> A = [1,2,5,3,4,6]
    >>> mid = len(A)//2
    >>> merge(A, 0, mid, len(A))
    2
    >>> A
    [1, 2, 3, 4, 5, 6]
    """ 
    i, j = start, mid

    temp = []
    inversions = 0
    while( i < mid and j < end):

        if A[i] > A[j]:
            temp.append(A[j])
            inversions += mid - i  # All elements from index i until middle are also greater (transitive property)
            j += 1
        else:
            temp.append(A[i])
            i += 1

    # Handle leftovers
    while i < mid:
        temp.append(A[i])
        i += 1
    while j < end:
        temp.append(A[j])
        j += 1

    # Mutate original array to be sorted
    for i, element in enumerate(temp, start):
        A[i] = element

    return inversions

if __name__ == "__main__":

    import doctest
    doctest.testmod()
