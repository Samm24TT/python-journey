# Dictionaries

band = {
    "vocals": "Plant",
    "guiter": "Page"
}

band2 = dict(vocals="Plant", guiter="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guiter"))

# lists all keys
print(band.keys())

# lists all values
print(band.values())

# lists of key/values pairs as typles
print(band.items())

# verify a key exits
print("guiter" in band)
print("sam" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band
# print('bad copy')
# print(band2)
# print(band)

# band2['drums'] = "Samm"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy")
print(band)
print(band2)

# or use the dict() constuructor function
band3 = dict(band)
print("Good copy")
print(f"band 3: {band3}")

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guiter"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update wit lists, tuples, and dictionaries, too.

# Merge two sets tocreate a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everthingexcept the duplicate
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
