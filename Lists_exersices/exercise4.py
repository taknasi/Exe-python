# Check if element exists in list in Python
# Input: test_list = [1, 6, 3, 5, 3, 4]
# Check if 3 exist or not
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list

lst = [1, 6, 3, 5, 3, 4]

# Using “in” Statement 
def check_member(test_list, num) :
   print (num in lst)
check_member(lst, 3)   

# Using a loop 
for num in lst:
   check = 3 in lst
print(check)

# Using any() function
checking = any(num == 3 for num in lst)
print(checking)

# Using count() function
exist_count = lst.count(3)
if exist_count > 0 :
   print("Number 3 exist in list")

# print ([[num, lst.count(num)] for num in set(lst)])

# Using sort with bisect_left and set()

# Using find() method
lst_of_str = list(map(str, lst))
new_str = " ".join(lst_of_str)
if new_str.find("3") != -1 :
   print("Number 3 exist in list")
else:
   print("Number 3 not exist in list")   

# Using Counter() function
from collections import Counter
new_dict = Counter(lst)
if new_dict[3] > 0 :
      print("Number 3 exist in list")
else:
   print("Number 3 not exist in list")   

# Using try-except block
def exist_element(list, element):
   try :
      list.index(element)
      return True
   except ValueError :
      return False
print(exist_element(lst, 7))
