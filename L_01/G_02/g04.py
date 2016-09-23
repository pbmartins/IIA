import sys
import math
from functools import reduce

def func(f, x):
    return f(x)

def func2args(f, x, y):
    return f(x, y)

def func8(f, lst_1, lst_2):
    if lst_1 == []:
        return True
    if not f(lst_1[0], lst_2):
        return False
    lst_2.remove(lst_1[0])
    return func8(f, lst_1[1:], lst_2)

def func9(f, lst, head=True, min_elem=None):
    if head:
        if lst == []:
            return None
        min_elem = lst[0]
    if lst == []:
        return min_elem
    if f(lst[0], min_elem):
        return func9(f, lst[1:], False, lst[0])
    return func9(f, lst[1:], False, min_elem)

def func10(f, lst, head=True, min_elem=None, to_rtn=[]):
    if head:
        if lst == []:
            return None
        min_elem = lst[0]
    if lst == []:
        return min_elem, to_rtn
    if f(lst[0], min_elem):
        return func10(f, lst[1:], False, lst[0], to_rtn + [min_elem])
    return func10(f, lst[1:], False, min_elem, to_rtn + [lst[0]])

def func11(f, lst, min_elem=[], head=True, ret_lst=[]):
    if lst == []:
        return None if head else min_elem[0], min_elem[1], ret_lst
    if head or len(min_elem) < 2:
        return func11(f, lst[1:], min_elem + [lst[0]], False, ret_lst)
    if f(lst[0], min_elem[0]) or f(lst[0], min_elem[1]):
        tmp = min_elem + [lst[0]]
        min_1 = min(tmp)
        tmp.remove(min_1)
        min_2 = min(tmp)
        tmp.remove(min_2)
        return func11(f, lst[1:], [min_1, min_2], False, ret_lst + [tmp[0]])
    return func11(f, lst[1:], min_elem, False, ret_lst + [lst[0]])

#####################################
# map()
def apply(f, lst):
    return [] if lst == [] else [f(lst[0])] + apply(f, lst[1:])

# filter()
def filt(f, lst):
    if lst == []:
        return []
    if f(lst[0]):
        return [lst[0]] + filt(f, lst[1:])
    return filt(f, lst[1:])

# reduce()
def reduc(f, lst, null):
    return null if lst == [] else f(lst[0], reduc(f, lst[1:], null))


#######################################

def func13(f, lst_1, lst_2):
    if lst_1 == [] and lst_2 == []:
        return []
    if lst_1 == []:
        return lst_2
    if lst_2 == []:
        return lst_1
    return [lst_1[0]] + func13(f, lst_1[1:], lst_2) if f(lst_1[0], lst_2[0])\
            else [lst_2[0]] + func13(f, lst_1, lst_2[1:])

def conc_aplic(f, lst):
    return [] if lst == [] \
            else list(map(lambda x : f(x), lst[0])) + conc_aplic(f, lst[1:])
    # return [] if lst == [] else [f(x) for x in lst[0]] + conc_aplic(f, lst[1:])

def aplic_combin(f, lst_1, lst_2):
    if lst_1 == [] and lst_2 == []:
        return []
    elif lst_1 == [] or lst_2 == []:
        return None
    lst = aplic_combin(f, lst_1[1:], lst_2[1:])
    return [f(lst_1[0], lst_2[0])] + lst if not lst == None else None

def func16(f, lst, null):
    return [] if lst == [] \
            else [reduce(lambda x,s : f(x, s), lst[0], null)] + func16(f, lst[1:], null)
    # return [] if lst == [] else [f(x) for x in lst[0]] + func16(f, lst[1:], null)

print(func(lambda x : x%2 != 0, 3))
print(func(lambda x : x < 0, -1))
print(func2args(lambda x, y: abs(x) < abs(y), 4, -3))
print(func2args(lambda x, y : (math.sqrt(x**2 + y**2), math.atan2(y,x)), 2, 2))

func5 = lambda f, g, h : lambda x, y, z : h(f(x, y), g(y, z))
print(func5(lambda x, y : x + y, lambda x, y : x * y, lambda x, y : x > y)(1, 2, 3))

func6 = lambda f, lst : all([f(x) for x in lst])
print(func6(lambda x : x > 0, [1, 2, 3]))

func7 = lambda f, lst : any([f(x) for x in lst])
print(func7(lambda x : x < 0, [-1, 2, 3]))

# No repetitions
func8_v2 = lambda lst1, lst_2 : [x for x in lst_1 if x in lst_2] == lst_1 
# With repetitions
print(func8(lambda x, lst : x in lst, [1, 2], [1, 2, 3, 4]))

print(func9(lambda x, y : x < y, [1, 2, 3, 4]))

print(func10(lambda x, y : x < y, [1, 2, 3, 4]))

print(func11(lambda x, y : x < y, [1, 2, 3, 4]))

func12 = lambda f, lst : [f(x[0], x[1]) for x in lst]
print(func12(lambda x, y : (math.sqrt(x**2 + y**2), math.atan2(y, x)), [(1, 2), (3, 4)]))

print(func13(lambda x, y : x <= y, [1, 2, 3], [2, 5, 6]))

func14 = lambda f, lists : [f(x) for sublist in lists for x in sublist]
print(func14(lambda x : x**2, [[1, 2, 3], [4, 5, 6]]))
print(conc_aplic(lambda x : x**2, [[1, 2, 3], [4, 5, 6]]))

func15 = lambda f, lst_1, lst_2 : [f(x[0], x[1]) for x in zip(lst_1, lst_2)] \
        if len(lst_1) == len(lst_2) else None
print(func15(lambda x, y : x * y, [1, 2, 3], [1, 2, 3]))
print(aplic_combin(lambda x, y : x * y, [1, 2, 3], [1, 2, 3]))

func16_v2 = lambda f, lists, null : \
        [reduce(lambda x, s : f(x, s), sublist, null) for sublist in lists]
print(func16_v2(lambda x, s : x * s, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(func16(lambda x, s : x * s, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
