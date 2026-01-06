# literal assignment
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
