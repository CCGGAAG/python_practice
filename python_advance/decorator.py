# coding=utf-8

from __future__ import print_function
import builtins
import traceback

__base_print = print

def nb_print(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        __base_print(traceback.format_stack()[-2])
    return wrapper
builtins.print = nb_print(print)

def log(func):
    def wrapper(*args, **kwargs):
        print("哈哈哈{}".format(func.__name__))
        func(*args, **kwargs)
    return wrapper

class demo():

    @nb_print
    @log
    def test(self, add):
        print("hello")
        print(add)

if __name__ == '__main__':
    demo().test("123")