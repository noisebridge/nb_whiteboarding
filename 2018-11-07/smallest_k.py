'''
17.14

Smallest K: Design an algorithm to find the smallest K numbers in an array.
'''

def partition(arr, start, end):
    """
    Partitions array in the given half-inclusive span: [start, end)
    Returns the end of the lower half (equivalently the start of the upper half)

    Author: Eugene Ma
    """

    n = end - start

    if n <= 1:
        return end

    # Range of lower bucket
    start1 = start
    end1 = start1

    # Range of upper bucket
    start2 = end - 1
    end2 = start2

    from random import randint

    pivot = randint(start, end - 1)
    # Put pivot value at end of span
    arr[pivot], arr[end2] = arr[end2], arr[pivot]

    pivotVal = arr[end2]

    while end1 < start2:
        val = arr[end1]

        if val < pivotVal:
            # Add in lower bucket
            end1 += 1
        else:
            # Add in upper bucket
            start2 -= 1
            arr[end1], arr[start2] = arr[start2], arr[end1]

    # Put pivot value at end of lower bucket
    arr[end1], arr[end2] = arr[end2], arr[end1]
    end1 += 1
    start2 += 1
    end2 += 1

    return end1

def partitionFirstK(arr, start, end, k):
    """
    Puts the k lowest values in the given half-inclusive span [start, end)
    into the first k slots of the span.
    Returns the end of the span containing these values.

    Author: Eugene Ma
    """

    n = end - start

    if k == 0:
        return start
    elif k >= n:
        return end

    targetDivider = start + k

    # Do binary search to find the target partition spot (the "divider").
    divider = partition(arr, start, end)    # Priming read
    while divider != targetDivider:
        if divider < targetDivider:
            start = divider
        else:
            end = divider

        divider = partition(arr, start, end)

    return targetDivider

if __name__ == "__main__":
    def testPartitionFirstK():
        """
        Tests partitionFirstK().

        Author: Eugene Ma
        """

        tests = [   (14,
                    [16, 64, 100, 54, 93, 38, 48, 45, 97, 16, 50, 19, 49, 36, 53,
                    15, 39, 18, 80, 55, 5, 2, 18, 88, 84, 98, 56, 80, 47, 1, 87,
                    88, 79, 55, 5, 99, 76, 26, 31, 13, 46, 61, 92, 95, 20, 8, 25]),

                    (40,
                    [29, 64, 28, 67, 30, 3, 22, 11, 60, 91, 8, 19, 2, 68, 30,
                    13, 95, 86, 75, 62, 45, 13, 51, 93, 11, 9, 71, 52, 1, 57,
                    9, 70, 42, 41, 99, 48, 14, 32, 15, 88, 52, 1, 94, 2, 65,
                    47, 49, 21, 16, 26, 89, 58, 26]),

                    (412,
                    [32, 57, 29, 57, 8, 37, 7, 89, 27, 84, 96, 45, 62, 87, 87, 17,
                    56, 39, 3, 73, 44, 44, 78, 34, 52, 60, 15, 63, 23, 34, 16, 38,
                    21, 19, 87, 17, 21, 82, 4, 62, 19, 26, 49, 25, 38, 58, 77, 61,
                    69, 45, 69, 56, 76, 66, 26, 75, 48, 84, 75, 65, 75, 46, 61, 9,
                    45, 76, 97, 47, 22, 30, 78, 83, 19, 65, 96, 30, 39, 45, 84, 63,
                    41, 65, 93, 32, 9, 72, 57, 100, 60, 61, 41, 40, 95, 15, 17, 10,
                    97, 60, 19, 73, 88, 73, 53, 41, 57, 17, 98, 59, 34, 90, 7, 6,
                    50, 84, 35, 37, 96, 3, 77, 28, 68, 33, 71, 87, 18, 24, 47, 33,
                    85, 95, 34, 32, 92, 31, 84, 44, 36, 23, 19, 17, 58, 34, 17, 29,
                    47, 58, 26, 7, 62, 68, 93, 58, 75, 65, 46, 32, 92, 28, 13, 64,
                    67, 16, 48, 17, 1, 84, 64, 41, 66, 7, 18, 29, 43, 70, 46, 25,
                    89, 12, 41, 98, 5, 54, 32, 23, 85, 17, 69, 44, 83, 18, 1, 81,
                    89, 28, 20, 9, 54, 61, 36, 41, 82, 75, 56, 5, 86, 14, 34, 90,
                    59, 37, 97, 74, 86, 8, 5, 76, 88, 87, 69, 70, 74, 91, 57, 39,
                    1, 38, 84, 56, 13, 15, 67, 22, 7, 74, 55, 37, 76, 61, 63, 22,
                    36, 2, 77, 16, 26, 34, 20, 19, 42, 59, 28, 16, 84, 48, 57, 71,
                    5, 78, 23, 33, 26, 74, 17, 46, 2, 70, 66, 13, 23, 74, 18, 23,
                    3, 30, 92, 83, 90, 83, 5, 82, 86, 100, 39, 10, 90, 17, 93, 27,
                    31, 70, 95, 60, 5, 36, 61, 20, 82, 5, 15, 25, 55, 91, 13, 37,
                    86, 54, 5, 83, 34, 33, 13, 35, 73, 9, 74, 58, 40, 62, 80, 16,
                    45, 17, 54, 83, 100, 70, 60, 92, 73, 58, 75, 62, 96, 1, 52, 4,
                    76, 33, 58, 98, 80, 32, 58, 98, 94, 53, 20, 53, 48, 1, 67, 27,
                    51, 7, 81, 85, 79, 62, 90, 61, 56, 51, 77, 23, 55, 23, 42, 31,
                    8, 62, 64, 51, 81, 64, 88, 73, 22, 79, 43, 98, 32, 66, 32, 91,
                    6, 72, 83, 83, 45, 30, 93, 30, 69, 78, 48, 79, 36, 5, 8, 39,
                    77, 28, 84, 30, 31, 92, 81, 44, 50, 17, 20, 24, 29, 64, 27,
                    82, 59, 63, 87, 40, 7, 97, 49, 7, 22, 14, 53, 12, 17, 95, 10,
                    65, 58, 7, 18, 21, 68, 44, 100, 9, 21, 56, 28, 36, 35, 52, 4,
                    94, 33, 58, 91, 97, 74, 46, 21, 32, 54, 30, 88, 69, 14, 67,
                    94, 12, 63, 93, 64, 93, 60, 21, 53, 9, 38, 85, 2, 17, 51, 81,
                    35, 55, 34, 76, 65, 71, 23, 36, 17, 8, 20, 85, 53, 95, 81, 1,
                    74, 4, 18, 72, 55, 16])
                ]

        from collections import Counter

        numPassed = 0
        for testIndex, test in enumerate(tests):
            k, arr = test

            # Gold standard
            goldStandardArr = arr.copy()
            goldStandardArr.sort()
            goldStandardCounts = Counter()
            for i in range(k):
                goldStandardCounts[goldStandardArr[i]] += 1

            # Test
            passedTest = True
            end = partitionFirstK(arr, 0, len(arr), k)
            if end != k:
                passedTest = False
            counts = Counter()
            for i in range(k):
                counts[arr[i]] += 1
            if counts != goldStandardCounts:
                passedTest = False

            if passedTest:
                numPassed += 1
            else:
                print('Failed test:', testIndex + 1)

        print(numPassed, 'of', len(tests), 'passed')

    testPartitionFirstK()
