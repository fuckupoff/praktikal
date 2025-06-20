def nums_od (num):
    list_num = str(num)
    for i in range(len(list_num) - 1):
        if list_num[i] <= list_num[i+1]:
            return False
    return True
print(nums_od(7431))
print(nums_od(789))