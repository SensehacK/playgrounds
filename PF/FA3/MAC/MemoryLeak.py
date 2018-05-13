'''
Created on Mar 13, 2017

@author: kautilya.save
'''
from memory_profiler import profile
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a
my_func()