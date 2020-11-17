import random
import threading
import time


def thread_task(index):
    print('Start Thread [%d]' % index)
    time.sleep(random.randint(3, 5))
    print('End Thread [%d]' % index)


if __name__ == '__main__':
    n_threads = int(input('Enter threads count: '))
    for i in range(n_threads):
        threading.Thread(target=thread_task, args=(i + 1,)).start()
        time.sleep(1)
