def quicksort(lst):
    if len(lst) <= 1:
        return lst
    return quicksort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + \
            quicksort([x for x in lst[1:] if x >= lst[0]])

print(quicksort([2, 7, 3, 4, 1]))
