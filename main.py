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

def apply_diff(target, diff):
    for v in diff:
        if v == 'add':
            target.update(diff['add'])
        elif v == 'remove':
            target.symmetric_difference_update(diff['remove'])

def to_rna(dnk):
    dnk1 = 'GCTA'
    rnk1 = 'CGAU'
    rna = ''
    for v in dnk:
        for i, value in enumerate(dnk1):
            if v == value:
                rna += rnk1[i]
    print(rna)

def build_query_string(dict):
    str_e = ''
    count = len(list(dict.keys()))
    i = 0
    for k, v in dict.items():
        str_e += k + '=' + str(v)
        i += 1
        if count > i:
            str_e += '&'
    print(str_e)

dict_num = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
def to_roman(n):
    result = ''
    for arabic, roman in dict_num.items():
        result += n // arabic * roman
        n %= arabic
    return result


dict_num = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}   # myself
dict_num_1 =  {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
def to_arabic(n):
    result = 0
    for arabic, roman in dict_num_1.items():
        if roman in n:
            n = n.replace(roman, "")
            result += arabic
    for arabic, roman in dict_num.items():
        for value in n:
            if roman == value:
                result += arabic
    return result



def find_where(books, value):
    for i in books:
        i1 = i.copy()
        i1.update(value)
        if i == i1:
            return print(i)
        else:
            print(None)


books = [
        {'title': 'Book of Foos', 'author': 'Foo', 'year': 1111},
        {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
        {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
        {'title': 'Book of Foos Bars', 'author': 'FooBar', 'year': 22222},
        {'title': 'Book of Foos Fix', 'author': 'FooFix', 'year': 123123},
        {'title': 'Book of Foos Mood', 'author': 'FooMood', 'year': 1611},
        {'title': 'Book of Foos', 'author': 'Foo', 'year': 1111},
        ]

find_where(books, {'author': 'FooBar'})
