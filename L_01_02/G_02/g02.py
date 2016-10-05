import sys

def unzipe(lst):
    if lst == []:
        return ([], [])
    l_a, l_b = unzipe(lst[1:])
    return [lst[0][0]] + l_a, [lst[0][1]] + l_b

def remove_count(lst, elem):
    if lst == []:
        return [], 0
    ls, count = remove_count(lst[1:], elem)
    return (ls, count + 1) if x == lst[0] else ([lst[0]] + ls, count)

# Using dictionary
def check_count(lst):
    if lst == []:
        return dict()
    d = check_count(lst[1:])
    if lst[0] in d:
        d[lst[0]] += 1
    else:
        d[lst[0]] = 1
    return d


# Using tuples
def count(lst):
    if lst == []:
        return []
    ls = count(lst[1:])
    elems = [x[0] for x in ls]
    if lst[0] in elems:
        return [x if x[0] != lst[0] else (x[0], x[1] + 1) for x in ls]
    else:
        return ls + [(lst[0], 1)]


print(unzipe([(1, 'a'), (2, 'b'), (3, 'c')]))
print(remove_count([1, 6, 2, 5, 5, 2, 5, 2], 2))
print(check_count([1, 6, 2, 5, 5, 2, 5, 2]))
