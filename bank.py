import sys
import threading
import logging
import random
import time


def withdraw(Acc1,Acc2):

   for i in range(50):
     r = random.random()
     logging.debug('Sleeping %0.02f', r)
     time.sleep(r)
     Acc1.withdraw(r)
     Acc2.withdraw(r)
     print("Number : {}\n".format(r))
     print("Withdraw from A balance : {}".format(Acc1.value))
     print("Withdraw from B balance : {}\n".format(Acc2.value))
      #print how much you subtract from and new acc value

def deposit(Acc1,Acc2):

   for i in range(50):
     r = random.random()
     logging.debug('Sleeping %0.02f', r)
     time.sleep(r)
     Acc1.deposit(r)
     Acc2.deposit(r)
     print("Number : {}\n".format(r))
     print("Deposit from A balance : {}".format(Acc1.value))
     print("Deposit from B balance : {}\n".format(Acc2.value))
     # print how much you add and  new acc value

class bankAcc:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start  # initial account value

    def withdraw(self,value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Lock for withdraw')
            self.value = self.value - value
        except:
            logging.debug('Error')
        finally:
            logging.debug('Release Withdraw')
            self.lock.release()

    def deposit(self,value):
        logging.debug('Waiting for a lock')
        self.lock.acquire()
        try:
            logging.debug('Lock for deposit')
            self.value = self.value + value
        except:
            logging.debug('Error')
        finally:
            logging.debug('Release Withdraw')
            self.lock.release()

if __name__ == '__main__':
    A = bankAcc(10)

    B = bankAcc(3)


    for i in range(3):
        t = threading.Thread(target=deposit, args=(A,B))
        t.start()

    for i in range(3):
        t = threading.Thread(target=withdraw, args=(A,B))
        t.start()


    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('A: %d B %d', A.value,B.value)
