#12/12/2018: Problem 5

class Foo:
    def method1(self):
        print("Called method 1")

    def method2(self):
        print("Called method 2")

    def method3(self):
        print("Called method 3")

def runMethodsForcingOrderInConcurrency(loopForever = False):
    """
    Three methods of an object, each called in separate threads,
    are forced to be called in a set sequence
    (i.e., method1, then method2, then method3).
    If specified in the parameter,
    this sequence will repeat in a cycle forever.

    Author: Eugene Ma
    """

    import threading

    foo = Foo()

    stage = 0
    stageLock = threading.RLock()
    stageCond = threading.Condition(stageLock)

    def makeTarget(preReqStage, func, nextStage):
        def target():
            nonlocal stage

            print('In thread: {0}'.format(threading.current_thread().name))

            while True:
                stageLock.acquire()
                try:
                    while True:
                        if stage == preReqStage:
                            func()
                            stage = nextStage
                            break;
                        else:
                            stageCond.wait()
                finally:
                    stageCond.notify_all()
                    stageLock.release()

                if not loopForever:
                    break;

        return target

    funcs = [
        lambda: foo.method1(),
        lambda: foo.method2(),
        lambda: foo.method3(),
    ]

    threads = []
    for i in range(3):
        nextStage = i + 1
        if loopForever:
            nextStage %= 3
        thread = threading.Thread(target=makeTarget(i, funcs[i], nextStage))
        threads.append(thread)

    import random
    random.shuffle(threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    # TODO: Pick one:
    runMethodsForcingOrderInConcurrency(False)
    #runMethodsForcingOrderInConcurrency(True)   # Loop forever
