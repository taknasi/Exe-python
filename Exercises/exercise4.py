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
   print("Number 3 exusts in list")

print ([[num, lst.count(num)] for num in set(lst)])

# Using sort with bisect_left and set()
sort_lst = lst.sort()
print(set(sort_lst))
# Using find() method

# Using Counter() function

# Using try-except block