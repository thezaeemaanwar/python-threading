from threading import *
import time


class Thread1(Thread):
    def run(self):
        for n in range(10):
            print("\tIn MyThread 01 - ", n)
            time.sleep(2)
            print("\twakey - ", n)


class Thread2(Thread):
    def run(self):
        for n in range(30):
            print("\t\tIn Thread 02 - ", n)
            time.sleep(0.5)
            print("\t\tWakey - ", n)


class Thread3(Thread):
    def run(self):
        for n in range(5):
            print("\t\t\tIn Thread 03 - ", n)
            time.sleep(2)
            print("\t\t\tWakey - ", n)


def main():
    thread_1 = Thread1()
    thread_2 = Thread2()
    thread_3 = Thread3()
    print("I am parent")
    thread_1.start()
    thread_2.start()
    thread_3.start()
    time.sleep(5)
    print("parent woke up")


if __name__ == "__main__":
    main()
