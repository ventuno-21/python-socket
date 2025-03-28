"""
threading allows to speed up programs by eecuting multiple task concurrently
eachh task wil be run on its own threading
each thread can run concurrently and share with each other

every thread when you start it must do sth, which we can define with a function
our threads will then target these functions
when we start th threads the target wukk be run
"""

import threading


def function_1():
    for i in range(10):
        print("one")


def function_2():
    for i in range(10):
        print("two")


def function_3():
    for i in range(10):
        print("three")


# # below functions will be run linearly/sequentially
# function_1()
# function_2()
# function_3()


# execute these functions concurently using threads
t1 = threading.Thread(target=function_1)
t2 = threading.Thread(target=function_2)
t3 = threading.Thread(target=function_3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# threading can only be run once, if you cant to reuse, you must redeifine
t1 = threading.Thread(target=function_1)
t1.start()
t1.join()


# if you want to pause the main program until a thread is done you can
t1 = threading.Thread(target=function_1)
t1.start()
t1.join()

print(
    "if we use join() method, this line will be execute after that, otherwise if we dont use join(), this print will show up anytime between our tasks's outputs"
)
