import math

f1 = lambda x: x % 2 != 0
f2 = lambda x: x > 0
f3 = lambda x, y: abs(x) < abs(y)
f4 = lambda x, y: (math.sqrt(x**2 + y**2), math.atan2(y, x))
f5 = lambda h, f, g: lambda x, y, z: h(f(x, y), g(y, z))
f6 = lambda f, lst: all([f(x) for x in lst])
f7 = lambda f, lst: any([f(x) for x in lst])
f8 = lambda lst1, lst2: len([x for x in lst1 if x in lst2]) == len(lst1)

# Counting repetitions
def func8(f, lst_1, lst_2):
    if lst_1 == []:
        return True
    if not f(lst_1[0], lst_2):
        return False
    lst_2.remove(lst_1[0])
    return func8(f, lst_1[1:], lst_2)

def f9(f, lst, min_elem=None, head=True):
    if lst == []:
        return None if head else min_elem
    if head:
        return f9(f, lst[1:], lst[0], False)
    return f9(f, lst[1:], lst[0], False) \
            if f(lst[0], min_elem) else f9(f, lst[1:], min_elem, False)

def f10(f, lst, head=True):
    if len(lst) < 2 and head:
        return None
    if len(lst) == 1:
        return lst[0], []
    min_elem, other_lst = f10(f, lst[1:], False)
    return (lst[0], other_lst + [min_elem]) if f(lst[0], min_elem) \
            else (min_elem, other_lst + [lst[0]])

def f11(f, lst, head=True):
    if len(lst) < 2 and head:
        return None
    if len(lst) == 1:
        return lst, []
    min_elem, other_lst = f11(f, lst[1:], False)
    min_elem += [lst[0]]
    if len(min_elem) < 3:
        return (min_elem, other_lst)
    max_elem = get_max(f, min_elem)
    min_elem.remove(max_elem)
    return (min_elem, other_lst + [max_elem])

def get_max(f, lst):
    max_list = [x for x in lst[1:] if not f(x, lst[0]) and x != lst[0]]
    return lst[0] if max_list == [] else get_max(f, max_list)

f12 = lambda lst: [(math.sqrt(item[0]**2 + item[1]**2), \
        math.atan2(item[1], item[0])) for item in lst]

def f13(f, lst1, lst2):
    if lst1 == [] and lst2 == []:
        return []
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    if f(lst1[0], lst2[0]):
        lst = f13(f, lst1[1:], lst2)
        return [lst1[0]] + lst
    else:
        lst = f13(f, lst1, lst2[1:])
        return [lst2[0]] + lst

f14 = lambda f, lst: [f(x) for sublist in lst for x in sublist]
f15 = lambda f, lst: [f(x[0], x[1]) for x in zip(lst[0], lst[1])]

def reduc(f, lst, null):
    return null if lst == [] else f(lst[0], reduc(f, lst[1:], null))

f16 = lambda f, lst, null: [reduc(f, sublist, null) for sublist in lst]

print(f1(3))
print(f2(3))
print(f3(2, 3))
print(f4(2, 2))
print(f5(lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y)(1, 2, 3))
print(f6(lambda x: x > 0, [-1, 2, 3]))
print(f7(lambda x: x > 0, [-1, 2, 3]))
print(f8([1, 2], [1, 2, 4]))
print(f9(lambda x, y: x < y, [1, -1, 4, 9]))
print(f10(lambda x, y: x < y, [1, -1, 4, 9]))
print(f11(lambda x, y: x < y, [1, -1, 4, 9]))
print(f12([(2, 2), (1, 2), (4, 5)]))
print(f13(lambda x, y: x < y, [1, 3, 5], [2, 4]))
print(f14(lambda x: x**2, [[1, 2, 3], [4, 5, 6]]))
print(f15(lambda x, y: x * y, [[1, 2, 3], [1, 2, 3]]))
print(f16(lambda s, x: s + x, [[1, 2, 4], [1, 2, 3]], 0))

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
def redu(f, lst, null):
    return null if lst == [] else f(lst[0], redu(f, lst[1:], null))


#######################################
