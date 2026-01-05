import math

print("Hello, world")
print('hello, world')
print("""this one run 
      multiple line""")  # triple quote for multi-line
print('This is a ' + 'string!')  # we can concatenate strings

# Math
print(50 + 50)  # add
print(50 - 50)  # substract
print(50 * 50)  # multiple
print(50/50)  # divide
print(50+50-50*50/50)  # PEMDAS

print('\n')

# variables and methods
age = 35
name = "Sam"
gpa = 3.7
print(int(age))

quote = "It's not over, until i win!"
print(quote)

print(quote.upper())  # uppercase
print(quote.lower())  # lowercase
print(quote.title())  # title case
print(len(quote))  # count character

print("My name is " + name + " and i am " + str(age) + " years old.")

age = 36
age += 1
print(age)

# x = float(input("give me a number: "))
# y = float(input("give me a another number: "))
# print(x + y)

print('\n')
# function - resuable block of code


def who_am_i(name, age):
    print(f"My name is {name} and i am {age} years old")


who_am_i("Sam", 35)


def add_one_hundred(num):
    print(num + 100)


add_one_hundred(100)
add_one_hundred(200)


def square_root(x):
    print(x ** .5)


square_root(64)


def nl():
    print('\n')


nl()
