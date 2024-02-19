# Find the Length of a List in Python
# Input: lst = [10,20,30,40]
# Output: 4

# Using len() function
lst = [10,20,30,40]
print(f"The length of list is: {len(lst)}")

# Using Naive Method
count = 0
for num in lst:
    count +=1
print(f"The lenght of list is: {count}")

# Using length_hint()   
from operator import length_hint
print(f"The length of list is: {length_hint(lst)}")

# Using a list comprehension & sum() method
lenght_lst = sum(1 for num in lst)
print(f"The lenght of list is: {lenght_lst}")

# Using Collections Module
from collections import Counter
lenght_lst = sum(Counter(lst).values())
print(f"The lenght of list is: {lenght_lst}")
 
# Using enumerate function

# Using recursion