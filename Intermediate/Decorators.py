#@mydecorator
#def dosometing():
#    pass

def mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Hello ")
        func(*args, **kwargs)
        print("How are you!")
    return wrapper

@mydecorator
def name():
    print("Alex")

name()

@mydecorator
def addition(x):
    print(x+10)

addition(19)

"""
import functools
def mydecorator(func):

    @functools.wrapper(func)
    def wrapper(*args, **kwargs):
        #do...
        result = func(*args, **kwargs)
        #do...
        return result
    return wrapper
"""


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executer {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def hello():
    print("Hello")

hello()
hello()
