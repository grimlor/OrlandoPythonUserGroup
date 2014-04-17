__filename__ = 'multithread_demo.py'
__author__ = 'jwestover@sonobi.com'

import threading
import time
import random

class HelloWorld(object):

    def __init__(self):
        self.my_number = 1
        self.lock = threading.Lock()

    def thread_target1(self, parameter = None):
        if parameter:
            print '{0} this parameter has been passed'.format(str(parameter))
            try:
                time.sleep(parameter)
                print 'Wake up time'
            except:
                #who cares
                pass
        else:
            print 'hello world.... this is stupid'
        return 'More stupid stuff'

    def thread_target2(self, parameter = None):
        time.sleep(.1*random.randint(0,10))
        self.my_number += 1
        time.sleep(float(parameter))
        self.my_number += 1
        print self.my_number

    def thread_target3(self, parameter = None):
        time.sleep(.1*random.randint(0,10))
        self.lock.acquire()
        self.my_number += 1
        self.lock.release()
        time.sleep(float(parameter))
        self.lock.acquire()
        self.my_number += 1
        self.lock.release()
        print self.my_number

    def demo1(self):

        for i in range(10):
            this_thread = threading.Thread(target = self.thread_target1, args = (i,)).start()
            print 'Thread count: {0}'.format(threading.active_count())
            #This should return something
            print this_thread
    def demo2(self):

        for i in range(10):
            this_thread = threading.Thread(target = self.thread_target1, args = (i,))
            this_thread.daemon = True
            this_thread.start()
            print 'Thread count: {0}'.format(threading.active_count())
        time.sleep(60)


    def demo3(self):
        for i in range(10):
            this_thread = threading.Thread(target = self.thread_target2, args = (i,))
            this_thread.daemon = False
            this_thread.start()
            print 'Thread count: {0} My Number: {1}'.format(threading.active_count(), self.my_number)

    def demo4(self):
        for i in range(10):
            this_thread = threading.Thread(target = self.thread_target3, args = (i,))
            this_thread.daemon = False
            this_thread.start()
            print 'Thread count: {0} My Number: {1}'.format(threading.active_count(), self.my_number)


test = HelloWorld()
#test.demo1()
#test.demo2()
#test.demo3()
#test.demo4()