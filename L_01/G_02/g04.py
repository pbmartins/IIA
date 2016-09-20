import sys
import math
from functools import reduce

def func(f, x):
    return f(x)

def func2args(f, x, y):
    return f(x, y)

def func5(f, g, h, x, y, z):
    return h(f(x, y), g(y, z))

def func6(f, lst):
    for item in lst:
        if not f(item):
            return False
    return True

def func7(f, lst):
    for item in lst:
        if f(item):
            return True
    return False

def func8(lst_1, lst_2):
    for elem in lst_1:
        if not elem in lst_2:
            return False
    return True

def func9(f, lst):
    if lst == []:
        return None
    ## Incomplete

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

def conc_aplic(f, lst):
    return [] if lst == [] else list(map(lambda x : f(x), lst[0])) + conc_aplic(f, lst[1:])
    # return [] if lst == [] else [f(x) for x in lst[0]] + conc_aplic(f, lst[1:])

def aplic_combin(f, lst_1, lst_2):
    if lst_1 == [] and lst_2 == []:
        return []
    elif lst_1 == [] or lst_2 == []:
        return None
    lst = aplic_combin(f, lst_1[1:], lst_2[1:])
    return [f(lst_1[0], lst_2[0])] + lst if not lst == None else None

def func16(f, lst, null):
    return [] if lst == [] else [reduce(lambda x,s : f(x, s), lst[0], null)] + func16(f, lst[1:], null)
    # return [] if lst == [] else [f(x) for x in lst[0]] + func16(f, lst[1:], null)

print(func(lambda x : x%2 != 0, 3))
print(func(lambda x : x < 0, -1))
print(func2args(lambda x, y: abs(x) < abs(y), 4, -3))
print(func2args(lambda x, y : (math.sqrt(x**2 + y**2), math.atan2(y,x)), 2, 2))
print(func5(lambda x, y : x + y, lambda x, y : x * y, lambda x, y : x > y, 1, 2, 3))
print(func6(lambda x : x > 0, [1, 2, 3]))
print(func7(lambda x : x < 0, [-1, 2, 3]))
print(func8([1, 2], [1, 2, 3, 4]))



print(conc_aplic(lambda x : x**2, [[1, 2, 3], [4, 5, 6]]))
print(aplic_combin(lambda x,y : x*y, [1, 2, 3], [1, 2, 3, 4]))
print(func16(lambda x,s : x * s, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
