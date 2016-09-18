import sys

def first_elem(lst):
    return None if lst == [] else lst[0]

def tail(lst, head=True):
    if lst == []: 
        if head:
            return None
        return []
    if head:
        return tail(lst[1:], False)
    return [lst[0]] + tail(lst[1:], False)

def same_elems(l1, l2):
    if l1 == [] and l2 == []:
        return []
    elif (l1 == [] and not l2 == []) or (not l1 == [] and l2 == []):
        return None
    if l1[0] == l2[0]:
        return [l1[0]] + same_elems(l1[1:], l2[1:])
    return same_elems(l1[1:], l2[1:])

def smaller(lst, min_elem=None, head=True):
    if lst == []:
        return min_elem
    if head or lst[0] < min_elem:
        return smaller(lst[1:], lst[0], False)
    return smaller(lst[1:], min_elem, False)

def smaller_list(lst, min_elem=None, head=True, ret_lst=[]):
    if lst == []:
        return None if head else min_elem, ret_lst
    if head:
        return smaller_list(lst[1:], lst[0], False, ret_lst)
    if lst[0] < min_elem:
        return smaller_list(lst[1:], lst[0], False, ret_lst + [min_elem])
    return smaller_list(lst[1:], min_elem, False, ret_lst + [lst[0]])

def max_min(lst, min_elem=None, max_elem=None, head=True):
    if lst == []:
        return None if head else min_elem, max_elem
    if head:
        return max_min(lst[1:], lst[0], lst[0], False)
    if lst[0] < min_elem:
        return max_min(lst[1:], lst[0], max_elem, False)
    if lst[0] > max_elem:
        return max_min(lst[1:], min_elem, lst[0], False)
    return max_min(lst[1:], min_elem, max_elem, False)

def min_list(lst, min_elem=[], head=True, ret_lst=[]):
    if lst == []:
        return None if head else min_elem[0], min_elem[1], ret_lst
    if head or len(min_elem) < 2:
        return min_list(lst[1:], min_elem + [lst[0]], False, ret_lst)
    if lst[0] < min_elem[0] or lst[0] < min_elem[1]:
        tmp = min_elem + [lst[0]]
        min_1 = min(tmp)
        tmp.remove(min_1)
        min_2 = min(tmp)
        tmp.remove(min_2)
        return min_list(lst[1:], [min_1, min_2], False, ret_lst + [tmp[0]])
    return min_list(lst[1:], min_elem, False, ret_lst + [lst[0]])

def medium(lst, aux=[], elem_sum=0, cp=False, head=True):
    if not cp:
        return medium(lst, lst, elem_sum, True, head)
    if aux == []:
        return None if head else elem_sum / len(lst), lst[int(len(lst)/2)]
    return medium(lst, aux[1:], elem_sum + aux[0], True, False)

print(first_elem([]))
print(tail([1, 2, 3]))
print(same_elems([1, 2, 3], [1, 3, 3]))
print(smaller([1, 2, 3, -1]))
print(smaller_list([1, 2, -3, 3, -1]))
print(max_min([1, 2, -3, 3, -1]))
print(min_list([1, 2, 5, 3, -1]))
print(medium([1, 2, 5, 3, -1]))
