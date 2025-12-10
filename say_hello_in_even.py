"""If the minute is even, you cannot speak; otherwise, you can."""

import datetime


def is_even():
    now = datetime.datetime.now()
    minute = now.minute
    return minute % 2 == 0


def say_hello():
    if is_even():
        print("hiss")
    else:
        print("Hi, Im here")


def say_bye():
    if is_even():
        print("hisss")
    else:
        print("bye bye")


say_hello()
say_bye()
