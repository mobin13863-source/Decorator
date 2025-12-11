"""Decorator"""

"""args is for when we want to pass any number of parameters
kwargs is so that if we write name = 10, it doesn't crash"""
import time


def macgic_dec(f):
    """It measures the start and end time of the function execution and counts each time it runs."""
    count = 0  # the External variable

    def wrapper(*args, **kwargs):
        nonlocal count  # for that I can use External variable
        count += 1  # Every time the program runs, someone adds one to it. 
        Start = time.time()  # save time
        result = f(*args, **kwargs)
        end = time.time()
        second = end - Start
        print(f"run in {second} second and called {count} time")
        return (
            count,
            result,
        )  # The outputs you see inside the output tuple are exactly these.

    return wrapper


@macgic_dec
def hello_to_name(name, age=18):
    """for hello to somaone"""
    return f"Hello {name} with {age} age"


print(hello_to_name("mobin", age=19))
