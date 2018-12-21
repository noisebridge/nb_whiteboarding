"""
12/12/2018: Problem 4 solution

Given 100 computers that each gives you a number when you make 
a function call with the computer's ID, sum up the numbers.
"""


NUM_COMPS = 100

def makeGetNumFromCompId(nums = None, failureLikelihood = 0):
    """
    Make a function that simulates getting a number from some remote computer.

    This is a reasonable simulation for testing code with threads in Python
    because delaying returning the value by making the thread sleep
    does not make the CPU do heavy work just like how doing I/O
    to get the number from a remote computer for real
    would not make the CPU do heavy work.
    (The Global Interpreter Lock in Python
    prevents code from running in parallel,
    so using threads does not speed up CPU-intensive work,
    but it does speed up I/O work since it is not done by the CPU.)

    Author: Eugene Ma
    """

    import random

    if nums is None:
        nums = [random.randint(-1000, 1000) for compId in range(NUM_COMPS)]
    elif len(nums) < NUM_COMPS:
        raise ValueError("There should be at least {0} numbers "
                "in the numbers list.".format(NUM_COMPS))

    if failureLikelihood < 0 or failureLikelihood > 1:
        raise ValueError("Failure likelihood {0} is invalid."
                .format(failureLikelihood))

    import time

    def getNumFromCompId(compId):
        time.sleep(random.random() * 2.0)

        if failureLikelihood == 1 or random.random() <= failureLikelihood:
            raise IOError("Failed to get number from computer {0}."
                    .format(compId))
        else:
            return nums[compId]

    return getNumFromCompId

def getTotalFromCompsNaively(getNumFromCompId):
    """
    Sum a bunch of numbers without concurrency.

    Author: Eugene Ma
    """

    total = 0
    for compId in range(NUM_COMPS):
        success = False
        attempt = 0
        while not success:
            attempt += 1
            try:
                total += getNumFromCompId(compId)
                success = True
            except IOError as err:
                print("Attempt {0}: {1}".format(attempt, err))

    return total

def getTotalFromCompsConcurrently(getNumFromCompId):
    """
    Sum a bunch of numbers using concurrency.

    Author: Eugene Ma
    """

    import threading

    total = 0
    totalLock = threading.RLock()

    def fetchNumFromCompIdAndAddToTotal(compId):
        nonlocal total

        # Fetch number from computer.
        num = None
        attempt = 0
        while num is None:
            attempt += 1
            try:
                num = getNumFromCompId(compId)
            except IOError as err:
                print("Attempt {0}: {1}".format(attempt, err))

        # Add to total.
        totalLock.acquire()
        try:
            # Artificial way to allow race condition
            # to mess up this code: total += num
            import time
            oldTotal = total
            time.sleep(0.001)
            total = oldTotal + num
        finally:
            totalLock.release()

    threads = []
    for compId in range(NUM_COMPS):
        thread = threading.Thread(target=fetchNumFromCompIdAndAddToTotal,
                args=(compId, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return total

if __name__ == '__main__':
    compIdsToNums = [-39, 498, -532, -453, 925, 687, 720, -664, -883, 939,
        -862, -985, 873, -390, 658, 824, -767, -434, 617, -39, -80, -319, 694,
        587, 510, 567, -819, -412, 529, 872, 203, 790, 503, 296, 956, -373,
        -338, 675, -782, -798, 549, 651, -38, 834, 481, 223, 994, -939, -16,
        882, 288, 469, 158, 29, -421, -994, 710, 465, 915, -526, 969, -586,
        -991, 935, 671, 952, 869, 798, -94, -837, -555, 954, 530, -20, 368,
        293, 139, 294, -486, 130, -503, -591, 233, 54, 220, -512, 45, 155,
        560, -488, 981, 626, -835, -354, 232, 391, 369, 902, 992, 340]

    # Gold standard
    goldTotal = sum(compIdsToNums)

    getNumFromCompId = makeGetNumFromCompId(compIdsToNums, 0.25)

    # TODO: Pick one:
    #total = getTotalFromCompsNaively(getNumFromCompId)
    total = getTotalFromCompsConcurrently(getNumFromCompId)

    if total == goldTotal:
        print("Passed test")
    else:
        print("Failed test: {0} != {1} (answer)".format(total, goldTotal))
