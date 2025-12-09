"""this is another way"""


def add(a, b):
    return a * b


def all(a, b, what_you_wnat):
    return what_you_wnat(a, b)


print(all(3, 4, add))
# or


def say_hello():
    print("hello there")


def do(what_to_do):
    what_to_do()
    what_to_do()


do(say_hello)
