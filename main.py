from concurrent.futures import thread
from threading import *
import time


class MyThread(Thread):
    def run(self):
        for n in range(10):
            print("In MyThread 01 - ", n)
            time.sleep(2)
            print("Thread 01 woke up - ",n)


class Thread2(Thread):
    def run(self):
        for n in range(10):
            print("In Thread 02 ", n)


def main():
    thread1 = MyThread()
    thread2 = Thread2()
    print("I am parent")
    thread1.start()
    time.sleep(3)
    thread2.start()
    print("parent woke up")


if __name__ == "__main__":
    main()
