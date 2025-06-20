arr = []
for i in range(14):
    arr.append(int(input('Enter a number: ')))
arr.append(sum(arr))
for num in arr:
    print(num)

