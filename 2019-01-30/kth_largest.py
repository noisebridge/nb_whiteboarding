'''
O(n log(n)) solution
'''

from random import randint


def kth_largest_slow(a, k):
    return sorted(a)[len(a)-k:]


if __name__ == "__main__":
    test = [randint(0, 20) for _ in range(randint(0, 10))]
    k = randint(0, len(test))
    print(test, " k=%s =>" % k, kth_largest_slow(test, k))
