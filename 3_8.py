import random
arr = []
len_arr = random.randrange(1,25)
start = random.randrange(0,100) * 3
for i in range(len_arr):
    arr.append(start - 3 * i)
print(arr)