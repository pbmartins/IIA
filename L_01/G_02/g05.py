def selectionsort(f, lst):
    if len(lst) <= 1:
        return lst
    minimum = get_min(f, lst)
    return [x for x in lst if x == minimum] \
            + selectionsort(f, [x for x in lst if x != minimum])

def get_min(f, lst):
    min_list = [x for x in lst[1:] if f(x, lst[0])]
    return lst[0] if min_list == [] else get_min(f, min_list)

def bubblesort(f, lst):
    if len(lst) <= 1:
        return lst
    lst = bubble_aux(f, lst)
    return bubblesort(f, lst[:-1]) + [lst[-1]]

def bubble_aux(f, lst):
    if len(lst) <= 1:
        return lst
    return [lst[1]] + bubble_aux(f, [lst[0]] + lst[2:]) if f(lst[1], lst[0]) \
            else [lst[0]] + bubble_aux(f, lst[1:])

def quicksort(f, lst):
    if len(lst) <= 1:
        return lst
    return quicksort(f, [x for x in lst[1:] if f(x, lst[0])]) + [lst[0]] + \
            quicksort(f, [x for x in lst[1:] if not f(x, lst[0])])

print(selectionsort(lambda x, y : x < y, [1, 2, 7, 3, 4, 1]))
print(bubblesort(lambda x, y : x < y, [2, 7, 3, 1, 4, 1]))
print(quicksort(lambda x, y : x < y, [2, 7, 1, 3, 4, 1]))
