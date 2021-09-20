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

#def find_longest_length(string):    #Самая длинная подстрока
    #count_char = []
    #for index, value in string:
        #if sting.count(value) > 1:
        #    count_char.append(index)
        #elif string[-1] = value:



def make_user(name, age):
    slov = dict(name = name,age = age)
    return slov

def format_user(slov):
    result = ''
    for v in slov.values():
        if result == '':
            result += v + ', '
        else:
            result += v
    return result

def count_all(li):
    di = {}
    for value in li:
        di[value] = li.count(value)
    return print(di)

def collect_indexes(di):
    di_res = {}
    for i, v in enumerate(di):
        di_res.setdefault(v, []).append(i)
    return di_res

def all_usnique(it):
    itset = set(it)
    if len(itset) == len(it):
        print(True)
    else:
        print(False)

def toggle(flag, li):
    if flag in li:
        li.discard(flag)
    else:
        li.add(flag)

def toggled(flag, li):
    li = li.copy()
    if flag in li:
        li.discard(flag)
        return li
    else:
        li.add(flag)
        return li

def diff_keys(old_di, new_di):
    di = {'kept': [], 'added': [], 'removed': []}
    new_di = set(new_di)
    old_di = set(old_di)
    for v in old_di:
        if v in new_di:
            di['kept'].append(v)
        elif v not in new_di:
            di['removed'].append(v)
    for v in new_di:
        if v not in old_di:
            di['added'].append(v)
    return di

print(diff_keys({'name': 'Bob', 'age' : 42}, {}))
print(diff_keys({}, {'name': 'Bob', 'age' : 42}))
print(diff_keys({'a' : 1}, {'a': 2}))
