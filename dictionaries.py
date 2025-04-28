# Dictionaries and Sets in python.
# Dictionaries are mutable, unordered collection of key-value pairs.

data = {
    "name" : "Sonal",
    "age" : 23,
    "city" : "Mumbai"
}
# or
data1 = dict(name ="Sonal", age = 23, city = "Mumbai")

print(data)
print(data1)
print(type(data))
print(len(data))

# Access Items

print(data["name"])
print(data.get("age"))

print(data.keys()) 
print(data.values())
print("age" in data)
print(data.items())

# change values
data["age"] = 24
data.update({"city": "DxB"})
print(data)

# remove items

data.pop("age")
print(data)

data["Dep"] = "IT"
print(data)

del data["Dep"]
print(data)

# copying dictionaries

data2 = data.copy()
data2["job"] = "Engineer"
print(data2)
print(data)

# or

data3 = dict(data)
print(data3)

# Nested Dictionaries

m1 = {
    "name": "Sonal",
    "age" : 24,
    "city": "Mumbai",
    "job": {
        "title": "Engineer",
        "company": "Shivnal"
    }
}
print(m1)
print(m1["job"]["title"])
print(m1.get("age"))

# Sets
# Set is an unordered collection of unique elements.
# Sets are mutable, but the elements of a set must be immutable.
# Sets do not support indexing, slicing, or other sequence-like behaviour.
# Sets are used to store multiple items in a single variable.
# It is used to perform set of operations like union, intersection, difference, etc.
# It is used to remove duplicates from a list.

s1 = set((2,5,8,10))
s2 = {1,2,3,4,5}
print(s1)
print(type(s1))
print(s2)
print(type(s2))

# no duplicates allowed

s3 = {1,2,2,3,4,5,5}
print(s3)

s4 = {1, True, 2, 3, False,0} # True is 1 and False is 0
print(s4) # 1 is not added twice 

s4.add(10)
print(s4)

s4.update(s2)
print(s4)

# Merge two sets

a1 = {1,2,3}
a2 = {4,5,6}
a = a1.union(a2)
print(a)

# to get the duplicates

a1 = {1,2,3}
a2 = {2,3,4}
a1.intersection_update(a2)
print(a1)

# to get everything except duplicates

a1 = {1,2,3}
a2 = {2,3,4}
a1.symmetric_difference_update(a2)
print(a1)