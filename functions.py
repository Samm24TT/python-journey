# Functions
# for a naming, should use all lower-case for naming a functions

def hello_world():
    print("hello world")


hello_world()


def hello_name(name):
    return "hello " + name


yourname = hello_name("Samuel")
print(yourname)


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


total = sum(1)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", last="John")
