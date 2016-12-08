import sys

def length(lst):
    return 0 if lst == [] else 1 + length(lst[1:])

def sum_elems(lst):
    return 0 if lst == [] else int(lst[0]) + sum_elems(lst[1:])

def check_elem(lst, elem):
    if lst == []:
        return False
    if lst[0] == elem:
        return True
    return check_elem(lst[1:], elem)

def concatenate(lst_1, lst_2):
    if lst_2 == []:
        return []
    if lst_1 == []:
        return lst_2[0:1] + concatenate(lst_1, lst_2[1:])
    return lst_1[0:1] + concatenate(lst_1[1:], lst_2)

def inverse(lst):
    return [] if lst == [] else lst[-1:] + inverse(lst[:-1])

def capicua(lst):
    if lst == []:
        return True
    return capicua(lst[1:-1]) if lst[0] == lst[-1] else False

def concatenate_lists(lst_of_lst):
    return [] if lst_of_lst == [] else lst_of_lst[0] + concatenate_lists(lst_of_lst[1:])

def subst_elem(lst, x, y):
    if lst == []:
        return []
    return [y] + subst_elem(lst[1:], x, y) if lst[0] == x else [lst[0]] + subst_elem(lst[1:], x, y)

def list_union(lst_1, lst_2):
    if lst_1 == [] and lst_2 == []:
        return []
    if lst_1 == []:
        return lst_2
    if lst_2 == []:
        return lst_1
    return [lst_1[0]] + list_union(lst_1[1:], lst_2) if lst_1[0] < lst_2[0] \
            else [lst_2[0]] + list_union(lst_1, lst_2[1:])
    
def sub_lists(lst):
    if lst == []:
        return [[]]
    ls = sub_lists(lst[1:])
    return ls + [[lst[0]] + x for x in ls] if [lst[0]] not in ls else ls

print(sys.argv)
print(length(sys.argv[1:]))
print(sum_elems(sys.argv[1:]))
print(check_elem(sys.argv[1:], '3'))
print(concatenate(sys.argv[1:3], sys.argv[-1:]))
print(inverse(sys.argv[1:]))
print(capicua(sys.argv[1:]))
print(concatenate_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(subst_elem(sys.argv[1:], '3', '4'))
print(list_union([1, 2, 3, 5], [2, 4, 6]))
print(sub_lists([1, 1, 2, 3]))
print(sub_lists([1, 2, 3]))
