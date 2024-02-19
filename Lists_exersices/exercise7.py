# Python | Cloning or Copying a list

# Using the slicing technique 
lst = [12, 74, 68, 894]
clone_lst = lst[:]
print(clone_lst)

# Using the extend() method 
clone_lst = []  
clone_lst.extend(lst)
print(clone_lst)

# List copy using =(assignment operator)
clone_lst = []
clone_lst = lst
print(clone_lst)

# Using the method of Shallow Copy 
clone_lst = lst.copy()
print(clone_lst)

# Using list comprehension 
clone_lst = [num for num in lst]
print(clone_lst)

# Using the append() method 
clone_lst = []
for num in lst :
    clone_lst.append(num)
print(clone_lst)

# Using the copy() method 

# Using the method of Deep Copy

# Using the map method 

# Using slice() function: