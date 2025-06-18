def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
lst = [10, 2, 3, 4, 5, 0]
print(change(lst))