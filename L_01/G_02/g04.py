import sys
import math

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

print(func(lambda x : x%2 != 0, 3))
print(func(lambda x : x < 0, -1))
print(func2args(lambda x, y: abs(x) < abs(y), 4, -3))
print(func2args(lambda x, y : (math.sqrt(x**2 + y**2), math.atan2(y,x)), 2, 2))
print(func5(lambda x, y : x + y, lambda x, y : x * y, lambda x, y : x > y, 1, 2, 3))
print(func6(lambda x : x > 0, [1, 2, 3]))
print(func7(lambda x : x < 0, [-1, 2, 3]))
print(func8([1, 2], [1, 2, 3, 4]))
