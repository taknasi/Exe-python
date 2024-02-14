# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Solutions in exercuse1 can be worked in this exercise

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
def swapPositions(new_lst, pos1, pos2):
    new_lst[pos1], new_lst[pos2] = new_lst[pos2], new_lst[pos1]
    return new_lst
print(swapPositions(lst, pos1-1, pos2-1))

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
def swapPositions(new_lst, pos1, pos2):
    first_item = new_lst[pos1]
    new_lst[pos1] = new_lst[pos2]
    new_lst[pos2] = first_item
    return new_lst
print(swapPositions(lst, pos1-1, pos2-1))

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
def swapPositions(new_lst, pos1, pos2):
    positions = new_lst[pos1], new_lst[pos2]
    new_lst[pos2], new_lst[pos1] = positions
    return new_lst
print(swapPositions(lst, pos1-1, pos2-1))

lst = [23, 65, 19, 90]
pos1, pos2  = 1, 3
def swapPositions(new_lst, pos1, pos2):
    position1 = new_lst.pop(pos1)
    position2 = new_lst.pop(pos2-1)
    new_lst.insert(0, position2)
    new_lst.insert(2, position1)
    return new_lst
print(swapPositions(lst, pos1-1, pos2-1))

# etc