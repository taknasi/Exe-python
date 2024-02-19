# Given a list, write a Python program to swap first and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# my solution

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    middle = new_lst[1:-1]
    new_lst.reverse()
    new_lst[1:-1] = middle
    return new_lst
print(swaplist(lst))   

# some other solutions

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    new_lst[0], new_lst[-1] = new_lst[-1], new_lst[0]
    return new_lst
print(swaplist(lst)) 

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    reversed_items = new_lst[0], new_lst[-1]
    new_lst[-1], new_lst[0] = reversed_items
    return new_lst
print(swaplist(lst)) 

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    first_item = new_lst[0]
    new_lst[0] = new_lst[-1]
    new_lst[-1] = first_item
    return new_lst
print(swaplist(lst)) 

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    new_lst = new_lst[-1:] + new_lst[1:-1] + new_lst[:1]
    return new_lst
print(swaplist(lst))

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    first_item = new_lst.pop(0)
    last_item = new_lst.pop(-1)
    new_lst.insert(0, last_item)
    new_lst.append(first_item)
    return new_lst
print(swaplist(lst)) 

lst = [12, 35, 9, 56, 24]
def swaplist(new_lst):
    start, *middle, end = new_lst
    new_lst = [end, *middle, start]
    return new_lst
print(swaplist(lst))