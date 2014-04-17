__filename__ = 'multithread_demo.py'
__author__ = 'jwestover@sonobi.com'

import multiprocessing
import time
import random

class HelloWorld(object):

    def __init__(self):
        self.my_number = 1
        self.my_number_2 = multiprocessing.Value('i', 1)
        #self.lock = threading.Lock()
        self.lock = multiprocessing.Lock()

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
            time.sleep(10)
        return 'More stupid stuff'

    def thread_target2(self, parameter = None):
        time.sleep(.1*random.randint(0,10))
        self.my_number += 1
        time.sleep(float(parameter))
        self.my_number += 1
        print self.my_number

    def thread_target3(self, parameter = None):
        time.sleep(.1*random.randint(0,10))
        with self.my_number_2.get_lock():
            self.my_number_2.value += 1
        time.sleep(float(parameter))
        with self.my_number_2.get_lock():
            self.my_number_2.value += 1
        print self.my_number_2.value

    def demo1(self):

        for i in range(10):
            #this_thread = threading.Thread(target = self.thread_target1, args = (i,)).start()
            this_thread = multiprocessing.Process(target = self.thread_target1).start()
            #print 'Thread count: {0}'.format(threading.active_count())
            print 'Process count: {0}'.format(multiprocessing.active_children())
            #This should return something
            print this_thread
    def demo2(self):

        for i in range(10):
            #this_thread = threading.Thread(target = self.thread_target1, args = (i,)).start()
            this_process = multiprocessing.Process(target = self.thread_target1, args = (i,))
            this_process.daemon = True
            this_process.start()
            #print 'Thread count: {0}'.format(threading.active_count())
            print 'Process count: {0}'.format(multiprocessing.active_children())
        time.sleep(60)


    def demo3(self):
        for i in range(10):
            #this_thread = threading.Thread(target = self.thread_target1, args = (i,)).start()
            this_process = multiprocessing.Process(target = self.thread_target2, args = (i,))
            this_process.daemon = False
            this_process.start()
            #print 'Thread count: {0}'.format(threading.active_count())
            print 'Process count: {0} My Number: {1}'.format(multiprocessing.active_children(), self.my_number)
            #print 'Thread count: {0} My Number: {1}'.format(threading.active_count(), self.my_number)

    def demo4(self):
        for i in range(10):
            #this_thread = threading.Thread(target = self.thread_target1, args = (i,)).start()
            this_process = multiprocessing.Process(target = self.thread_target3, args = (i,))
            this_process.daemon = False
            this_process.start()
            #print 'Thread count: {0}'.format(threading.active_count())
            print 'Process count: {0} My Number {1}'.format(multiprocessing.active_children(), self.my_number)
            #print 'Thread count: {0} My Number: {1}'.format(threading.active_count(), self.my_number)

test = HelloWorld()
#test.demo1()
#test.demo2()
#test.demo3()
test.demo4()