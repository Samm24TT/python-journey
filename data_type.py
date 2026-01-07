# literal assignment
import math
first = "john"
last = "smith"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructure function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like country song form the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
hello, Mr.Python

nice to meet you

               good nice!
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                           "
multiline = "                          " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print('')

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print('')

# string inex value
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some method return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.20
y = float(1.14)
print(type(gpa))

print('')

# complex type
comp_value = 5 + 2j
print(comp_value)
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

# math
print(math.pi)
print(math.sqrt(144))
print(math.floor(gpa))
print(math.ceil(gpa))

# Casting a string to a number
zipcode = '10010'
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
