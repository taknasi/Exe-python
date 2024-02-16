# Different ways to clear a list in Python.
# Input: [2, 3, 5, 6, 7]
# Output: []
# Explanation: Python list is cleared and it becomes empty so we have returned empty list.

lst = [2, 3, 5, 6, 7]

# Using clear()
lst.clear()
print(lst)

# Reinitializing the list
lst = []
print(lst)

# Using “*= 0”
lst *= 0  # lst = lst * 0 
print(lst)

# Using del
del(lst[:])
print(lst)

# Using pop() method
lst = [lst.pop(num) for num in lst] # lst = [lst.remove(num) for num in lst]
print(lst)

# Using slicing
lst = lst[:0]
print(lst)