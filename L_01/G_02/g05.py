def selectionsort(f, lst):
    if len(lst) <= 1:
        return lst
    minimum = get_min(f, lst)
    return [minimum] + selectionsort(f, [x for x in lst if x != minimum])

def get_min(f, lst):
    min_list = [x for x in lst[1:] if f(x, lst[0])]
    return lst[0] if min_list == [] else get_min(f, min_list)

def bubblesort(f, lst):
    if len(lst) <= 1:
        return lst
    for i in range(0, len(lst)-1):
        if f(lst[i+1], lst[i]):
            lst[i+1], lst[i] = lst[i], lst[i+1]
    return bubblesort(f, lst[:-1]) + [lst[-1]]

def quicksort(f, lst):
    if len(lst) <= 1:
        return lst
    return quicksort(f, [x for x in lst[1:] if f(x, lst[0])]) + [lst[0]] + \
            quicksort(f, [x for x in lst[1:] if not f(x, lst[0])])

print(selectionsort(lambda x, y : x < y, [2, 7, 3, 4, 1]))

print(bubblesort(lambda x, y : x < y, [2, 7, 3, 4, 1]))

print(quicksort(lambda x, y : x < y, [2, 7, 3, 4, 1]))
