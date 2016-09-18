import sys

def unzipe(lst):
    if lst == []:
        return ([], [])
    l_a, l_b = unzipe(lst[1:])
    a, b = lst[0]
    return [a] + l_a, [b] + l_b

def remove_count(lst, elem):
    if lst == []:
        return [], 0
    l, count = remove_count(lst[1:], elem)
    if lst[0] == elem:
        count += 1
    else:
        l = [lst[0]] + l
    return l, count

def check_count(lst):
    if lst == []:
        return dict()
    d = check_count(lst[1:])
    if lst[0] in d:
        d[lst[0]] += 1
    else:
        d[lst[0]] = 1
    return d



print(unzipe([(1, 'a'), (2, 'b'), (3, 'c')]))
print(remove_count([1, 6, 2, 5, 5, 2, 5, 2], 2))
print(check_count([1, 6, 2, 5, 5, 2, 5, 2]))
