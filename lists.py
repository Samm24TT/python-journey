users = ["Dave", "John", "Sara"]

data = ['Dave', 42, True]

emptyList = []

print(users[0])
print(users.index('Sara'))

print(users[0:1])
print(users[0:])
print(users[-3:-2])

print(len(data))

users.append('Elsa')
print(users)

users += ['jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data

data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
# print(sorted(nums, reverse=False))

print(type(nums))

myList = list([1, 'Neil', True])
print(myList)


# Tuples

myTuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(myTuple)
print(type(myTuple))
print(type(anothertuple))

print(anothertuple.count(2))
