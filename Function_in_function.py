"""I write a Functions in function and i use it in this function"""


def Calculste(a, b, what_do_you_want):
    def add(a, b):
        return a + b

    def zarb(a, b):# for example I can't write zarb function out the Calculste function (The same legb)
        return a * b

    if what_do_you_want == "add":
        return add(a, b)
    if what_do_you_want == "zarb":
        return zarb(a, b)


result = Calculste(3, 5, "zarb")
print(result)
