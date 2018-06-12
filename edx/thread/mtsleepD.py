#!/usr/bin/env python

import threading
from time import sleep, ctime

looos = [4, 2]

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):

    print('start loop ', nloop, 'at', ctime())
    sleep(nesc)
    print('loop', nloop, ctim())

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops: #Create all threads
        t = threading.Thread(
                target=ThreadFunc(loop, (i,loops[i])),
                loop.__name__)
        threads.append(t)

        for i in nloops:  # start all threads
            threads[i].start()

        for i in nloops:
            thread[i].join()

        print'All DONE at:', ctime()

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.THread.__init__(self)
        self.name = name
        slef.func = func
        slef.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start '
    sleep(nesc)
    print 'loop', nloop


def main():
    print 'starting at:', ctime()

    threads = []
    nloop = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), 
                loop.__name__)

    for i in loops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'All DONE at:', ctime()

if __name__ == '__main__':

    main()



class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        slef.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:', \
                ctime()
        self.res = self.func(*self.args)
        print self.name, 'finised at:', \
                ctime()







if __name__ == '__main__':
    main()


