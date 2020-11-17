import multiprocessing
import random
import threading
import psutil
import time

import numpy as np


def task(index):
    v = np.random.randint(10, 20, (800, 800))
    np.savetxt('outputs/Matrix[%d]' % index, v)
    v2 = np.square(v)
    np.savetxt('outputs/SquaredMatrix[%d]' % index, v2)


def without_thread():
    start_time = time.time()
    for i in range(5):
        task(i+1)
    print('Without Thread: Executed in %fs' % (time.time() - start_time))


def threaded():
    start_time = time.time()
    threads = list()
    for i in range(5):
        threads.append(threading.Thread(target=task, args=(i + 1,)))
    random.shuffle(threads)
    for t in threads:
        t.start()
    print('CPU usage: {:.0f}%'.format(psutil.cpu_percent(interval=1)))
    for t in threads:
        t.join()
    print('All threads terminated: Executed in %fs' % (time.time() - start_time))


def multi_process():
    start_time = time.time()
    jobs = list()
    for i in range(5):
        jobs.append(multiprocessing.Process(target=task, args=(i + 1,)))
    random.shuffle(jobs)
    for t in jobs:
        t.start()
    print('CPU usage: {:.0f}%'.format(psutil.cpu_percent(interval=1)))
    for t in jobs:
        t.join()
    print('All jobs terminated: Executed in %fs' % (time.time() - start_time))


if __name__ == '__main__':
    without_thread()
    threaded()
    multi_process()
