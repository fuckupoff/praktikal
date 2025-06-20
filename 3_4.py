def pos_nums_arr (arr):
    q_pos_nums = 0
    for i in arr:
        if i > 0:
            q_pos_nums += 1
    return q_pos_nums
print(pos_nums_arr([1,-2,3,-4,5]))