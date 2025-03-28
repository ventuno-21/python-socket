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


# below functions will be run linearly
function_1()
function_2()
function_3()
