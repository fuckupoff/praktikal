new_dict = []
while True:
    i = input()
    if i == '':
        break
    new_dict.append(i)
min_num = min(new_dict, key=len)
max_num = max(new_dict, key=len)
print(min_num, max_num)
