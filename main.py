import math


def get_square_roots(num):
    defult_list = []
    defult_list.append(-math.sqrt(num))
    defult_list.append(math.sqrt(num))
    return print(defult_list)

def get_range(n):
    defult_list1 = []
    i = 0
    while i < n:
        defult_list1.append(i)
        i += 1
    if i > n and n == 0:
        return print(defult_list1)
    return print(defult_list1)

def duplicate(li):
	return li.extend(li)

def rotatelist(li):
    if li == []:
        return print(li)
    else:
        li.insert(0, li.pop())
        return print(li)

def rotated_left(lststr):
    lststr = lststr[1::] + lststr[0:1:]
    return print(lststr)

def rotated_right(lststr):
    lststr = lststr[-1::] + lststr[0:-1:]
    return print(lststr)

def find_index(felem ,li):
    for (index, elem) in enumerate(li):
        if felem == elem:
            return index
            break 
        else:
            None


def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    second = find_index(value, iterator)
    if second is not None:
        return second

def is_continuous_sequence(li):
    if li == []:
        return False
    new_li = list(range(li[0], (li[0] + len(li))))
    if len(li) == 0 or len(li) == 1:
        return False
    elif new_li == li:
        return True
    else: 
        return False
            
        

print(is_continuous_sequence([10, 11, 12, 13]))
print(is_continuous_sequence([-5, -4, -3]))
print(is_continuous_sequence([10, 11, 12, 14, 15]))
print(is_continuous_sequence([1, 2, 2, 3]))
print(is_continuous_sequence([13]))
print(is_continuous_sequence([]))
