l = []
while True:
    s=input()
    if not s:
        break
    l.append(s)
print(min(l, key=len),max(l, key=len))