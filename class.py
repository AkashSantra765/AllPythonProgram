'''class item:
    x=5
    def __init__(self):
        self.a=10
i1=item()
print(i1.x)
print(i1.a)'''

'''class A:
    def __init__(self,k):
        self.a=k
i1=A(20)
print(i1.a)'''

#Example of class
'''class student:
    def __init__(self):
        self.name="Akash santra"
        self.age=20
        self.marks=80
    def talk(self):
        print("Hello I am :",obj.name)
        print("My age is :",self.age)
        print("My marks are :",self.marks)
obj=student()'''


import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")