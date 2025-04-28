# Let's study the list which is a data structure in python
# List is a collection of items
# List is mutable, meaning we can change the items in the list.

users = ["John", "Jane", "Doe"]
Emp = ["John", 42, True]
EmptyList = []

print('John' in users)
print(users[0])
print(users[-1])
print(users.index("Jane"))
print(users[0:2])
print(users[1:])
print(users[-1:])
print(users[-3:-1])

print(users.count("John")) # count the number of times John appears in the list.
print(len(users)) # Lenght of the list.

print(users + Emp) # Concatenate the lists
print(users * 2) # Repeat the lits twice

# List Methods

users.append("Sonal") # Append the list with Sonal
print(users)
# or
users += ["Sonal"] # Append the list with Sonal
print(users)
# or
users.extend(["Mom", "Dad"])
print(users)
# users.extend(Emp)
# print(users)
users.insert(0, "Shona")
print(users)

users[2:2] = ["Rob", "Monty"] # Insert the items in the list at index 2
print(users)

users[1:3] = ["mohini", "Rocky"] # Replace the items in the list with new items
print(users)

# REmoving or deleting the items from the list

users.remove("Sonal")
print(users)

print(users.pop())

del users[1]
print(users)

del users[1:3]
print(users)

Emp.clear()
print(Emp)

# Sorting the list

users.sort() # Sort the list in ascending order
print(users)


# users[1:3] = ["bob"] 
# print(users)

# users.sort(key=str.lower) # Sort the list in ascending order ignoring the case
# print(users)

# nums = [34,5,67,8,98] 
# nums.reverse() # Reverse the list
# print(nums)

# nums.sort(reverse=True) # Sort the list in descending order
# print(nums)
# # or
# print(nums)
# print(sorted(nums, reverse=True)) # Sort the list in descending order and return a new list without changing the original list.
# # sorted is a global function which can be used to sort any iterable object.


# # copying the list with various methods

# myusers = nums.copy()
# mycopy = nums[:]
# userscopy = list(nums)

# print(myusers)
# print(mycopy)
# print(userscopy)

# # Tuples
# # Tuples are immutable, meaning we cannot change the items in the tuple.

# Mydata = ("sonal", 24, True)
# print(type(Mydata))

# # how to change the tuple

# Newlist = list(Mydata)
# Newlist.append("Indian")
# Newtuple = tuple(Newlist)
# print(Newtuple)

# (one, two, *three) = Newtuple
# print(one)
# print(two)
# print(three) # three wll take the rest of the items in the tuple.
