"""The code you wrote is a simple decorator that measures the execution time of a function."""

import time


def macgic_decorator(f):
    """When you want to find out how long a function takes to execute"""

    def wrapper(n):
        start = time.time()  # I save the time
        result = f(n)  # I call the function (the main code and that paramtetr)
        end = time.time()
        second = end - start
        print(f"run in {second} second")
        return result

    return wrapper  # we return the wrapper with out the ()


@macgic_decorator
def make_list(n):
    """My main code"""
    number = [i for i in range(1, n + 1)]  # I use List Comprehension
    return number


print(make_list(10))
