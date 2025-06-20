def task_2(arr: list):
    sum_pos = sum(x for x in arr if x > 0)

    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    start, end = sorted([min_idx, max_idx])

    product = 1
    for num in arr[start + 1: end]:
        product *= num

    return (sum_pos, product)

arr = [3, -1, 4, -2, 5, -6, 2]
print(task_2(arr))