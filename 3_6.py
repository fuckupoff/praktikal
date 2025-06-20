def odd_pos(arr):
    res = 1
    for i in range(len(arr)):
        if i % 2 != 0:
            res *= arr[i]
    return res
print(odd_pos([2,3,4,5,6]))