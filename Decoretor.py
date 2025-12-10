import datetime


def run_on_zog(f):
    def wrapper():
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            f()
        else:
            print("hisss")

    return wrapper


@run_on_zog
def say_hello():
    print("hi! Im here")


@run_on_zog
def bye():
    print("bye bye")


say_hello()
bye()
