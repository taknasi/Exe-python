# Reversing a List in Python
# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4] 
# Explanation: The list we are having in the output is reversed to the list we have in the input.

# Using the slicing technique
lst = [4, 5, 6, 7, 8, 9]
def reverse_lst(lst):
    lst = lst[::-1]
    return lst
print(reverse_lst(lst))

# Reversing list by swapping present and last numbers at a time

# Using the reversed() and reverse() built-in function
lst.reverse()
print(lst)


# Using a two-pointer approach

# Using the insert() function
lst = [4, 5, 6, 7, 8, 9]
new_lst = []
for num in lst:
    new_lst.insert(0, num)    
print(new_lst)

# Using list comprehension
lst = [4, 5, 6, 7, 8, 9]
new_list = [lst[len(lst) - i] for i in range(1, len(lst)+1)]
print(new_list)

  # for i in range(1, len(lst + 1))
  # new_lst = [lst[len(lst) - 1]]
  # new_lst = [lst[len(lst) - 2]]
  # new_lst = [lst[len(lst) - 3]]
  # new_lst = [lst[len(lst) - 4]]
 # new_lst = [lst[len(lst) - 5]]
  # new_lst = [lst[len(lst) - 6]]

# Reversing a list using Numpy
