def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
lst = [8, 1, 3, 5, 19, 4]
print(change(lst))
