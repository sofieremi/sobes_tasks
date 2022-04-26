import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        print(f'ELAPSE TIME: {time.time() - start}')
        return val

    return wrapper


@timer
def worker():
    time.sleep(2.3)


worker()


def chain_sum(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper

    return wrapper


print(chain_sum(5)(2)())


def chain_sum2(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        try:
            number2 = int(number2)
        except TypeError:
            return result
        result += number2
        return wrapper

    return wrapper


print(chain_sum2(2)(3)())


def chain_sum3(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper

        logic = {
            type(None): lambda: wrapper.result,
            int: inner
        }
        return logic[type(number2)]()

    wrapper.result = number
    return wrapper


print(chain_sum3(5)(2)())


class Chain_sum:
    def __init__(self, number):
        self.number = number

    def __call__(self, value=0):
        return Chain_sum(self.number + value)

    def __str__(self):
        return str(self.number)


class Sum(int):
    def __call__(self, addition=0):
        return Sum(self + addition)


print(Sum(2)(5) + 1)

import math

print(math.sin(Sum(100)))
